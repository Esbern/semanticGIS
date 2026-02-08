---
title: HoejdefikspunktFO
draft: false
type: entity
---

# HoejdefikspunktFO

fast punkt som definerer referencenettet i højden i Færøerne

### Semantic Template
```python
p.io.declare_input(
    output_name="hoejdefikspunktfo",
    attributes={
        "afmaerkningsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "afmærkningstekst med fysisk udformning og placering i forhold til omgivelserne"
        },
        "artskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.højdeartskodeværdi, str),
            "description": "klassifikation af et punkt inddelt efter afmærkningstype, opmålings- og beregningsmetode"
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
        "easting": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.real, float),
            "description": "eastingkoordinat på den anvendte ellipsoide"
        },
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "fikspunktsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.uri, str),
            "description": "samlet beskrivelse af et fikspunkt indeholdende en afmærkningsbeskrivelse, tekstbeskrivelse og målskitse. Der vil også være kortudsnit med placering og nabopunkter"
        },
        "fikspunktsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "unikt nummer for et fikspunkt"
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.fikspunktforretningshændelseværdi, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.fikspunktforretningsområdeværdi, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.fikspunktforretningsprocesværdi, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.gm_point, str),
            "description": "opbygning af punkter og/eller linjer og/eller flader der tilsammen udgør en geografisk udstrækning"
        },
        "gmlid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "herredsogn_herredsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "herredsogn_koebstadnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "herredsogn_sognenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "description": ""
        },
        "id_namespace": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "kote": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.real, float),
            "description": "højde over den anvendte geoide nulreferenceflade"
        },
        "kotereferenceversion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.kotereferenceversionværdi, str),
            "description": "kote system hvori koten er beregnet"
        },
        "loebenummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "er sidste del af fikspunktsnummer uden opmålingsdistriktet"
        },
        "maaleaar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.årstal, str),
            "description": "sidste år der er målt til punktet"
        },
        "maalemetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.målemetodeværdi, str),
            "description": "metode hvorved et fikspunkt er opmålt"
        },
        "maalskitse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.uri, str),
            "description": "en grafisk skitse over punktets placering med mål til nærmeste genstande. Skitsen er ikke målfast"
        },
        "middelfejl": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "udtryk for middelfejlen på den enkelte koordinat/kote ud fra beregning af observationerne til punktet"
        },
        "mvstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.mvstatusværdi, str),
            "description": "en overordnet inddeling af fikspunkter ud fra anvendelsesformål"
        },
        "northing": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.real, float),
            "description": "northingkoordinat på den anvendte ellipsoide"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.fikspunktstatusværdi, str),
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        },
        "tekstbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "tekst der indeholder en detaljeret beskrivelse om fikspunktets placering"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor objektets virkning ophører"
        },
    }
)
```
