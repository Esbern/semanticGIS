---
title: Ejendomsvurdering
draft: false
type: entity
---

# Ejendomsvurdering

en afgørelse af en ejendoms beskatningsmæssige værdi. Kun afsluttede vurderinger, dvs. vurderinger med status 'låst' samt overspringsvurderinger, udstilles via Datafordeleren

### Semantic Template
```python
p.io.declare_input(
    output_name="ejendomsvurdering",
    attributes={
        "bebyggelseprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "planlagt maximalt bebyggelsesprocent for et område udlagt til etageboligbebyggelse, eller ejendommens specifikke bebyggelsesprocent"
        },
        "benyttelsekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingBenyttelseKode, str),
            "cardinality": "1..1",
            "description": "benyttelseskode angiver ejendommens benyttelse, som den er blevet fastlagt i forbindelse med en vurdering"
        },
        "dkningsafgiftforskelvrdi": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "dækningsafgiftspligtig forskelsværdi for erhvervsejendomme eller dækningsafgiftspligtig forskelsværdi for offentlige ejendomme, der er fritaget for grundskyld"
        },
        "ejendomvrdibelb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "den ved en vurdering ansatte ejendomsværdi (i hele kroner)"
        },
        "grundvrdibelb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "den ved vurdering ansatte grundværdi (i hele kroner)"
        },
        "grundvrdiomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "et nummer eller bogstav, eller en kombination af tal og bogstaver, der unikt identificerer et grundværdiområde indenfor en vurderingskreds i en kommune"
        },
        "meddelelsestypekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingMeddelelsestypeKode, str),
            "cardinality": "1..1",
            "description": "typen angiver, hvilken type ejermeddelelse, der anvendes for den pågældende ejendom"
        },
        "ar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "det år vurderingen gælder for"
        },
        "antalmedvurderedelejligheder": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "antal medvurderede lejligheder i den vurderede ejendom"
        },
        "dkningsafgiftpligtkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingDækningsafgiftPligtKode, str),
            "cardinality": "1..1",
            "description": "kode, der angiver om ejendommen er helt eller delvis dækningsafgiftspligtig"
        },
        "vurderetareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "vurderet grundareal. Ejendommens samlede vurderede areal i m2 (incl. Vejareal)"
        },
        "dkningsafgiftpligttypekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingDækningsafgiftPligtTypeKode, str),
            "cardinality": "1..1",
            "description": "koden angiver typen af dækningsafgiftspligten, enten afhængig af ejertype (offentlig) eller af ejendomstypen (erhvervsmæssig)"
        },
        "ejerlejlighedkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingEjerlejlighedKode, str),
            "cardinality": "1..1",
            "description": "kode for, om en ejerlejlighed er vurderet som fri eller udlejet"
        },
        "ajourfringdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "timestamp for hvornår en vurdering, en eventuel vurderingsændring, årsregulering eller §4/4A vurdering er opdateret enten maskinelt ved en batch-kørsel eller i forbindelse med sagsbehandling"
        },
        "ndringdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for seneste gældende vurdering"
        },
        "pgf4kodevurderingophjet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kode for ophøjet §4 eller 4A vurdering. Koden angiver, om vurderingen er en årsomvurdering, der er sket ved ophøjelsen af en §4 eller 4A vurdering"
        },
        "pgf4kodevurdering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kode for § 4 eller § 4A vurdering. Koden angiver, om vurderingen er en § 4 eller § 4A vurdering eller en ændret § 4 eller § 4A vurdering"
        },
        "ndringkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingÆndringKode, str),
            "cardinality": "1..1",
            "description": "årsagen til ændringen af ejendomsvurderingen. Kode, der angiver type af vurdering eller myndighed, der har afgjort en vurdering"
        },
        "vur_vurderingsid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "nøgle der entydig identificerer en ejendomsvurdering"
        },
        "vurderingskredskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingVurderingskredsKode, str),
            "cardinality": "1..1",
            "description": "underinddeling af en kommune, som benyttes ved vurdering"
        },
        "omvurderinggrund1kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingOmvurderingGrundKode, str),
            "cardinality": "1..1",
            "description": "koden angiver årsagen til årsomvurderingen"
        },
        "omvurderinggrund2kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsvurdering.EjendomsvurderingOmvurderingGrundKode, str),
            "cardinality": "1..1",
            "description": "koden angiver årsagen til årsomvurderingen"
        },
        "klagetype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "verserende klager, genoptagelser eller skatterådesager i 1. instans (SKAT) eller verserende klager i 2. instans (Vurderingsankenævn)"
        },
        "juridiskkategorikode": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "kode der angiver den juridiske kategori, som ejendommen er tildelt ved denne ejendomsvurdering"
        },
        "juridiskkategoritekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "tekst, der beskriver den juridiske kategori, som ejendommen er tildelt ved denne ejendomsvurdering"
        },
        "juridiskunderkategorikode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kode der angiver den juridiske underkategori, som ejendommen er blevet tildelt ved denne ejendomsvurdering"
        },
        "juridiskunderkategoritekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "tekst der beskriver den juridiske underkategori, som er blevet tildelt ved denne vurdering"
        },
        "vurmark": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver kilde-system og type for vurderingen"
        },
        "styringskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..*",
            "description": "samling af egenskaber, som repræsenterer en styringskode"
        },
        "vurderingsejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.Vurderingsejendom, str),
            "cardinality": "0..1",
            "description": ""
        },
        "fordeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.Fordeling, str),
            "cardinality": "0..*",
            "description": ""
        },
        "bfenummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.BestemtFastEjendom, str),
            "cardinality": "1..*",
            "description": ""
        },
        "fradragforforbedringoverordnet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.FradragForForbedringOverordnet, str),
            "cardinality": "0..1",
            "description": ""
        },
        "grundvrdispecifikation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.Grundværdispecifikation, str),
            "cardinality": "0..*",
            "description": ""
        },
        "loftansttelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.Loftansættelse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "fritagelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejendomsvurdering.Fritagelse, str),
            "cardinality": "0..*",
            "description": ""
        }
    }
)
```