---
title: Bygning
draft: false
type: entity
---

# Bygning

repræsentation af et bygningsobjekts bebyggede og overdækkede areal

### Semantic Template
```python
p.io.declare_input(
    output_name="bygning",
    attributes={
        "applikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "et frit tekstfelt, der angiver den applikation og version, der har indleveret data til databasen"
        },
        "bbraktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.bbraktionværdi, str),
            "description": "dette er en hjælpeattribut i forbindelse med geokodning"
        },
        "bbruuid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "attribut afledt af relationen imellem GeoDanmark element og Bygværkselement i Bygninger og boliger"
        },
        "bygningstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.bygningstypeværdi, str),
            "description": "angiver type af bygning med én af de anførte værdier"
        },
        "dataansvar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "navnet på den myndighed, der har dataansvaret for objektet"
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
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.geodanmarkforretningshændelseværdi, str),
            "description": "den forretningshændelse, som afstedkom opdateringen"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "fORM-kode for det offentlige forretningsområde som har opdateret dataobjektet"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.geodanmarkforretningsprocesværdi, str),
            "description": "den forretningsproces som har opdateret dataobjektet"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.gm_surface, str),
            "description": "objektets geografiske placering"
        },
        "geometristatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.geometristatusværdi, str),
            "description": "angivelse af status for registrering af geometri"
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
        "kommentar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "et frit tekstfelt, der kan indeholde en valgfri kommentar/beskrivelse af objektets forhold"
        },
        "maalestedbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.målestedbygningværdi, str),
            "description": "angiver den metode, objektet er stedfæstet med"
        },
        "metode3d": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.metode3dværdi, str),
            "description": "angiver efter hvilken metode herunder specifikation z-koordinaten er registreret"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "overlapbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, om en BYGNING overlappes helt eller delvist af en anden BYGNING"
        },
        "plannoejagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.nøjagtighedværdi, str),
            "description": "den forventede middelfejl på nøjagtigheden af den registrerede XY-koordinat i forhold til dets placering i virkeligheden. 'Ukendt nøjagtighed' angives med en nøjagtighed på '10.00'"
        },
        "planstedfaestelsesmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.stedfæstelsesmetodeværdi, str),
            "description": "metode til stedfæstelse af objektets koordinater i XY"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato og tid for databasesystemets tildeling af en ny ident til objektet og for alle efterfølgende ændringer af enhver art på objektet"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der sidst har registreret noget på objektet, så objektet fik ny ident"
        },
        "registreringsspecifikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.registreringsspecifikationværdi, str),
            "description": "navnet på den specifikation objektet er registreret under eller er opgraderet til. 'GeoDanmark Spec 6.0'"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet for objektets 'ændring' eller 'sletning' i databasen. Ved 'ændring' forstås ændring af enhver art, hvor den hidtidige version af objektet gøres historisk og en ny version, bliver den aktuelle"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.geodanmarkstatusværdi, str),
            "description": "angivelse af hvor et GeoDanmarkobjekt er i sin livscyklus"
        },
        "synligbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, om en BYGNING er synlig i et ortofoto"
        },
        "tempid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "midlertidig nøgle til kobling af GeoDanmarkobjekter med eksterne databaser"
        },
        "underminimumbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angivelse af om arealet er mindre end den minimumstørrelse på en Bygning, som er defineret i GeoDanmark-Specifikationen"
        },
        "vertikalnoejagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.nøjagtighedværdi, str),
            "description": "den forventede middelfejl på nøjagtigheden af den registrerede Z-koordinat i forhold til dets placering i virkeligheden. 'Ukendt nøjagtighed' angives med en nøjagtighed på '10.00'"
        },
        "vertikalstedfaestelsesmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.stedfæstelsesmetodeværdi, str),
            "description": "metode til stedfæstelse af objektets Z-.koordinater"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra objektet har virkning. For fotogrammetri: fotodatoen. Ellers kan datoen dateres til fortiden, nutiden eller fremtiden"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der sidst har udført ændringer af enhver art på objektet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet for objektets 'ændring' eller 'sletning' i databasen. Ved 'ændring' forstås ændring af enhver art, hvor den hidtidige version af objektet gøres historisk og en ny version, bliver den aktuelle"
        },
    }
)
```
