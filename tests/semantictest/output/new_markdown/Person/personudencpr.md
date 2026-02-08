---
title: PersonUdenCpr
draft: false
type: entity
---

# PersonUdenCpr

person som ikke har et CPR nummer. Anvendes som beholder for informationer om relationspersoner som er tilknyttet Personer med cprnummer men som ikke vides at have nogen anden tilknytning til Danmark. Dette kan fx. være ægtefæller der er udenlandske statsborger og som ikke bor i Danmark

### Semantic Template
```python
p.io.declare_input(
    output_name="personudencpr",
    attributes={
        "foedselsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "fødselsdato på personen"
        },
        "foedselsdatousikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at fødselsdato er usikker"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "navn på personen"
        },
        "navnemarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Navnemarkering, str),
            "cardinality": "0..1",
            "description": "angiver navnemarkering for navn på personen"
        },
        "foraelderoplysning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Foraelderoplysning, str),
            "cardinality": "0..*",
            "description": ""
        }
    }
)
```