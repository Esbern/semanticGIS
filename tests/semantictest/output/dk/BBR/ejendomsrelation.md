---
title: Ejendomsrelation
draft: false
type: entity
---

# Ejendomsrelation

ejendomsrelation samler oplysningerne om de fysiske BBR-entiteters relation til den ejendom de udgør eller indgår i

### Semantic Template
```python
p.io.declare_input(
    output_name="ejendomsrelation",
    attributes={
        "bfenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver den fælles ejendomsidentifikation for den bestemte faste ejendom som den tilhørende BBR-entitet udgør eller indgår i"
        },
        "bygningpaafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "ejendommensejerforholdskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.ejerforholdskode, str),
            "description": "ejerforholdskode for hovedejeren for den ejendom som denne ejendomsrelation refrerer til, baseret på Ejerfortegnelsens oplysninger om ejendommens ejerskaber"
        },
        "ejendomsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "ejendomsnummer for den ESR-ejendom som denne ejendomsrelation indgår i"
        },
        "ejendomstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.ejendomstype, str),
            "description": "afledt attribut som angiver ejendomstypen, dvs. om ejendommen udgør en samlet fast ejendom (dvs. et matrikuleret areal), en bygning på fremmed grund eller en ejerlejlighed"
        },
        "ejerlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "ejerlejlighedsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver Matriklens ejerlejlighedsnummer når Ejendomsrelation er af typen ejerlejlighed"
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningshændelse, str),
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningsområde, str),
            "description": "FORM-kode for det offentlige forretningsområde som har opdateret bygværkselementet til den pågældende version"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningsproces, str),
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
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
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kommunekode, str),
            "description": "kode der identificerer den kommune som bygværkselementet hører til"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen af den pågældende version af bygværkselementet er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kode som angiver hvilken aktør der har foretaget registreringen af den pågældende version af bygværkselementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor næste version af bygværkselementet registreres, og hvor denne version således ikke længere er den seneste"
        },
        "samletfastejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.livscyklus, str),
            "description": "kode for bygværkselementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "tinglystareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver ESR's oplysning om det samlede tinglyste areal af en ejerlejlighed som indgår i en enhed eller bygning"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet er startet"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.virkningsaktør, str),
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af bygværkselementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet ophører"
        },
        "vurderingsejendomsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver SKAT's vurderingsejendomsnummer som denne Ejendomsrelation indgår i"
        },
    }
)
```
