---
title: AdministrativEnhed
draft: false
type: entity
---

# AdministrativEnhed

en myndighed eller et land som det er registreret i CPR

### Semantic Template
```python
p.io.declare_input(
    output_name="administrativenhed",
    attributes={
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den administrative enheds kode, der består af op til 4 cifre"
        },
        "landekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "hvis den administrative enhed er et land, udfyldes denne med landets landekode i formatet: ISO 3166-1 alpha-3"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den administrative enheds navn"
        },
        "administrativenhedtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhedType, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```