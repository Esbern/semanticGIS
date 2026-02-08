---
title: PlanfikspunktFærøerne
draft: false
type: entity
---

# PlanfikspunktFærøerne

fast punkt som definerer referencenettet i planet, beliggende i Færøerne

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktfærøerne",
    attributes={
        "herredsogn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angivelse af hvilket herred, sogn og købstad et fikspunkt tilhører"
        },
        "lbenummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "er sidste del af fikspunktsnummer uden opmålingsdistriktet"
        },
        "northing": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "northingkoordinat på den anvendte ellipsoide"
        },
        "easting": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "eastingkoordinat på den anvendte ellipsoide"
        },
        "ellipsoidehjde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "højde over den anvendte ellipsoiden"
        },
        "fo10kmnet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "REFFO er det grundlæggende GPS-baserede referencenet på Færøerne"
        },
        "fikspunktsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "unikt nummer for et fikspunkt"
        },
        "specialnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..*",
            "description": "et alternativt fikspunktnummer oprindeligt defineret af anden bruger"
        },
        "kote": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "højde over den anvendte geoide nulreferenceflade"
        },
        "artskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.PlanArtskodeVærdi, str),
            "cardinality": "1..1",
            "description": "klassifikation af et punkt inddelt efter afmærkningstype, opmålings- og beregningsmetode"
        },
        "kotereferenceversion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.KotereferenceversionVærdi, str),
            "cardinality": "1..1",
            "description": "kote system hvori koten er beregnet"
        },
        "mvstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.MvStatusVærdi, str),
            "cardinality": "1..1",
            "description": "en overordnet inddeling af fikspunkter ud fra anvendelsesformål"
        },
        "middelfejl": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "udtryk for middelfejlen på den enkelte koordinat/kote ud fra beregning af observationerne til punktet"
        },
        "malemetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.MålemetodeVærdi, str),
            "cardinality": "1..1",
            "description": "metode hvorved et fikspunkt er opmålt"
        },
        "plandescriptor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.PlandescriptorVærdi, str),
            "cardinality": "0..3",
            "description": "afmærkningstype (afmærkningsform) og fysisk status"
        },
        "punktdescriptor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.PunktdescriptorVærdi, str),
            "cardinality": "0..3",
            "description": "afmærkningstype (afmærkningsform) og fysisk tilstand og status"
        },
        "gpsegnet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.GPSEgnetVærdi, str),
            "cardinality": "1..1",
            "description": "anvendelighed for GPS-måling"
        },
        "fikspunktsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "valdemar fikspunktsbeskrivelse"
        },
        "afmrkningsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "afmærkningstekst med fysisk udformning og placering i forhold til omgivelserne"
        },
        "tekstbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "tekst der indeholder en detaljeret beskrivelse om fikspunktets placering"
        },
        "malskitse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "en grafisk skitse over punktets placering med mål til nærmeste genstande. Skitsen er ikke målfast"
        },
        "foto": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..*",
            "description": "fotografi af punktet, dele af punktet og/eller dets omgivelser"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "opbygning af punkter og/eller linjer og/eller flader der tilsammen udgør en geografisk udstrækning"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
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
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.FikspunktForretningshændelseVærdi, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
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
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.FikspunktForretningsområdeVærdi, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.FikspunktStatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.FikspunktForretningsprocesVærdi, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        }
    }
)
```