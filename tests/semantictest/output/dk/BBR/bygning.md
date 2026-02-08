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
            "description": "angiver bygningens nummer indenfor ejendommen"
        },
        "byg021bygningensanvendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.bygningsanvendelse, str),
            "description": "angiver bygningens hovedanvendelse"
        },
        "byg024antallejlighedermedkoekken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "antal lejligheder med køkken i bygning"
        },
        "byg025antallejlighederudenkoekken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "antal lejligheder uden køkken i bygning"
        },
        "byg026opfoerelsesaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens opførselsår"
        },
        "byg027omtilbygningsaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens seneste om- eller tilbygningsår"
        },
        "byg029datoformidlertidigopfoertbygning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver udløbsdato for midlertidig opført bygning"
        },
        "byg030vandforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.vandforsyning, str),
            "description": "angiver bygningens vandforsyning"
        },
        "byg031afloebsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.afløbsforhold, str),
            "description": "angiver bygningens afløbsforhold"
        },
        "byg032ydervaeggensmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.ydervæggenesmateriale, str),
            "description": "angiver bygningens ydervægsmateriale"
        },
        "byg033tagdaekningsmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tagdækningsmateriale, str),
            "description": "angiver bygningens tagdækningsmateriale"
        },
        "byg034supplerendeydervaeggensmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.ydervæggenesmateriale, str),
            "description": "angiver bygningens supplerende ydervægsmateriale"
        },
        "byg035supplerendetagdaekningsmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tagdækningsmateriale, str),
            "description": "angiver bygningens supplerende tagdækningsmateriale"
        },
        "byg036asbestholdigtmateriale": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.asbestholdigtmateriale, str),
            "description": "angivelse af om der er  konstateret asbestholdigt materiale i ydervæg eller tagdækning"
        },
        "byg037kildetilbygningensmaterialer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kildetiloplysninger, str),
            "description": "angiver kilde til bygningens materialer"
        },
        "byg038samletbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens samlede areal"
        },
        "byg039bygningenssamledeboligareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens samlede boligareal"
        },
        "byg040bygningenssamledeerhvervsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens samlede erhvervsareal"
        },
        "byg041bebyggetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver bygningens bebyggede areal"
        },
        "byg042arealindbyggetgarage": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af indbygget garage"
        },
        "byg043arealindbyggetcarport": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af indbygget carport"
        },
        "byg044arealindbyggetudhus": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af indbygget udhus"
        },
        "byg045arealindbyggetudestueellerlign": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af indbygget udestue"
        },
        "byg046samletarealaflukkedeoverdaekningerpaabygningen": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af lukkede overdækninger på hele bygningen"
        },
        "byg047arealafaffaldsrumiterraenniveau": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af samtlige affaldsrum i terrænniveau"
        },
        "byg048andetareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver øvrige arealer i bygningen"
        },
        "byg049arealafoverdaekketareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver arealet af overdækket areal på bygning"
        },
        "byg050arealaabneoverdaekningerpaabygningensamlet": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver det samlede areal af åbne overdækninger på bygningen"
        },
        "byg051adgangsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver det samlede adgangsareal på bygning"
        },
        "byg052beregningsprincipcarportareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.beregningsprincipforarealafcarport, str),
            "description": "angiver beregningsprincip for areal af carport"
        },
        "byg053bygningsarealerkilde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kildetiloplysninger, str),
            "description": "angiver kilde til oplysninger om bygningens arealer"
        },
        "byg054antaletager": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal etager i bygningen"
        },
        "byg055afvigendeetager": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.afvigendeetager, str),
            "description": "angiver om bygningen indeholder afvigende etager"
        },
        "byg056varmeinstallation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.varmeinstallation, str),
            "description": "angiver bygningens primære varmeinstallation"
        },
        "byg057opvarmningsmiddel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.opvarmningsmiddel, str),
            "description": "angiver bygningens primære opvarmningsmiddel"
        },
        "byg058supplerendevarme": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.supplerendevarme, str),
            "description": "angiver supplerende varmeinstallation i bygningen"
        },
        "byg069sikringsrumpladser": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antallet at sikringsrumpladser i bygningen"
        },
        "byg070fredning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.fredning, str),
            "description": "angiver om bygningen er fredet"
        },
        "byg071bevaringsvaerdighedreference": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "linker til Kulturstyrelsens registrering i FBB (Fredede og Bevaringsværdige Bygninger)"
        },
        "byg094revisionsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver revisionsdato for seneste ændring af geometrioplysninger"
        },
        "byg111stormraadetsoversvoemmelsesselvrisiko": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.oversvømmelsesselvrisiko, str),
            "description": "erstatning efter stormflod og oversvømmelse"
        },
        "byg112datoforregistreringfrastormraadet": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for registrering"
        },
        "byg113byggeskadeforsikringsselskab": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.byggeskadeforsikringsselskab, str),
            "description": "angiver navnet på byggeskadeforsikringsselskab"
        },
        "byg114datoforbyggeskadeforsikring": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver ikrafttrædelsesdatoen for byggeskadeforsikring"
        },
        "byg119udledningstilladelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.udledningstilladelse, str),
            "description": "angiver status for udledningstilladelse på bygningen"
        },
        "byg121omfattetafbyggeskadeforsikring": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.omfattetafbyggeskadeforsikring, str),
            "description": "angiver om bygningen er omfattet af byggeskadeforsikring"
        },
        "byg122gyldighedsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver gyldighedsdato i forbindelse med vurdering"
        },
        "byg123medlemskabafspildevandsforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.medlemsskabafsplidevandforsyning, str),
            "description": "angiver om der for bygningen er indgået kontraktligt medlemskab af spildevandsforsyningsselskab"
        },
        "byg124paabudvedrspildevandsafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.rensningspåbud, str),
            "description": "angiver om der er givet påbud vedr. spildevandsafledning på bygningen"
        },
        "byg125fristvedrspildevandsafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for frist for evt. påbud vedr. spildevandsafledning på bygningen"
        },
        "byg126tilladelsetiludtraeden": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tilladelsetiludtræden, str),
            "description": "angiver tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "byg127datofortilladelsetiludtraeden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "byg128tilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tilladelsetilalternativbortskaffelseellerafledning, str),
            "description": "angiver tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "byg129datofortilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "den dato, hvor bygningens tilladelse til alternativ afledning er meddelt eller bortfaldet"
        },
        "byg130arealafudvendigefterisolering": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver areal af udvendig efterisolering"
        },
        "byg131dispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.dispensationfritagelseiftkollektivvarmeforsyning, str),
            "description": "angiver om der er givet dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "byg132datofordispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "byg133kildetilkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kildetilkoordinatsæt, str),
            "description": "kodeliste der angiver kilden til geometrioplysninger"
        },
        "byg134kvalitetafkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kvalitetafkoordinatsæt, str),
            "description": "kodeliste der angiver kvaliteten af geometrioplysninger"
        },
        "byg135supplerendeoplysningomkoordinatsaet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.supplerendeoplysningeromkoordinatsæt, str),
            "description": "angiver om det fysiske objekt koordinatsættet referer til ligger under eller over jorden"
        },
        "byg136placeringpaasoeterritorie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.bygværkpåsøterritorie, str),
            "description": "angiver om objekt ligger på søterritorie"
        },
        "byg137banedanmarkbygvaerksnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver Banedanmarks BGV-nummer og bygværksnummer"
        },
        "byg140servitutforudlejningsejendomdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for eventuel tinglyst servitut der undtager en udlejningsejendom for byggeskadeforsikring"
        },
        "byg150gulvbelaegning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.gulvbelaegning, str),
            "description": "oplysning som kan knyttes til en bygning til erhvervsformål. Angiver typen af gulvbelægning fx beton"
        },
        "byg151frihoejde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "oplysning som kan knyttes til en bygning til lagerformål, garage e.l. angiver den maksimale højde af køretøjer der kan køre ind og ud af  bygningen"
        },
        "byg152aabenlukketkonstruktion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.konstruktion, str),
            "description": "information om bygningen udgør en åben eller lukket konstruktion, dvs. med eller uden ydervægge"
        },
        "byg153konstruktionsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.konstruktionsforhold, str),
            "description": "information om typen af bygningens bærende konstruktion"
        },
        "byg301typeafflytning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.typeafflytning, str),
            "description": "angiver type af flytning af en bygning"
        },
        "byg302tilflytterkommune": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver den kommune bygningen flyttes til"
        },
        "byg403oevrigebemaerkningerfrastormraadet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "naturskaderådet oplyser"
        },
        "byg404koordinat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.gm_point, str),
            "description": "angiver bygningens geografiske repræsentation i form af et punkt"
        },
        "byg406koordinatsystem": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.koordinatsystem, str),
            "description": "angiver geografisk koordinatsystem og projektion"
        },
        "byg500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
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
