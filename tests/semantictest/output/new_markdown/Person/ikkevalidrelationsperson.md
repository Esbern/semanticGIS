---
title: IkkeValidRelationsPerson
draft: false
type: entity
---

# IkkeValidRelationsPerson

person der er registreret i CPR med personnummer. Anvendes som beholder for borgerdata informationer med utilstrækkelig data, som er tilknyttet Personer

### Semantic Template
```python
p.io.declare_input(
    output_name="ikkevalidrelationsperson",
    attributes={
        "foedselsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "fødselsdato på IkkeValidRelationsPerson"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "navn på IkkeValidRelationsPerson"
        },
        "personnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "personnummer på IkkeValidRelationsPerson"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik identifikation for en person"
        },
        "gaeldendeperson": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.GeneriskPerson, str),
            "cardinality": "0..1",
            "description": ""
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