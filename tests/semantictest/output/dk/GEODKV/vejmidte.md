---
title: Vejmidte
draft: false
type: entity
---

# Vejmidte

midte af et færdselsareal benyttet til motoriseret, gående, cyklende eller ridende færdsel

### Semantic Template
```python
p.io.declare_input(
    output_name="vejmidte",
    attributes={
        "applikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "et frit tekstfelt, der angiver den applikation og version, der har indleveret data til databasen"
        },
        "cvfadmnr": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "alle objekter repræsenterende en vej eller sti, som findes i Vejdirektoratets ”Centrale Vej- og Stifortegnelse”, kan tildeles en kode i overensstemmelse med registret"
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
            "role": sg.LOOKUP(dk.geodkv.lookups.gm_curve, str),
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
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "alle objekter tildeles en værdi. Værdien svarer normalt til nummeret på den kommune, hvori de ligger"
        },
        "niveau": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.niveauværdi, str),
            "description": "angiver om vejmidten befinder sig på en bro eller i en tunnel"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "overflade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.overfladeværdi, str),
            "description": "angiver vejmidtens overfladebelægning"
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
        "rundkoersel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver om vejmidte er en rundkørsel"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.geodanmarkstatusværdi, str),
            "description": "angivelse af hvor et GeoDanmarkobjekt er i sin livscyklus"
        },
        "tempid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "midlertidig nøgle til kobling af GeoDanmarkobjekter med eksterne databaser"
        },
        "tilogfrakoersel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver om vejmidte er en ensrettet til- eller frakørsel til en større vej"
        },
        "trafikart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.trafikartværdi, str),
            "description": "værdien af Trafikart tildeles i overensstemmelse med de begrænsninger i færdselsarter, som er indført i henhold til færdselsloven"
        },
        "vejkategori": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.vejkategoriværdi, str),
            "description": "kategorisering af vejen"
        },
        "vejkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "i overensstemmelse med DAR (danmarksadresser.dk)"
        },
        "vejmidtetype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.geodkv.lookups.vejmidtetypeværdi, str),
            "description": "angiver typen af vejmidten"
        },
        "vejmyndighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "navnet på den ansvarlige myndighed i henhold til ”Lov om offentlige veje” eller ”Lov om private fællesveje”"
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
