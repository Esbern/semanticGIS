# Danmarks Administrative Geografiske Inddeling entity catalog (inherited attributes)

Total entities: 13

## Afstemningsområde
### Sources
- Afstemningsområde (aggregate)
- Afstemningsområde_2000000 (1:2000000)
- Afstemningsområde_250000 (1:250000)
- Afstemningsområde_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- afstemningsområdenummer: CharacterString [1..1]
- afstemningsstedNavn: CharacterString [1..1]
- afstemningsstedAdresse: EAID_6043F4D9_C4CA_44d0_BE88_027166A8B008 -> Afstemningsområde (role afstemningsområde; 0..1 ⇢ 1..1)
- kommune: Kommuneinddeling -> Kommuneinddeling (role afstemningsområde; 1..1 ⇢ 1..*)
- opstillingskreds: Opstillingskreds -> Opstillingskreds (role afstemningsområde; 1..1 ⇢ 1..*)
- afstemningsstedHusnummer: EAID_D0A626FC_CCAE_4209_B2F6_AC919B74A528 -> Afstemningsområde (role afstemningsområde; 1..1 ⇢ 1..1)
- afstemningsområde: Afstemningsområde -> Afstemningsområde (role afstemningsstedAdresse; 1..1 ⇢ 0..1)

## Danmark
### Sources
- Danmark (aggregate)
- Danmark_2000000 (1:2000000)
- Danmark_250000 (1:250000)
- Danmark_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]

## Kommuneinddeling
### Sources
- Kommuneinddeling (aggregate)
- Kommuneinddeling_2000000 (1:2000000)
- Kommuneinddeling_250000 (1:250000)
- Kommuneinddeling_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- kommunekode: CharacterString [1..1]
- udenforKommuneinddeling: Boolean [1..1]
- region: Regionsinddeling -> Regionsinddeling (role kommune; 1..1 ⇢ 1..*)
- kommune: Kommuneinddeling -> Kommuneinddeling (role region; 1..* ⇢ 1..1)

## Landsdel
### Sources
- Landsdel (aggregate)
- Landsdel_2000000 (1:2000000)
- Landsdel_250000 (1:250000)
- Landsdel_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]

## Opstillingskreds
### Sources
- Opstillingskreds (aggregate)
- Opstillingskreds_2000000 (1:2000000)
- Opstillingskreds_250000 (1:250000)
- Opstillingskreds_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- opstillingskredsnummer: CharacterString [1..1]
- valgkredsnummer: CharacterString [1..1]
- kredskommunenavn: CharacterString [1..1]
- kredskommunenummer: CharacterString [1..1]
- storkreds: Storkreds -> Storkreds (role opstillingskreds; 1..1 ⇢ 1..*)
- opstillingskreds: Opstillingskreds -> Opstillingskreds (role storkreds; 1..* ⇢ 1..1)

## Politikreds
### Sources
- Politikreds (aggregate)
- Politikreds_2000000 (1:2000000)
- Politikreds_250000 (1:250000)
- Politikreds_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- myndighedskode: CharacterString [1..1]
- politikredsnummer: CharacterString [1..1]

## Postnummerinddeling
### Sources
- Postnummerinddeling (aggregate)
- Postnummerinddeling_2000000 (1:2000000)
- Postnummerinddeling_250000 (1:250000)
- Postnummerinddeling_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- erGadepostnummer: Boolean [1..1]
- postnummer: CharacterString [1..1]

## Regionsinddeling
### Sources
- Regionsinddeling (aggregate)
- Regionsinddeling_2000000 (1:2000000)
- Regionsinddeling_250000 (1:250000)
- Regionsinddeling_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- regionskode: CharacterString [1..1]

## Retskreds
### Sources
- Retskreds (aggregate)
- Retskreds_2000000 (1:2000000)
- Retskreds_250000 (1:250000)
- Retskreds_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- myndighedskode: CharacterString [1..1]
- retskredsnummer: CharacterString [1..1]

## Sogneinddeling
### Sources
- Sogneinddeling (aggregate)
- Sogneinddeling_2000000 (1:2000000)
- Sogneinddeling_250000 (1:250000)
- Sogneinddeling_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- sognekode: CharacterString [1..1]

## Storkreds
### Sources
- Storkreds (aggregate)
- Storkreds_2000000 (1:2000000)
- Storkreds_250000 (1:250000)
- Storkreds_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- storkredsnummer: CharacterString [1..1]
- valglandsdel: Valglandsdel -> Valglandsdel (role storkreds; 1..1 ⇢ 1..*)
- storkreds: Storkreds -> Storkreds (role valglandsdel; 1..* ⇢ 1..1)

## SupplerendeBynavn
### Sources
- SupplerendeBynavn (aggregate)
- SupplerendeBynavn_2000000 (1:2000000)
- SupplerendeBynavn_250000 (1:250000)
- SupplerendeBynavn_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- kommune: Kommuneinddeling -> Kommuneinddeling (role supplerendeBynavn; 1..1 ⇢ 0..*)
- supplerendeBynavn: SupplerendeBynavn -> SupplerendeBynavn (role kommune; 0..* ⇢ 1..1)

## Valglandsdel
### Sources
- Valglandsdel (aggregate)
- Valglandsdel_2000000 (1:2000000)
- Valglandsdel_250000 (1:250000)
- Valglandsdel_500000 (1:500000)

### Attributes
- id: Identifikation [1..1]
- navn: CharacterString [1..1]
- registreringFra: DateTime [1..1]
- registreringTil: DateTime [0..1]
- registreringsaktør: Registreringsaktør [1..1]
- virkningFra: DateTime [1..1]
- virkningTil: DateTime [0..1]
- virkningsaktør: Virkningsaktør [1..1]
- forretningshændelse: Forretningshændelse [1..1]
- forretningsproces: Forretningsproces [1..1]
- geometri: GM_MultiSurface [1..1]
- valglandsdelsbogstav: CharacterString [1..1]
