---
title: CprAdresse
draft: false
type: entity
---

# CprAdresse

adresse som den er defineret i CPR registret, med reference til DAR adresse når denne reference kendes

### Semantic Template
```python
p.io.declare_input(
    output_name="cpradresse",
    attributes={
        "bygningsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "bygningsnummer anvendes på Grønland som selvstændigt datum eller i stedet for husnummer. Kan være udfyldt med op til 4 tegn"
        },
        "bynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "bynavn i klarskrift. Benyttes som en del af den postale adresse, hvor postnummer og postdistrikt er utilstrækkeligt, ved forsendelse af post til borgeren"
        },
        "cprvejkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "CPR-Vejkode danner sammen med CPR-kommunekode en entydig kode for en vej i CPR. Værdimængde: 0001 - 9999"
        },
        "etage": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "etageangivelse i adressen. 01 - 99 samt kl, k2, k3, st og blank. mz, kv, og pt kan desuden forekomme ved adresseregistreringer"
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "feltet angiver husnummer på en given bolig. Position 1-3: 001 - 999 eller blanke i alle tre positioner. Position 4: A - Z eller blank. Er de tre første positioner blanke er 4. Position også blank"
        },
        "postdistrikt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver postdistrikts navn i klarskrift. Feltet er på 20 karakterer, så det sammen med postnummer + 1 blank kan være i en rudekuvert"
        },
        "vejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "hvis adressen er tilknyttet en DAR UUID, er vejnavn identisk med DAR NavngivenVej.vejnavn attributten, og der henvises derfor til definitionen heraf. Hvis adressen ikke er tilknyttet en DAR UUID, er vejnavn CPR’s vejnavn for en administrativ vej (såkaldt høj vejkode), CPR’s vejnavn for en administrativ vej i en administrativ kommune, CPR’s vejnavn for en vej i en grønlandsk adresse eller CPR’s vejnavn for en vej i en adresse, hvor adressen ikke er knyttet til en adresse i DAR"
        },
        "postnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "postvæsenets landsdækkende postnummerkode"
        },
        "sidedoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "side- eller dørnummer for en bolig. Identificerer sammen med kommunekode, vejkode, husnummer, og etage en bolig"
        },
        "vejadresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "forkortet udgave af vejnavn på højst 20 tegn. Hvis adressen er tilknyttet en DAR UUID, er vejadresseringsnavn identisk med DAR NavngivenVej.vejadresseringsnavn attributten, og der henvises derfor til definitionen heraf"
        },
        "daradresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Adresse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```