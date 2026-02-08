---
title: Notat
draft: false
type: entity
---

# Notat

notater til brug for kommunens forvaltning

### Semantic Template
```python
p.io.declare_input(
    output_name="notat",
    attributes={
        "notatlinie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "tekstfelt, der kan benyttes til fritekst i forbindelse med folkeregisternotater"
        },
        "notatnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "angiver en notatlinies nummer, idet en person kan have flere notatlinier"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for indsættelse af notat"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "angiver slutdato for notatet CPR"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for notat"
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