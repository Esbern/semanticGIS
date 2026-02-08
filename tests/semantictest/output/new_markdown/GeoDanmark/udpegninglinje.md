---
title: UdpegningLinje
draft: false
type: entity
---

# UdpegningLinje

linje til udpegning af områder der skal ajourføres

### Semantic Template
```python
p.io.declare_input(
    output_name="udpegninglinje",
    attributes={
        "ar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "årstal for forventet synlighed i et luftfoto fotograferet i marts-april måned det pågældende år"
        },
        "nummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "fortløbende nummer"
        },
        "kilde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "hvem indberettede denne hændelse ?. Kommunenummer eller SDFE"
        },
        "aktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.AktionVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvilken handling, der forventes udført på det udpegede sted"
        },
        "objtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "navnet på den objekttype, der skal behandles"
        },
        "foretaget": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.ForetagetVærdi, str),
            "cardinality": "1..1",
            "description": "er der foretaget en ajourføring dette sted?"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "objektets geografiske placering"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
        },
        "tempid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "midlertidig nøgle til kobling af GeoDanmarkobjekter med eksterne databaser"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.GeoDanmarkStatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et GeoDanmarkobjekt er i sin livscyklus"
        },
        "geometristatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.GeometristatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af status for registrering af geometri"
        },
        "registreringsspecifikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.RegistreringsspecifikationVærdi, str),
            "cardinality": "1..1",
            "description": "navnet på den specifikation objektet er registreret under eller er opgraderet til. 'GeoDanmark Spec 6.0'"
        },
        "dataansvar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "navnet på den myndighed, der har dataansvaret for objektet"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.GeoDanmarkForretningshændelseVærdi, str),
            "cardinality": "1..1",
            "description": "den forretningshændelse, som afstedkom opdateringen"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "fORM-kode for det offentlige forretningsområde som har opdateret dataobjektet"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.GeoDanmarkForretningsprocesVærdi, str),
            "cardinality": "0..1",
            "description": "den forretningsproces som har opdateret dataobjektet"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der sidst har registreret noget på objektet, så objektet fik ny ident"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato og tid for databasesystemets tildeling af en ny ident til objektet og for alle efterfølgende ændringer af enhver art på objektet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet for objektets 'ændring' eller 'sletning' i databasen. Ved 'ændring' forstås ændring af enhver art, hvor den hidtidige version af objektet gøres historisk og en ny version, bliver den aktuelle"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der sidst har udført ændringer af enhver art på objektet"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra objektet har virkning. For fotogrammetri: fotodatoen. Ellers kan datoen dateres til fortiden, nutiden eller fremtiden"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet for objektets 'ændring' eller 'sletning' i databasen. Ved 'ændring' forstås ændring af enhver art, hvor den hidtidige version af objektet gøres historisk og en ny version, bliver den aktuelle"
        },
        "plannjagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.NøjagtighedVærdi, str),
            "cardinality": "1..1",
            "description": "den forventede middelfejl på nøjagtigheden af den registrerede XY-koordinat i forhold til dets placering i virkeligheden. 'Ukendt nøjagtighed' angives med en nøjagtighed på '10.00'"
        },
        "planstedfstelsesmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.StedfæstelsesmetodeVærdi, str),
            "cardinality": "1..1",
            "description": "metode til stedfæstelse af objektets koordinater i XY"
        },
        "vertikalnjagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.NøjagtighedVærdi, str),
            "cardinality": "1..1",
            "description": "den forventede middelfejl på nøjagtigheden af den registrerede Z-koordinat i forhold til dets placering i virkeligheden. 'Ukendt nøjagtighed' angives med en nøjagtighed på '10.00'"
        },
        "vertikalstedfstelsesmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.GeoDanmark.StedfæstelsesmetodeVærdi, str),
            "cardinality": "1..1",
            "description": "metode til stedfæstelse af objektets Z-.koordinater"
        },
        "applikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "et frit tekstfelt, der angiver den applikation og version, der har indleveret data til databasen"
        },
        "kommentar": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "et frit tekstfelt, der kan indeholde en valgfri kommentar/beskrivelse af objektets forhold"
        }
    }
)
```