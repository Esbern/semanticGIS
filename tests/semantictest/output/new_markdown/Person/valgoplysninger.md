---
title: Valgoplysninger
draft: false
type: entity
---

# Valgoplysninger

oplysninger om valgret til bl. a. folketinget for personer der er midlertidigt udrejst af landet eller er danske diplomater i udlandet. Desuden oplysninger om valg til EU

### Semantic Template
```python
p.io.declare_input(
    output_name="valgoplysninger",
    attributes={
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver om oplysningen er aktuel"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for valgoplysninger"
        },
        "valgoplysningstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Valgoplysningstype, str),
            "cardinality": "1..1",
            "description": "angiver hvilken type valgret personen har"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "slutdato for valgoplysninger"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "dato for startoplysninger"
        }
    }
)
```