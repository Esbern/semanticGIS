---
title: TekniskAnlaeg
draft: false
type: entity
---

# TekniskAnlaeg

et teknisk anlæg er en stedfast, klart afgrænset konstruktion, der er opført til et bestemt formål, og som ikke karakteriseres som en bygning

### Semantic Template
```python
p.io.declare_input(
    output_name="tekniskanlaeg",
    attributes={
        "bygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "ejerlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "enhed": {
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
        "grund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "jordstykke": {
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
        "tek007anlaegsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver anlæggets nummer indenfor ejendommen"
        },
        "tek020klassifikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.klassifikation, str),
            "description": "angiver det tekniske anlægs anvendelse"
        },
        "tek021fabrikattype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver det tekniske anlægs fabrikattype"
        },
        "tek022eksterndatabase": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angivelse af reference til ekstern database"
        },
        "tek023eksternnoegle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver unik teknisk nøgle til det tekniske anlæg"
        },
        "tek024etableringsaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver år for færdigetablering"
        },
        "tek025tilombygningsaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver til/ombygningsår for det tekniske anlæg"
        },
        "tek026stoerrelsesklasseolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.størrelseklasse, str),
            "description": "angiver størrelsesklasse af olietank"
        },
        "tek027placering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.placering, str),
            "description": "angivelse af placering af tank"
        },
        "tek028sloejfningolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.sløjfning, str),
            "description": "angiver forhold for sløjfning af olietank"
        },
        "tek030fabrikationsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "tankens fabrikationsnummer"
        },
        "tek031typegodkendelsesnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver typegodkendelse af tank"
        },
        "tek032stoerrelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver tankens størrelse"
        },
        "tek033type": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.typeafvægge, str),
            "description": "angiver olietankens type"
        },
        "tek034indholdolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.indhold, str),
            "description": "angiver tankens/olietankens Indhold"
        },
        "tek035sloejfningsfristolietank": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for frist for sløjfning af tank"
        },
        "tek036rumfang": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver rumfang af teknisk anlæg"
        },
        "tek037areal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver det bebyggede areal af teknisk anlæg"
        },
        "tek038hoejde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver det tekniske anlægs højde"
        },
        "tek039effekt": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver effekt for et energiproducerende teknisk anlæg"
        },
        "tek040fredning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.fredning, str),
            "description": "angiver eventuel type af fredning der gælder for det teknisk anlæg"
        },
        "tek042revisionsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver revisionsdato for seneste ændring af geometrioplysninger"
        },
        "tek045koordinatsystem": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.koordinatsystem, str),
            "description": "angiver geografisk koordinatsystem og projektion"
        },
        "tek067fabrikationsaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver fabrikationsår for tanke"
        },
        "tek068materiale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.materiale, str),
            "description": "angiver det materiale tanken er lavet af"
        },
        "tek069supplerendeindvendigkorrosionsbeskyttelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.supplerendeindvendigkorrosionsbeskyttelse, str),
            "description": "angiver type af senest udførte supplerende indvendig korrosionsbeskyttelse"
        },
        "tek070datoforsenestudfoertesupplerendeindvendigkorrosionsbeskyttelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for den senest udførte indvendige korrosionsbeskyttelse"
        },
        "tek072sloejfningsaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver årstal for sløjfning af tank"
        },
        "tek073navhoejde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.real, float),
            "description": "angiver vindmøllens højde ved navet"
        },
        "tek074vindmoellenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver den unikke identifikation af vindmøllen"
        },
        "tek075rotordiameter": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.real, float),
            "description": "angiver diameteren for rotoren på vindmøllen"
        },
        "tek076kildetilkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kildetilkoordinatsæt, str),
            "description": "angiver kilden til geometrioplysninger"
        },
        "tek077kvalitetafkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kvalitetafkoordinatsæt, str),
            "description": "angiver kvaliteten af geometrioplysninger"
        },
        "tek078supplerendeoplysningomkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.supplerendeoplysningeromkoordinatsæt, str),
            "description": "angiver om det fysiske objekt"
        },
        "tek101gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver gyldighedsdato i forbindelse med vurdering"
        },
        "tek102fabrikatvindmoelle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver fabrikat på vindmølle"
        },
        "tek103fabrikatoliefyr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver fabrikat på oliefyr"
        },
        "tek104fabrikatsolcelleanlaegsolvarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver fabrikat på solcelleanlæg eller solvarmeanlæg"
        },
        "tek105overdaekningtank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver om tanken er overdækket"
        },
        "tek106inspektionsdatotank": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for inspektion af tank"
        },
        "tek107placeringpaasoeterritorie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.bygværkpåsøterritorie, str),
            "description": "angiver om teknisk anlæg ligger på søterritorie"
        },
        "tek109koordinat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.gm_point, str),
            "description": "angiver det tekniske areals geografiske placering"
        },
        "tek110driftstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.driftstatus, str),
            "description": "angiver om anlægget er i drift eller ikke"
        },
        "tek111datoforsenesteinspektion": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "information om tidspunktet for seneste inspektion af det tekniske anlæg"
        },
        "tek112inspicerendevirksomhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "information om virksomhed der udført seneste inspektion af det tekniske anlæg"
        },
        "tek500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
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
