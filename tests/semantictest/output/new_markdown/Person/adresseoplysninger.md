---
title: Adresseoplysninger
draft: false
type: entity
---

# Adresseoplysninger

oplysninger om personers adresser, Kommune, vej, husnummer, etage, side-dørnummer, bygningsnummer, c/o-navn, lokalitet, bynavn, postnummer og postdistrikt

### Semantic Template
```python
p.io.declare_input(
    output_name="adresseoplysninger",
    attributes={
        "fraflytningsdatokommune": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for fraflytning fra tidligere bopælskommune. (når personen er flyttet mellem 2 kommuner)"
        },
        "fraflytningsdatokommuneusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at fraflytningsdato fra tidligere bopælskommune er usikker"
        },
        "conavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "C/O navn i adressen. Konstanten C/O samt en blank vil være indeholdt i de første 4 positioner"
        },
        "tilflytningsdatokommune": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for tilflytning til nuværende kommune, hvis Personen er flyttet mellem 2 kommuner"
        },
        "tilflytningsdatokommuneusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at tilflytningsdato til nuværende kommune er usikker"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "bopælsregistreringens gyldighedsstartdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "om gyldighedsstartdato er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "bopælsregistreringens gyldighedsslutdato"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at virkningTil er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver status for adresseoplysning"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        },
        "adresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.CprAdresse, str),
            "cardinality": "1..1",
            "description": ""
        },
        "supplerendeadresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.SimpelAdresseoplysning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "fraflytningskommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "0..1",
            "description": ""
        }
    }
)
```