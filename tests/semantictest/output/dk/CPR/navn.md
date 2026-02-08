---
title: Navn
draft: false
type: entity
---

# Navn

Informationer om en persons navne - fornavne, mellemnavne, efternavn og slægtsnavn. Herudover adresseringsnavn, som kun registreres på den nuværende forekomst. Navn er null for nyfødte.

### Semantic Template
```python
p.io.declare_input(
    output_name="navn",
    attributes={
        "adresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Adresseringsnavn er på formen fornavne (inkl. evt. mellemnavn), efternavn. Adresseringsnavn kan anvendes af offentlige myndigheder til forsendelse, og det vil normalt være det navn, som fremgår af sundhedskortet, dog hvor efternavn skrives sidst og uden brug af komma separation. Om adresseringsnavn gælder i øvrigt at Hvis en persons navn i CPR efter stk. 1 og 2 er for langt til brug ved maskinel udskrivning (adressering), sørger Økonomi- og Indenrigsministeriet for, at der i CPR dannes et adresseringsnavn for vedkommende. Dette navn skal, hvis det er teknisk muligt, indeholde hele efternavnet og mindst ét helt fornavn registreret efter stk. 1.Forkortelser efter foretages ved, at fornavn eller mellemnavn i nødvendigt omfang forkortes til 1. bogstav. Eventuelle forkortelser foretages i sidste fornavn eller mellemnavn før efternavnet, dernæst i næstsidste og så fremdeles. Hvis første bogstav i første fornavn sammen med efternavnet overstiger det teknisk mulige for adressering, foretages forkortelserne tillige i efternavnet.Er den maskinelle forkortelse utilfredsstillende, registreres det bedst mulige adresseringsnavn, der så vidt muligt altid skal indeholde personens efternavn og mindst ét fornavn skrevet fuldt ud.Enhver har ret til ved henvendelse i sin bopælskommune at få registreret et adresseringsnavn på grundlag af det fulde navn, herunder at få ændret et adresseringsnavn. Adresseringsnavnet skal altid indeholde vedkommendes efternavn og mindst ét af vedkommendes fornavne skrevet fuldt ud."
        },
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "datafordelerregisterimportsequencenumber": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "datafordelerrowid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "datafordelerrowversion": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "efternavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Personens efternavn."
        },
        "efternavnmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "fornavne": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Persons fornavne."
        },
        "fornavnemarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "mellemnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Personens mellemnavne."
        },
        "mellemnavnmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "navnesoegning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "personid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.status, str),
            "description": "Angiver status på navnet."
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
    }
)
```
