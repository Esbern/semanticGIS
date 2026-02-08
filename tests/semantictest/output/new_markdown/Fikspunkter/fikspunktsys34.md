---
title: FikspunktSys34
draft: false
type: entity
---

# FikspunktSys34

fast punkt som definerer referencenettet i planet efter system 34 koordinatsystemet

### Semantic Template
```python
p.io.declare_input(
    output_name="fikspunktsys34",
    attributes={
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
        "y": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "y koordinat i System 34"
        },
        "x": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "x koordinat i System 34"
        },
        "system34version": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.System34VersionVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af System34 version punktet er placeret i"
        },
        "fikspunktsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "samlet beskrivelse af et fikspunkt indeholdende en afmærkningsbeskrivelse, tekstbeskrivelse og målskitse. Der vil også være kortudsnit med placering og nabopunkter"
        },
        "artskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Fikspunkter.PlanArtskodeVærdi, str),
            "cardinality": "1..1",
            "description": "klassifikation af et punkt inddelt efter afmærkningstype, opmålings- og beregningsmetode"
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
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "den 4-cifrede CPR-kode der entydigt angiver en kommune"
        },
        "malskitse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "en grafisk skitse over punktets placering med mål til nærmeste genstande. Skitsen er ikke målfast"
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