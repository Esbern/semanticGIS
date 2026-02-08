---
title: CprAdresse
draft: false
type: entity
---

# CprAdresse

Adresse som den er defineret i CPR registret, med reference til DAR adresse når denne reference kendes.

### Semantic Template
```python
p.io.declare_input(
    output_name="cpradresse",
    attributes={
        "bygningsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Bygningsnummer anvendes på Grønland som selvstændigt datum eller i stedet for husnummer. Kan være udfyldt med op til 4 tegn."
        },
        "bynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Bynavn i klarskrift. Benyttes som en del af den postale adresse, hvor postnummer og postdistrikt er utilstrækkeligt, ved forsendelse af post til borgeren."
        },
        "conavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "cprkommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "cprvejkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "daradresse": {
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
        "etage": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Etageangivelse i adressen.01 - 99 samt kl, k2, k3, st og blank.mz, kv, og pt kan desuden forekomme ved adresseregistreringer."
        },
        "fraflytningsdatokommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "fraflytningsdatokommuneusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
        "fraflytningskommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Feltet angiver husnummer på en given bolig. Position 1-3: 001 - 999 eller blanke i alle tre positioner.Position   4: A - Z eller blank.Er de tre første positioner blanke er 4. Position også blank"
        },
        "personid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "postdistrikt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Angiver postdistrikts navn i klarskrift. Feltet er på 20 karakterer, så det sammen med postnummer + 1 blank kan være i en rudekuvert."
        },
        "postnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Postvæsenets landsdækkende postnummerkode."
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "sidedoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseadresselinie1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseadresselinie2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseadresselinie3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseadresselinie4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseadresselinie5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadresseregistreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "supplerendeadressestatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadressevirkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadressevirkningframyndighedskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "supplerendeadressevirkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "tilflytningsdatokommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "tilflytningsdatokommuneusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
        "vejadresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Forkortet udgave af vejnavn på højst 20 tegn. Hvis adressen er tilknyttet en DAR UUID, er vejadresseringsnavn identisk med DAR NavngivenVej.vejadresseringsnavn attributten, og der henvises derfor til definitionen heraf."
        },
        "vejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Hvis adressen er tilknyttet en DAR UUID, er vejnavn identisk med DAR NavngivenVej.vejnavn attributten, og der henvises derfor til definitionen heraf. Hvis adressen ikke er tilknyttet en DAR UUID, er vejnavn CPR’s vejnavn for en administrativ vej (såkaldt høj vejkode), CPR’s vejnavn for en administrativ vej i en administrativ kommune, CPR’s vejnavn for en vej i en grønlandsk adresse eller CPR’s vejnavn for en vej i en adresse, hvor adressen ikke er knyttet til en adresse i DAR."
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
    }
)
```
