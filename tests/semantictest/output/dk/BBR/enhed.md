---
title: Enhed
draft: false
type: entity
---

# Enhed

en enhed er et sammenhængende areal i en bygning, der er fysisk adskilt fra andre enheder. En enhed skal have mindst én selvstændig adgang fra en opgang/indgang og udgøre en brugsmæssig helhed

### Semantic Template
```python
p.io.declare_input(
    output_name="enhed",
    attributes={
        "adresseidentificerer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "bygning": {
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
        "enh008uuidtilmoderlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.bbr.enhed, str),
            "description": "angiver henvisning fra supplementsrum til moderlejlighed"
        },
        "enh020enhedensanvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.enhedsanvendelse, str),
            "description": "angiver kode for enhedens anvendelse"
        },
        "enh023boligtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.boligtype, str),
            "description": "angiver kode for boligtype"
        },
        "enh024kondemneretboligenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kondemneretboligenhed, str),
            "description": "angiver kode for kondemneret boligenhed"
        },
        "enh025oprettelsesdatoforenhedensidentifikation": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver oprettelsesdato for enheden"
        },
        "enh026enhedenssamledeareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens samlede areal"
        },
        "enh027arealtilbeboelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens areal til beboelse"
        },
        "enh028arealtilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens areal til erhverv"
        },
        "enh030kildetilenhedensarealer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kildetiloplysninger, str),
            "description": "angiver kode for kilde til oplysninger om areal"
        },
        "enh031antalvaerelser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal værelser i enheden"
        },
        "enh032toiletforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.toiletforhold, str),
            "description": "angiver kode for enhedens toiletforhold"
        },
        "enh033badeforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.badeforhold, str),
            "description": "angiver kode for enhedens badeforhold"
        },
        "enh034koekkenforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.køkkenforhold, str),
            "description": "angiver kode for enhedens køkkenforhold"
        },
        "enh035energiforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.energiforsyning, str),
            "description": "angiver kode for enhedens energiforsyning"
        },
        "enh039andetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens andet areal"
        },
        "enh041lovliganvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.lovliganvendelse, str),
            "description": "angiver eventuel dispensation til anvendelse af enheden"
        },
        "enh042datofortidsbegraensetdispensation": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for tidsbegrænset dispensation"
        },
        "enh044datofordelvisibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for delvis ibrugtagningstilladelse"
        },
        "enh045udlejningsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.udlejningsforhold, str),
            "description": "angiver enhedens udlejningsforhold"
        },
        "enh046offentligstoette": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.offentligstøtte, str),
            "description": "angiver offentlig støtte"
        },
        "enh047indflytningdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for indflytning"
        },
        "enh048godkendttombolig": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.godkendttomboligændretadministrativpraksis, str),
            "description": "angiver om boligen er godkendt som tom bolig"
        },
        "enh051varmeinstallation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.varmeinstallation, str),
            "description": "angiver enhedens varmeinstallation"
        },
        "enh052opvarmningsmiddel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.opvarmningsmiddel, str),
            "description": "angiver enhedens opvarmningsmiddel"
        },
        "enh053supplerendevarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.supplerendevarme, str),
            "description": "angiver enhedens supplerende varme"
        },
        "enh060enhedensandelfaellesadgangsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens andel i fælles adgangsareal"
        },
        "enh061arealafaabenoverdaekning": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens areal af åben overdækning"
        },
        "enh062arealaflukketoverdaekningudestue": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens areal af lukket overdækning"
        },
        "enh063antalvaerelsertilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal værelser i enheden der anvendes til erhverv"
        },
        "enh065antalvandskylledetoiletter": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal vandskyllende toiletter"
        },
        "enh066antalbadevaerelser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal badeværelser"
        },
        "enh067stoejisolering": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver årstal for støjisolering"
        },
        "enh068flexboligtilladelsesart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tilladelsesart, str),
            "description": "angivelse af om en tilladelse til flexbolig er personlig eller ej og om den er med eller uden tidsbegrænsning"
        },
        "enh069flexboligophoersdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "​dato for ophør af en tidsbegrænset flexboligtilladelse"
        },
        "enh070aabenaltantagterrasseareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "samlet areal af åben altan og/eller åben tagterrasse"
        },
        "enh071adressefunktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.adresserolle, str),
            "description": "angiver adressens funktion i forhold til denne enhed"
        },
        "enh101gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver gyldighedsdato for enheden"
        },
        "enh102herafareal1": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh105"
        },
        "enh103herafareal2": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh106"
        },
        "enh104herafareal3": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh107"
        },
        "enh105supplerendeanvendelseskode1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.enhedsanvendelse, str),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh102"
        },
        "enh106supplerendeanvendelseskode2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.enhedsanvendelse, str),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh103"
        },
        "enh107supplerendeanvendelseskode3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.enhedsanvendelse, str),
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh104"
        },
        "enh127fysiskarealtilbeboelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens fysiske areal til beboelse"
        },
        "enh128fysiskarealtilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver enhedens fysiske areal til erhverv"
        },
        "enh500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "etage": {
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
        "opgang": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
