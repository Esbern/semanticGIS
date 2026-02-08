---
title: KommunaleForhold
draft: false
type: entity
---

# KommunaleForhold

oplysninger om kommunale forhold: Kommunernes eventuelle oplysning om, at vedkommende lever adskilt fra sin ægtefælle, er et plejebarn, pensionsforhold, tidligere opholdskommune mv

### Semantic Template
```python
p.io.declare_input(
    output_name="kommunaleforhold",
    attributes={
        "bemaerkninger": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "fritekstfelt til bemærkninger i tilknytning til kommunale forhold"
        },
        "kommunaleforholdskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "oplysningen indrapporteres af kommunerne, og værdimængden er ikke fastlagt på forhånd. Koder er forskellige fra kommune til kommune. Dog er nogle kendte og fælles"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "oplysningens gyldighedsstartdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "om gyldighedsstartdato er usikker"
        },
        "kommunaleforholdstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.KommunaleForholdstype, str),
            "cardinality": "1..1",
            "description": "angiver typen af kommunale forhold"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for oplysningen"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "oplysningens gyldighedsslutdato"
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