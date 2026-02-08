---
title: AdministrativEnhedType
draft: false
type: entity
---

# AdministrativEnhedType

administrativEnhedType indeholder typekode og typenavn for den administrative enhed

### Semantic Template
```python
p.io.declare_input(
    output_name="administrativenhedtype",
    attributes={
        "typekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "CPR's typekode for den administrative enhed"
        },
        "typenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "typenavnet for den administrative enhed"
        }
    }
)
```