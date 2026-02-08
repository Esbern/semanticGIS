---
title: HistoriskLinje
draft: false
type: entity
---

# HistoriskLinje

generelt objekt til opbevaring af historiske linjeobjekter, der ikke ellers findes i den aktuelle version af specifikationen

### Semantic Template
```python
p.io.declare_input(
    output_name="historisklinje",
    attributes={
        "applikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "et frit tekstfelt, der angiver den applikation og version, der har indleveret data til databasen"
        },
        "att01": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att02": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att03": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att04": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att05": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att06": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att07": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att08": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att09": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att10": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att11": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att12": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att13": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att14": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att16": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att17": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att18": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att19": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "att20": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "generisk attribut"
        },
        "attributindex": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angivelse af, hvorledes attributterne i det aktuelle historiske objekt er opbevaret i de generiske attributter. Hvert index-par adskilles af et semikolon ; F.eks. 01:Bytype;02:Bebyggelseskode"
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
        "histid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "geoDanmark-identen, som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
        },
        "histobjekttype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "her gemmes det objekttypenavn, som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
        },
        "histregistreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "attributværdien som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
        },
        "histregistreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "attributværdien som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
        },
        "histvirkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "attributværdien som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
        },
        "histvirkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "attributværdien som objektet havde, umiddelbart inden at det blev overført til den historiske objekttype"
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
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "tempid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "midlertidig nøgle til kobling af GeoDanmarkobjekter med eksterne databaser"
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
