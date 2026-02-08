---
title: FordelingAfFordelingsareal
draft: false
type: entity
---

# FordelingAfFordelingsareal

angiver hvordan et fordelingsareal fordeles ud på hver af de enheder som indgår i fordelingen, herunder areal til bolig hhv. til erhverv

### Semantic Template
```python
p.io.declare_input(
    output_name="fordelingaffordelingsareal",
    attributes={
        "beboelsesarealfordelttilenhed": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "den del af et fordelingsareal som tillægges enhedens beboelsesareal"
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
        "enhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "erhvervsarealfordelttilenhed": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "den del af et fordelingsareal som tillægges enhedens erhvervsareal"
        },
        "fordelingsareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.livscyklus, str),
            "description": "kode for bygværkselementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
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
    }
)
```
