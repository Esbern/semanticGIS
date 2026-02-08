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
        "enh008uuidtilmoderlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver henvisning fra supplementsrum til moderlejlighed"
        },
        "enh020enhedensanvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Enhedsanvendelse, str),
            "cardinality": "1..1",
            "description": "angiver kode for enhedens anvendelse"
        },
        "enh023boligtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Boligtype, str),
            "cardinality": "1..1",
            "description": "angiver kode for boligtype"
        },
        "enh024kondemneretboligenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KondemneretBoligenhed, str),
            "cardinality": "1..1",
            "description": "angiver kode for kondemneret boligenhed"
        },
        "enh025oprettelsesdatoforenhedensidentifikation": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver oprettelsesdato for enheden"
        },
        "enh026enhedenssamledeareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens samlede areal"
        },
        "enh027arealtilbeboelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens areal til beboelse"
        },
        "enh028arealtilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens areal til erhverv"
        },
        "enh030kildetilenhedensarealer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KildeTilOplysninger, str),
            "cardinality": "1..1",
            "description": "angiver kode for kilde til oplysninger om areal"
        },
        "enh031antalvrelser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal værelser i enheden"
        },
        "enh032toiletforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Toiletforhold, str),
            "cardinality": "1..1",
            "description": "angiver kode for enhedens toiletforhold"
        },
        "enh033badeforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Badeforhold, str),
            "cardinality": "1..1",
            "description": "angiver kode for enhedens badeforhold"
        },
        "enh034kkkenforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Køkkenforhold, str),
            "cardinality": "1..1",
            "description": "angiver kode for enhedens køkkenforhold"
        },
        "enh035energiforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Energiforsyning, str),
            "cardinality": "1..1",
            "description": "angiver kode for enhedens energiforsyning"
        },
        "enh039andetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens andet areal"
        },
        "enh041lovliganvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.LovligAnvendelse, str),
            "cardinality": "1..1",
            "description": "angiver eventuel dispensation til anvendelse af enheden"
        },
        "enh042datofortidsbegrnsetdispensation": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for tidsbegrænset dispensation"
        },
        "enh044datofordelvisibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for delvis ibrugtagningstilladelse"
        },
        "enh045udlejningsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Udlejningsforhold, str),
            "cardinality": "1..1",
            "description": "angiver enhedens udlejningsforhold"
        },
        "enh046offentligsttte": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.OffentligStøtte, str),
            "cardinality": "1..1",
            "description": "angiver offentlig støtte"
        },
        "enh047indflytningdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for indflytning"
        },
        "enh048godkendttombolig": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.GodkendtTomBoligÆndretAdministrativPraksis, str),
            "cardinality": "1..1",
            "description": "angiver om boligen er godkendt som tom bolig"
        },
        "enh051varmeinstallation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Varmeinstallation, str),
            "cardinality": "1..1",
            "description": "angiver enhedens varmeinstallation"
        },
        "enh052opvarmningsmiddel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Opvarmningsmiddel, str),
            "cardinality": "1..1",
            "description": "angiver enhedens opvarmningsmiddel"
        },
        "enh053supplerendevarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.SupplerendeVarme, str),
            "cardinality": "1..1",
            "description": "angiver enhedens supplerende varme"
        },
        "enh060enhedensandelfllesadgangsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens andel i fælles adgangsareal"
        },
        "enh061arealafabenoverdkning": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens areal af åben overdækning"
        },
        "enh062arealaflukketoverdkningudestue": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens areal af lukket overdækning"
        },
        "enh063antalvrelsertilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal værelser i enheden der anvendes til erhverv"
        },
        "enh065antalvandskylledetoiletter": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal vandskyllende toiletter"
        },
        "enh066antalbadevrelser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal badeværelser"
        },
        "enh067stjisolering": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver årstal for støjisolering"
        },
        "enh101gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver gyldighedsdato for enheden"
        },
        "enh127fysiskarealtilbeboelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens fysiske areal til beboelse"
        },
        "enh128fysiskarealtilerhverv": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver enhedens fysiske areal til erhverv"
        },
        "enh500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "enh068flexboligtilladelsesart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Tilladelsesart, str),
            "cardinality": "1..1",
            "description": "angivelse af om en tilladelse til flexbolig er personlig eller ej og om den er med eller uden tidsbegrænsning"
        },
        "enh069flexboligophrsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "​dato for ophør af en tidsbegrænset flexboligtilladelse"
        },
        "enh070abenaltantagterrasseareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "samlet areal af åben altan og/eller åben tagterrasse"
        },
        "enh102herafareal1": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh105"
        },
        "enh103herafareal2": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh106"
        },
        "enh104herafareal3": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Anvendelseskoden for det pågældende areal fremgår af feltet enh107"
        },
        "enh105supplerendeanvendelseskode1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Enhedsanvendelse, str),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh102"
        },
        "enh106supplerendeanvendelseskode2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Enhedsanvendelse, str),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh103"
        },
        "enh107supplerendeanvendelseskode3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Enhedsanvendelse, str),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en erhvervsenhed som har anvendelser. Enhedens areal med den pågældende anvendelse fremgår af feltet enh104"
        },
        "enh071adressefunktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.AdresseRolle, str),
            "cardinality": "1..1",
            "description": "angiver adressens funktion i forhold til denne enhed"
        },
        "adresseidentificerer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Adresse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "etage": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Etage, str),
            "cardinality": "1..1",
            "description": ""
        },
        "bygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "1..1",
            "description": ""
        },
        "opgang": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Opgang, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejerlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Ejendomsrelation, str),
            "cardinality": "0..*",
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