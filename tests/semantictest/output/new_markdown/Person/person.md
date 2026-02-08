---
title: Person
draft: false
type: entity
---

# Person

person der er registreret i CPR med personnummer

### Semantic Template
```python
p.io.declare_input(
    output_name="person",
    attributes={
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "dato for startoplysninger"
        },
        "statusdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "hændelsesdato for angivelse af status. Eksisterer kun i forbindelse med en inaktiv status"
        },
        "statusdatousikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at statusdato er usikker"
        },
        "stilling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "stilling ift. beskæftigelse i klarskrift"
        },
        "supplerendefoedselsregistreringssted": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "alternativt fritekstfelt til angivelse af fødselsregistreringssted (tekstfelt uden kode)"
        },
        "foedselsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "fødselsdato på personen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Personstatus, str),
            "cardinality": "1..1",
            "description": "angiver status for personen"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        },
        "foedselsdatousikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at fødselsdato er usikker"
        },
        "koen": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Koen, str),
            "cardinality": "1..1",
            "description": "angiver kønnet på personen"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at virkningFra er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "angiver slutdato"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at virkningTil er usikker"
        },
        "deltbopael": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.DeltBopael, str),
            "cardinality": "0..1",
            "description": ""
        },
        "foraeldremyndighedsoplysning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Foraeldremyndighedsoplysning, str),
            "cardinality": "0..2",
            "description": ""
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Navn, str),
            "cardinality": "0..*",
            "description": ""
        },
        "valgoplysninger": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Valgoplysninger, str),
            "cardinality": "0..*",
            "description": ""
        },
        "cprhaendelseskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.CprHaendelseskode, str),
            "cardinality": "0..*",
            "description": ""
        },
        "foraelderoplysning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Foraelderoplysning, str),
            "cardinality": "0..2",
            "description": ""
        },
        "folkekirke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Folkekirke, str),
            "cardinality": "1..*",
            "description": ""
        },
        "kontaktadresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.SimpelAdresseoplysning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "civilstand": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Civilstand, str),
            "cardinality": "1..*",
            "description": ""
        },
        "adresseoplysninger": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Adresseoplysninger, str),
            "cardinality": "1..*",
            "description": ""
        },
        "cprfoedselsregistreringssted": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "1..1",
            "description": ""
        },
        "notat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Notat, str),
            "cardinality": "0..*",
            "description": ""
        },
        "forsvinding": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Forsvinding, str),
            "cardinality": "0..*",
            "description": ""
        },
        "udrejseindrejse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.UdrejseIndrejse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "cprhaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Cprhaendelse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "statsborgerskab": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Statsborgerskab, str),
            "cardinality": "1..*",
            "description": ""
        },
        "personnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Personnummer, str),
            "cardinality": "1..*",
            "description": ""
        },
        "flyttepaabud": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Flyttepaabud, str),
            "cardinality": "0..1",
            "description": ""
        },
        "beskyttelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Beskyttelse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "vaergemaal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Vaergemaal, str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommunaleforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.KommunaleForhold, str),
            "cardinality": "0..*",
            "description": ""
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