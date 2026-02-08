---
title: Opstillingskreds
draft: false
type: entity
---

# Opstillingskreds

geografisk inddeling af landet i kredse, hvorfra kandidater opstilles og vælges til Folketinget

## Sources

- Opstillingskreds (aggregate)
- Opstillingskreds_250000 (1:250000)
- Opstillingskreds_500000 (1:500000)
- Opstillingskreds_2000000 (1:2000000)

### Semantic Template
```python
p.io.declare_input(
    output_name="opstillingskreds",
    attributes={
        "opstillingskredsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "opstillingskredsens nummer jf. lovbekendtgørelse. To-cifret, unikt nummer i storkredsen (1-92)"
        },
        "valgkredsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "valgkredsnummer jf. lovbekendgørelse. To-cifret, unikt nummer i storkredsen"
        },
        "kredskommunenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "navnet på den kommune, som er formand for den fælles valgbestyrelse i opstillingskredsen jf. lovbekendtgørelse"
        },
        "kredskommunenummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kommunekoden for den kommune, som er formand for den fælles valgbestyrelse i opstillingskredsen jf. lovbekendtgørelse"
        },
        "storkreds": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DAGI.Storkreds, str),
            "cardinality": "1..1",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "navngivningen af DAGI objektet"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DAGI.Registreringsaktør, str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor objektets virkning ophører"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DAGI.Virkningsaktør, str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DAGI.Forretningshændelse, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DAGI.Forretningsproces, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "geografisk udstrækning for den administrative inddeling"
        }
    }
)
```