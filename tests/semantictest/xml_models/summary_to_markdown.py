from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

SUMMARY_PATH = Path("tests/semantictest/xml_models/class_summary.json")
OUTPUT_BASE = Path("tests/semantictest/output/new_markdown")

PRIMITIVE_TYPE_MAP: Dict[str, str] = {
    "characterstring": "str",
    "string": "str",
    "uuid": "str",
    "id": "str",
    "identifier": "str",
    "identifikation": "str",
    "integer": "int",
    "int": "int",
    "long": "int",
    "short": "int",
    "decimal": "float",
    "double": "float",
    "float": "float",
    "measure": "float",
    "number": "float",
    "real": "float",
    "boolean": "bool",
    "datetime": "datetime",
    "date": "date",
    "time": "time",
    "gm_point": "str",
    "gm_surface": "str",
    "gm_polygon": "str",
    "gm_curve": "str",
    "gm_multipoint": "str",
    "gm_multisurface": "str",
    "uri": "str",
    "reference": "str",
}


def slugify(value: str, allow_non_ascii: bool = False) -> str:
    raw = value or ""
    if allow_non_ascii:
        normalized = unicodedata.normalize("NFKC", raw)
        lowered = normalized.casefold()
        slug = re.sub(r"[^0-9\w]+", "_", lowered, flags=re.UNICODE).strip("_")
    else:
        normalized = unicodedata.normalize("NFKD", raw)
        normalized = normalized.encode("ascii", "ignore").decode("ascii")
        lowered = normalized.lower()
        slug = re.sub(r"[^0-9a-z]+", "_", lowered).strip("_")
    return slug or "item"


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    compact = " ".join(value.split())
    return compact.strip()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def clean_register_dir(path: Path) -> None:
    if not path.exists():
        return
    for child in path.glob("*.md"):
        child.unlink()


def value_type_for(attr: Dict[str, object]) -> str:
    type_name = (attr.get("typeName") or "").lower()
    primitive = PRIMITIVE_TYPE_MAP.get(type_name)
    if primitive:
        return primitive
    type_uml = (attr.get("typeUml") or "").lower()
    if type_uml in {"uml:enumeration", "uml:class", "uml:datatype"}:
        return "str"
    return "str"


def scale_for(value_type: str) -> str:
    if value_type in {"int", "float"}:
        return "MeasurementScale.RATIO"
    if value_type in {"datetime", "date", "time"}:
        return "MeasurementScale.INTERVAL"
    return "MeasurementScale.NOMINAL"


def attribute_slug(attr: Dict[str, object], fallback_index: int) -> str:
    if attr.get("typeName") == "Identifikation":
        return "id_lokalid"
    slug = slugify(str(attr.get("name", "")))
    if not slug:
        slug = f"attr_{fallback_index}"
    return slug


def attribute_description(attr: Dict[str, object]) -> str:
    doc = attr.get("documentation") or {}
    text = doc.get("definitionDa") or doc.get("commentDa") or ""
    desc = clean_text(text)
    return desc.replace('"', "'")


def attribute_cardinality(attr: Dict[str, object]) -> str:
    card = attr.get("cardinality")
    if card:
        return str(card)
    lower = attr.get("lowerMultiplicity")
    upper = attr.get("upperMultiplicity")
    if lower is not None and upper is not None:
        return f"{lower}..{upper}"
    return ""


def determine_role(attr: Dict[str, object], register_name: str, value_type: str) -> str:
    type_name = attr.get("typeName")
    if type_name == "Identifikation":
        return f"sg.PK({value_type})"

    if attr.get("isAssociation"):
        target = attr.get("foreignKeyTarget") or {}
        target_register = target.get("register") or register_name
        target_class = target.get("className") or type_name or attr.get("name", "")
        return f"sg.FK(dk.{target_register}.{target_class}, {value_type})"

    if (attr.get("typeUml") or "").lower() == "uml:enumeration":
        enum_name = type_name or attr.get("name", "")
        return f"sg.LOOKUP(dk.{register_name}.{enum_name}, {value_type})"

    return f"sg.DES({value_type})"


def build_attribute_lines(attrs: Iterable[Dict[str, object]], register_name: str) -> List[str]:
    lines: List[str] = []
    attrs = list(attrs)
    for idx, attr in enumerate(attrs):
        slug = attribute_slug(attr, idx)
        value_type = value_type_for(attr)
        scale = scale_for(value_type)
        role = determine_role(attr, register_name, value_type)
        desc = attribute_description(attr)
        cardinality = attribute_cardinality(attr)

        lines.append(f"        \"{slug}\": {{")
        lines.append(f"            \"scale\": {scale},")
        lines.append(f"            \"role\": {role},")
        lines.append(f"            \"cardinality\": \"{cardinality}\",")
        lines.append(f"            \"description\": \"{desc}\"")
        closing = "        }" + ("," if idx < len(attrs) - 1 else "")
        lines.append(closing)
    return lines


def format_dagi_sources(base_name: str, variants: List[Tuple[str, str]]) -> List[str]:
    if not variants:
        return []
    lines = [f"- {base_name} (aggregate)"]
    for variant_name, scale in sorted(variants, key=lambda item: int(item[1])):
        lines.append(f"- {variant_name} (1:{scale})")
    return lines


def generate_class_markdown(
    register_name: str,
    class_data: Dict[str, object],
    source_variants: List[str] | None = None,
) -> Tuple[str, str]:
    class_name = class_data.get("name", "Entity")
    entity_slug = slugify(class_name, allow_non_ascii=True)
    attrs = class_data.get("attributes") or []
    attr_lines = build_attribute_lines(attrs, register_name)

    doc = class_data.get("documentation") or {}
    definition = clean_text(doc.get("definitionDa")) or "Ingen definition tilgængelig."

    md_lines: List[str] = []
    md_lines.append("---")
    md_lines.append(f"title: {class_name}")
    md_lines.append("draft: false")
    md_lines.append("type: entity")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# {class_name}")
    md_lines.append("")
    md_lines.append(definition)
    md_lines.append("")
    if source_variants:
        md_lines.append("## Sources")
        md_lines.append("")
        md_lines.extend(source_variants)
        md_lines.append("")
    md_lines.append("### Semantic Template")
    md_lines.append("```python")
    md_lines.append("p.io.declare_input(")
    md_lines.append(f"    output_name=\"{entity_slug}\",")
    md_lines.append("    attributes={")
    if attr_lines:
        md_lines.extend(attr_lines)
    md_lines.append("    }")
    md_lines.append(")")
    md_lines.append("```")
    md_content = "\n".join(md_lines)
    filename = f"{entity_slug}.md"
    return filename, md_content


def generate_register_index(register_name: str, reg_data: Dict[str, object]) -> str:
    package = reg_data.get("registerPackage") or {}
    package_name = package.get("name") or register_name
    xml_file = reg_data.get("xmlFile", "ukendt")
    doc = reg_data.get("registerDocumentation") or {}
    definition = clean_text(doc.get("definitionDa")) or "Ingen definition tilgængelig."
    comment = clean_text(doc.get("commentDa")) or "—"
    example = clean_text(doc.get("exampleDa")) or "—"
    classes = reg_data.get("classes", [])
    attribute_total = sum(cls.get("attributeCount", len(cls.get("attributes", []))) for cls in classes)

    md_lines: List[str] = []
    md_lines.append("---")
    md_lines.append(f"title: {package_name}")
    md_lines.append("draft: false")
    md_lines.append("type: register")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# {package_name}")
    md_lines.append("")
    md_lines.append(definition)
    md_lines.append("")
    md_lines.append("## Registerpakke")
    md_lines.append(f"- Navn: {package_name}")
    md_lines.append(f"- ID: {package.get('id', 'ukendt')}")
    md_lines.append(f"- Kilde XML: {xml_file}")
    md_lines.append(f"- Antal klasser: {len(classes)}")
    md_lines.append(f"- Antal attributter: {attribute_total}")
    md_lines.append("")
    md_lines.append("## Dokumentation")
    md_lines.append(f"- definition (da): {definition}")
    md_lines.append(f"- comment (da): {comment}")
    md_lines.append(f"- example (da): {example}")
    return "\n".join(md_lines)


def dagi_variant_map(classes: List[Dict[str, object]]) -> Tuple[Dict[str, List[Tuple[str, str]]], set[str]]:
    pattern = re.compile(r"^(?P<base>.+)_(?P<scale>[0-9]+)$")
    variants: Dict[str, List[Tuple[str, str]]] = {}
    skip: set[str] = set()
    for cls in classes:
        name = cls.get("name", "")
        match = pattern.match(name)
        if not match:
            continue
        base = match.group("base")
        scale = match.group("scale")
        variants.setdefault(base, []).append((name, scale))
        skip.add(name)
    return variants, skip


def main() -> None:
    data = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    ensure_dir(OUTPUT_BASE)
    register_count = 0
    class_count = 0

    for register_name, reg_data in data.items():
        register_dir = OUTPUT_BASE / register_name
        ensure_dir(register_dir)
        clean_register_dir(register_dir)

        index_content = generate_register_index(register_name, reg_data)
        (register_dir / "index.md").write_text(index_content, encoding="utf-8")

        classes = sorted(reg_data.get("classes", []), key=lambda cls: cls.get("name", ""))
        dagi_variants: Dict[str, List[Tuple[str, str]]] = {}
        dagi_skip: set[str] = set()
        if register_name == "DAGI":
            dagi_variants, dagi_skip = dagi_variant_map(classes)

        for cls in classes:
            class_name = cls.get("name", "")
            if cls.get("isAbstract"):
                continue
            if register_name == "DAGI" and class_name in dagi_skip:
                continue
            sources = None
            if register_name == "DAGI":
                sources = format_dagi_sources(class_name, dagi_variants.get(class_name, []))
            filename, content = generate_class_markdown(register_name, cls, sources)
            (register_dir / filename).write_text(content, encoding="utf-8")
            class_count += 1

        register_count += 1

    print(f"Wrote {class_count} class files across {register_count} registers to {OUTPUT_BASE}")


if __name__ == "__main__":
    main()
