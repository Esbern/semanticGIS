---
title: Navn
draft: false
type: entity
---

# Navn

informationer om en persons navne - fornavne, mellemnavne, efternavn og slægtsnavn. Herudover adresseringsnavn, som kun registreres på den nuværende forekomst. Navn er null for nyfødte

### Semantic Template
```python
p.io.declare_input(
    output_name="navn",
    attributes={
        "adresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "adresseringsnavn er på formen fornavne (inkl. evt. mellemnavn), efternavn. Adresseringsnavn kan anvendes af offentlige myndigheder til forsendelse, og det vil normalt være det navn, som fremgår af sundhedskortet, dog hvor efternavn skrives sidst og uden brug af komma separation. Om adresseringsnavn gælder i øvrigt at hvis en persons navn i CPR efter stk. 1 og 2 er for langt til brug ved maskinel udskrivning (adressering), sørger Økonomi- og Indenrigsministeriet for, at der i CPR dannes et adresseringsnavn for vedkommende. Dette navn skal, hvis det er teknisk muligt, indeholde hele efternavnet og mindst ét helt fornavn registreret efter stk. 1. Forkortelser efter foretages ved, at fornavn eller mellemnavn i nødvendigt omfang forkortes til 1. bogstav. Eventuelle forkortelser foretages i sidste fornavn eller mellemnavn før efternavnet, dernæst i næstsidste og så fremdeles. Hvis første bogstav i første fornavn sammen med efternavnet overstiger det teknisk mulige for adressering, foretages forkortelserne tillige i efternavnet. Er den maskinelle forkortelse utilfredsstillende, registreres det bedst mulige adresseringsnavn, der så vidt muligt altid skal indeholde personens efternavn og mindst ét fornavn skrevet fuldt ud. Enhver har ret til ved henvendelse i sin bopælskommune at få registreret et adresseringsnavn på grundlag af det fulde navn, herunder at få ændret et adresseringsnavn. Adresseringsnavnet skal altid indeholde vedkommendes efternavn og mindst ét af vedkommendes fornavne skrevet fuldt ud"
        },
        "efternavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "personens efternavn"
        },
        "fornavne": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "persons fornavne"
        },
        "mellemnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "personens mellemnavne"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "gyldighedsstartdato for navneoplysningen"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "om gyldighedsstartdatoen er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "slutdato for angivelse af navne. Feltet knytter sig kun til felterne efternavn, mellemnavn og fornavn"
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
            "description": "angiver status på navnet"
        },
        "fornavnsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Navnemarkering, str),
            "cardinality": "0..1",
            "description": "angiver navnemarkering for fornavne"
        },
        "mellemnavnsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Navnemarkering, str),
            "cardinality": "0..1",
            "description": "angiver navnemarkering for mellemnavn"
        },
        "efternavnsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Navnemarkering, str),
            "cardinality": "0..1",
            "description": "angiver navnemarkering for efternavn"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        }
    }
)
```