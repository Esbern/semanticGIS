---
title: UbearbejdetNavnLinje
draft: false
type: entity
---

# UbearbejdetNavnLinje

linjeobjekt indberettet via den fælles indberetningsportal for Stednavne

### Semantic Template
```python
p.io.declare_input(
    output_name="ubearbejdetnavnlinje",
    attributes={
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "opbygning af punkter og/eller linjer og/eller flader, der tilsammen udgør en geografisk udstrækning"
        },
        "ubearbejdetnavntype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Stednavne.UbearbejdetNavnetype, str),
            "cardinality": "1..1",
            "description": "underinddeling af UbearbejdetNavn på baggrund af indberettet objekttype"
        },
        "bruger": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "identifikation af individ, der har oprettet/ændret objektet"
        },
        "maskine": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "identifikation af maskine, der har oprettet/ændret objektet"
        },
        "program": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "identifikation af program benyttet til at oprette/ændre objektet"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Stednavne.StednavneForretningshændelsestype, str),
            "cardinality": "1..1",
            "description": "den begivenhed i 'virkeligheden' som udløser en ændring i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Stednavne.StednavneForretningsprocestype, str),
            "cardinality": "1..1",
            "description": "den manuelle eller it-understøttede proces, hvori forretningsområdet håndterer hændelsen"
        },
        "id": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "globalt unik identifikation, som ikke ændres i data-objektets levetid"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..*",
            "description": "datatype, der indeholder attributterne for et Stednavn tilknyttet et specifikt NavngivetSted"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet, hvor registreringen er foretaget"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet, hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør, der har foretaget en registrering"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Stednavne.NavngivetStedStatustype, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        }
    }
)
```