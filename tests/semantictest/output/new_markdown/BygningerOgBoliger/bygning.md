---
title: Bygning
draft: false
type: entity
---

# Bygning

en bygning består af en eller flere konstruktioner, der udgør en rumlig helhed, og som skærmer mod vejrliget. En bygning består som minimum af en overdækning (et tag)

### Semantic Template
```python
p.io.declare_input(
    output_name="bygning",
    attributes={
        "byg007bygningsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens nummer indenfor ejendommen"
        },
        "byg021bygningensanvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Bygningsanvendelse, str),
            "cardinality": "1..1",
            "description": "angiver bygningens hovedanvendelse"
        },
        "byg024antallejlighedermedkkken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "antal lejligheder med køkken i bygning"
        },
        "byg025antallejlighederudenkkken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "antal lejligheder uden køkken i bygning"
        },
        "byg026opfrelsesar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens opførselsår"
        },
        "byg027omtilbygningsar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens seneste om- eller tilbygningsår"
        },
        "byg029datoformidlertidigopfrtbygning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver udløbsdato for midlertidig opført bygning"
        },
        "byg030vandforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Vandforsyning, str),
            "cardinality": "1..1",
            "description": "angiver bygningens vandforsyning"
        },
        "byg031aflbsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Afløbsforhold, str),
            "cardinality": "1..1",
            "description": "angiver bygningens afløbsforhold"
        },
        "byg032ydervggensmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.YdervæggenesMateriale, str),
            "cardinality": "1..1",
            "description": "angiver bygningens ydervægsmateriale"
        },
        "byg033tagdkningsmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Tagdækningsmateriale, str),
            "cardinality": "1..1",
            "description": "angiver bygningens tagdækningsmateriale"
        },
        "byg034supplerendeydervggensmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.YdervæggenesMateriale, str),
            "cardinality": "1..1",
            "description": "angiver bygningens supplerende ydervægsmateriale"
        },
        "byg035supplerendetagdkningsmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Tagdækningsmateriale, str),
            "cardinality": "1..1",
            "description": "angiver bygningens supplerende tagdækningsmateriale"
        },
        "byg036asbestholdigtmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.AsbestholdigtMateriale, str),
            "cardinality": "1..1",
            "description": "angivelse af om der er konstateret asbestholdigt materiale i ydervæg eller tagdækning"
        },
        "byg037kildetilbygningensmaterialer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KildeTilOplysninger, str),
            "cardinality": "1..1",
            "description": "angiver kilde til bygningens materialer"
        },
        "byg038samletbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens samlede areal"
        },
        "byg039bygningenssamledeboligareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens samlede boligareal"
        },
        "byg040bygningenssamledeerhvervsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens samlede erhvervsareal"
        },
        "byg041bebyggetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver bygningens bebyggede areal"
        },
        "byg042arealindbyggetgarage": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af indbygget garage"
        },
        "byg043arealindbyggetcarport": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af indbygget carport"
        },
        "byg044arealindbyggetudhus": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af indbygget udhus"
        },
        "byg045arealindbyggetudestueellerlign": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af indbygget udestue"
        },
        "byg046samletarealaflukkedeoverdkningerpabygningen": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af lukkede overdækninger på hele bygningen"
        },
        "byg047arealafaffaldsrumiterrnniveau": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af samtlige affaldsrum i terrænniveau"
        },
        "byg048andetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver øvrige arealer i bygningen"
        },
        "byg049arealafoverdkketareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver arealet af overdækket areal på bygning"
        },
        "byg050arealabneoverdkningerpabygningensamlet": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver det samlede areal af åbne overdækninger på bygningen"
        },
        "byg051adgangsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver det samlede adgangsareal på bygning"
        },
        "byg052beregningsprincipcarportareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.BeregningsprincipForArealAfCarport, str),
            "cardinality": "1..1",
            "description": "angiver beregningsprincip for areal af carport"
        },
        "byg053bygningsarealerkilde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KildeTilOplysninger, str),
            "cardinality": "1..1",
            "description": "angiver kilde til oplysninger om bygningens arealer"
        },
        "byg054antaletager": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal etager i bygningen"
        },
        "byg055afvigendeetager": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.AfvigendeEtager, str),
            "cardinality": "1..1",
            "description": "angiver om bygningen indeholder afvigende etager"
        },
        "byg056varmeinstallation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Varmeinstallation, str),
            "cardinality": "1..1",
            "description": "angiver bygningens primære varmeinstallation"
        },
        "byg057opvarmningsmiddel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Opvarmningsmiddel, str),
            "cardinality": "1..1",
            "description": "angiver bygningens primære opvarmningsmiddel"
        },
        "byg058supplerendevarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.SupplerendeVarme, str),
            "cardinality": "1..1",
            "description": "angiver supplerende varmeinstallation i bygningen"
        },
        "byg069sikringsrumpladser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antallet at sikringsrumpladser i bygningen"
        },
        "byg070fredning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Fredning, str),
            "cardinality": "1..1",
            "description": "angiver om bygningen er fredet"
        },
        "byg071bevaringsvrdighedreference": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "linker til Kulturstyrelsens registrering i FBB (Fredede og Bevaringsværdige Bygninger)"
        },
        "byg094revisionsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver revisionsdato for seneste ændring af geometrioplysninger"
        },
        "byg111stormradetsoversvmmelsesselvrisiko": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Oversvømmelsesselvrisiko, str),
            "cardinality": "1..1",
            "description": "erstatning efter stormflod og oversvømmelse"
        },
        "byg112datoforregistreringfrastormradet": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for registrering"
        },
        "byg113byggeskadeforsikringsselskab": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Byggeskadeforsikringsselskab, str),
            "cardinality": "1..1",
            "description": "angiver navnet på byggeskadeforsikringsselskab"
        },
        "byg114datoforbyggeskadeforsikring": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver ikrafttrædelsesdatoen for byggeskadeforsikring"
        },
        "byg119udledningstilladelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Udledningstilladelse, str),
            "cardinality": "1..1",
            "description": "angiver status for udledningstilladelse på bygningen"
        },
        "byg121omfattetafbyggeskadeforsikring": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.OmfattetAfByggeskadeforsikring, str),
            "cardinality": "1..1",
            "description": "angiver om bygningen er omfattet af byggeskadeforsikring"
        },
        "byg122gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver gyldighedsdato i forbindelse med vurdering"
        },
        "byg123medlemskabafspildevandsforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.MedlemsskabAfSplidevandforsyning, str),
            "cardinality": "1..1",
            "description": "angiver om der for bygningen er indgået kontraktligt medlemskab af spildevandsforsyningsselskab"
        },
        "byg124pabudvedrspildevandsafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Rensningspåbud, str),
            "cardinality": "1..1",
            "description": "angiver om der er givet påbud vedr. spildevandsafledning på bygningen"
        },
        "byg125fristvedrspildevandsafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for frist for evt. påbud vedr. spildevandsafledning på bygningen"
        },
        "byg126tilladelsetiludtrden": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TilladelseTilUdtræden, str),
            "cardinality": "1..1",
            "description": "angiver tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "byg127datofortilladelsetiludtrden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "byg128tilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TilladelseTilAlternativBortskaffelseEllerAfledning, str),
            "cardinality": "1..1",
            "description": "angiver tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "byg129datofortilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "den dato, hvor bygningens tilladelse til alternativ afledning er meddelt eller bortfaldet"
        },
        "byg130arealafudvendigefterisolering": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver areal af udvendig efterisolering"
        },
        "byg131dispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.DispensationFritagelseIftKollektivVarmeforsyning, str),
            "cardinality": "1..1",
            "description": "angiver om der er givet dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "byg132datofordispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "byg133kildetilkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KildeTilKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "kodeliste der angiver kilden til geometrioplysninger"
        },
        "byg134kvalitetafkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.KvalitetAfKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "kodeliste der angiver kvaliteten af geometrioplysninger"
        },
        "byg135supplerendeoplysningomkoordinatst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.SupplerendeOplysningerOmKoordinatsæt, str),
            "cardinality": "1..1",
            "description": "angiver om det fysiske objekt koordinatsættet referer til ligger under eller over jorden"
        },
        "byg136placeringpasterritorie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.BygværkPåSøterritorie, str),
            "cardinality": "1..1",
            "description": "angiver om objekt ligger på søterritorie"
        },
        "byg137banedanmarkbygvrksnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver Banedanmarks BGV-nummer og bygværksnummer"
        },
        "byg301typeafflytning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TypeAfFlytning, str),
            "cardinality": "1..1",
            "description": "angiver type af flytning af en bygning"
        },
        "byg302tilflytterkommune": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver den kommune bygningen flyttes til"
        },
        "byg403vrigebemrkningerfrastormradet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "naturskaderådet oplyser"
        },
        "byg404koordinat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver bygningens geografiske repræsentation i form af et punkt"
        },
        "byg406koordinatsystem": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Koordinatsystem, str),
            "cardinality": "1..1",
            "description": "angiver geografisk koordinatsystem og projektion"
        },
        "byg500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "byg150gulvbelgning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Gulvbelaegning, str),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en bygning til erhvervsformål. Angiver typen af gulvbelægning fx beton"
        },
        "byg151frihjde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "oplysning som kan knyttes til en bygning til lagerformål, garage e.l. angiver den maksimale højde af køretøjer der kan køre ind og ud af bygningen"
        },
        "byg152abenlukketkonstruktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Konstruktion, str),
            "cardinality": "1..1",
            "description": "information om bygningen udgør en åben eller lukket konstruktion, dvs. med eller uden ydervægge"
        },
        "byg153konstruktionsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Konstruktionsforhold, str),
            "cardinality": "1..1",
            "description": "information om typen af bygningens bærende konstruktion"
        },
        "byg140servitutforudlejningsejendomdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for eventuel tinglyst servitut der undtager en udlejningsejendom for byggeskadeforsikring"
        },
        "bygningpafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Ejendomsrelation, str),
            "cardinality": "0..*",
            "description": ""
        },
        "jordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "grund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Grund, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejerlejlighed": {
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