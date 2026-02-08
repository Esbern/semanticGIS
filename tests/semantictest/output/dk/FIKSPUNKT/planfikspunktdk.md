---
title: PlanfikspunktDK
draft: false
type: entity
---

# PlanfikspunktDK

fast punkt som definerer referencenettet i planet, beliggende i Danmark

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktdk",
    attributes={
        "afmaerkningsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "afmærkningstekst med fysisk udformning og placering i forhold til omgivelserne"
        },
        "artskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.planartskodeværdi, str),
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
        "dk10kmnet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angivelse om det plane fikspunkt hørere til 10 km nettet"
        },
        "easting": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.real, float),
            "description": "eastingkoordinat på den anvendte ellipsoide"
        },
        "ellipsoidehoejde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.real, float),
            "description": "højde over den anvendte ellipsoiden"
        },
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "fikspunktsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.uri, str),
            "description": "valdemar fikspunktsbeskrivelse"
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
        "gpsegnet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.gpsegnetværdi, str),
            "description": "anvendelighed for GPS-måling"
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
        "klasse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.klasseværdi, str),
            "description": "klasse er et kvalitetsudtryk for koordinaten"
        },
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den 4-cifrede CPR-kode der entydigt angiver en kommune"
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
        "refdk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angivelse om det plane fikspunkt hørere til RefDK nettet"
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
