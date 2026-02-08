---
title: TekniskAnlæg
draft: false
type: entity
---

# TekniskAnlæg

et teknisk anlæg er en stedfast, klart afgrænset konstruktion, der er opført til et bestemt formål, og som ikke karakteriseres som en bygning

### Semantic Template
```python
p.io.declare_input(
    output_name="tekniskanlæg",
    attributes={
        "tek007anlgsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver anlæggets nummer indenfor ejendommen"
        },
        "tek020klassifikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Klassifikation, str),
            "cardinality": "1..1",
            "description": "angiver det tekniske anlægs anvendelse"
        },
        "tek021fabrikattype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver det tekniske anlægs fabrikattype"
        },
        "tek022eksterndatabase": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angivelse af reference til ekstern database"
        },
        "tek023eksternngle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver unik teknisk nøgle til det tekniske anlæg"
        },
        "tek024etableringsar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver år for færdigetablering"
        },
        "tek025tilombygningsar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver til/ombygningsår for det tekniske anlæg"
        },
        "tek026strrelsesklasseolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Størrelseklasse, str),
            "cardinality": "1..1",
            "description": "angiver størrelsesklasse af olietank"
        },
        "tek027placering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Placering, str),
            "cardinality": "1..1",
            "description": "angivelse af placering af tank"
        },
        "tek028sljfningolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Sløjfning, str),
            "cardinality": "1..1",
            "description": "angiver forhold for sløjfning af olietank"
        },
        "tek030fabrikationsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "tankens fabrikationsnummer"
        },
        "tek031typegodkendelsesnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver typegodkendelse af tank"
        },
        "tek032strrelse": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver tankens størrelse"
        },
        "tek033type": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TypeAfVægge, str),
            "cardinality": "1..1",
            "description": "angiver olietankens type"
        },
        "tek034indholdolietank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Indhold, str),
            "cardinality": "1..1",
            "description": "angiver tankens/olietankens Indhold"
        },
        "tek035sljfningsfristolietank": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for frist for sløjfning af tank"
        },
        "tek036rumfang": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver rumfang af teknisk anlæg"
        },
        "tek037areal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver det bebyggede areal af teknisk anlæg"
        },
        "tek038hjde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver det tekniske anlægs højde"
        },
        "tek039effekt": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver effekt for et energiproducerende teknisk anlæg"
        },
        "tek040fredning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Fredning, str),
            "cardinality": "1..1",
            "description": "angiver eventuel type af fredning der gælder for det teknisk anlæg"
        },
        "tek042revisionsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver revisionsdato for seneste ændring af geometrioplysninger"
        },
        "tek045koordinatsystem": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Koordinatsystem, str),
            "cardinality": "1..1",
            "description": "angiver geografisk koordinatsystem og projektion"
        },
        "tek067fabrikationsar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver fabrikationsår for tanke"
        },
        "tek068materiale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Materiale, str),
            "cardinality": "1..1",
            "description": "angiver det materiale tanken er lavet af"
        },
        "tek069supplerendeindvendigkorrosionsbeskyttelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.SupplerendeIndvendigKorrosionsbeskyttelse, str),
            "cardinality": "1..1",
            "description": "angiver type af senest udførte supplerende indvendig korrosionsbeskyttelse"
        },
        "tek070datoforsenestudfrtesupplerendeindvendigkorrosionsbeskyttelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for den senest udførte indvendige korrosionsbeskyttelse"
        },
        "tek072sljfningsar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver årstal for sløjfning af tank"
        },
        "tek073navhjde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "angiver vindmøllens højde ved navet"
        },
        "tek074vindmllenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver den unikke identifikation af vindmøllen"
        },
        "tek075rotordiameter": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "angiver diameteren for rotoren på vindmøllen"
        },
        "tek076kildetilkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KildeTilKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "angiver kilden til geometrioplysninger"
        },
        "tek077kvalitetafkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KvalitetAfKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "angiver kvaliteten af geometrioplysninger"
        },
        "tek078supplerendeoplysningomkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.SupplerendeOplysningerOmKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "angiver om det fysiske objekt"
        },
        "tek101gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver gyldighedsdato i forbindelse med vurdering"
        },
        "tek102fabrikatvindmlle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver fabrikat på vindmølle"
        },
        "tek103fabrikatoliefyr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver fabrikat på oliefyr"
        },
        "tek104fabrikatsolcelleanlgsolvarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver fabrikat på solcelleanlæg eller solvarmeanlæg"
        },
        "tek105overdkningtank": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver om tanken er overdækket"
        },
        "tek106inspektionsdatotank": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for inspektion af tank"
        },
        "tek107placeringpasterritorie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.BygværkPåSøterritorie, str),
            "cardinality": "1..1",
            "description": "angiver om teknisk anlæg ligger på søterritorie"
        },
        "tek109koordinat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver det tekniske areals geografiske placering"
        },
        "tek500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "tek110driftstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Driftstatus, str),
            "cardinality": "1..1",
            "description": "angiver om anlægget er i drift eller ikke"
        },
        "tek111datoforsenesteinspektion": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "information om tidspunktet for seneste inspektion af det tekniske anlæg"
        },
        "tek112inspicerendevirksomhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "information om virksomhed der udført seneste inspektion af det tekniske anlæg"
        },
        "jordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "bygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "grund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Grund, str),
            "cardinality": "0..1",
            "description": ""
        },
        "bygningpafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Ejendomsrelation, str),
            "cardinality": "0..1",
            "description": ""
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Husnummer, str),
            "cardinality": "0..1",
            "description": ""
        },
        "ejerlejlighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Ejendomsrelation, str),
            "cardinality": "0..1",
            "description": ""
        },
        "enhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Enhed, str),
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