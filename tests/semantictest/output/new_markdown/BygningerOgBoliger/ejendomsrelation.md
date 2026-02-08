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
            "cardinality": "0..1",
            "description": "angiver den fælles ejendomsidentifikation for den bestemte faste ejendom som den tilhørende BBR-entitet udgør eller indgår i"
        },
        "ejendommensejerforholdskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Ejerforholdskode, str),
            "cardinality": "0..1",
            "description": "ejerforholdskode for hovedejeren for den ejendom som denne ejendomsrelation refrerer til, baseret på Ejerfortegnelsens oplysninger om ejendommens ejerskaber"
        },
        "ejendomsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "0..1",
            "description": "ejendomsnummer for den ESR-ejendom som denne ejendomsrelation indgår i"
        },
        "vurderingsejendomsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "0..1",
            "description": "angiver SKAT's vurderingsejendomsnummer som denne Ejendomsrelation indgår i"
        },
        "ejerlejlighedsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver Matriklens ejerlejlighedsnummer når Ejendomsrelation er af typen ejerlejlighed"
        },
        "ejendomstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Ejendomstype, str),
            "cardinality": "1..1",
            "description": "afledt attribut som angiver ejendomstypen, dvs. om ejendommen udgør en samlet fast ejendom (dvs. et matrikuleret areal), en bygning på fremmed grund eller en ejerlejlighed"
        },
        "tinglystareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver ESR's oplysning om det samlede tinglyste areal af en ejerlejlighed som indgår i en enhed eller bygning"
        },
        "bygningpafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.BygningPåFremmedGrund, str),
            "cardinality": "0..1",
            "description": ""
        },
        "ejerlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Ejerlejlighed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "samletfastejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.SamletFastEjendom, str),
            "cardinality": "0..1",
            "description": ""
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningshændelse, str),
            "cardinality": "1..1",
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningsområde, str),
            "cardinality": "1..1",
            "description": "FORM-kode for det offentlige forretningsområde som har opdateret bygværkselementet til den pågældende version"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Livscyklus, str),
            "cardinality": "1..1",
            "description": "kode for bygværkselementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningsproces, str),
            "cardinality": "1..1",
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik og uforanderlig identifikation af bygværkselementet igennem hele dets livscyklus"
        },
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Kommunekode, str),
            "cardinality": "1..1",
            "description": "kode der identificerer den kommune som bygværkselementet hører til"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen af den pågældende version af bygværkselementet er foretaget"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kode som angiver hvilken aktør der har foretaget registreringen af den pågældende version af bygværkselementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor næste version af bygværkselementet registreres, og hvor denne version således ikke længere er den seneste"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet er startet"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Virkningsaktør, str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af bygværkselementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet ophører"
        }
    }
)
```