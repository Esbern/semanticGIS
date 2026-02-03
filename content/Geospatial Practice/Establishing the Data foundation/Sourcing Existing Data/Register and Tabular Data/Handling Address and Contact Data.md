---
title: " Best Practice: Handling Address & Contact Data"
draft: false
tags:
---
 
## The Principle: Don't Mix "Who" with "Where"
In many environmental projects, stakeholder data is collected haphazardly. A common mistake is treating a database cell like a postal label.
* **The Mistake:** Lumping the person's name, the "Care of" (C/O), and the street address into a single column.
* **The Consequence:**
    * **Geocoding fails:** The GIS cannot find a coordinate for "Farmer Jensen".
    * **Mail Merge fails:** You cannot write "Dear Mr. Jensen" automatically.
    * **Sorting fails:** You cannot group stakeholders by city or street.

### Level 1: Minimum Viable Normalization (The "Safe Enough" Approach)
If you cannot enforce a strict database schema, you must *at absolute minimum* separate the **Entity** from the **Location**.

| Name / Contact (WHO) | Address String (WHERE) | Postcode & City |
| :--- | :--- | :--- |
| **Why?** | **Why?** | **Why?** |
| Stores names, C/O, and attention. This is for *reading*, not mapping. | Stores Street, Number, Floor, Door. This allows Geocoders (like Google Maps) to function. | Allows quick filtering and sorting. |
| *Example:*<br>`Søren Hansen c/o Staldgården` | *Example:*<br>`Markvejen 2, 1. th` | *Example:*<br>`4000 Roskilde` |

* **Pros:** Easy for non-technical users to type.
* **Cons:** Still hard to customize letters ("Dear Søren" vs "Dear Hansen"); Geocoding might struggle with floor/door numbers if the parser is strict.

---

### Level 2: The "Golden Standard" (Atomic Data)
For robust GIS projects, databases, and large-scale mailings, every semantic concept gets its own column. This is the **SemanticGIS** recommendation.

| Column | Description | Example |
| :--- | :--- | :--- |
| **First Name** | Personal name (for informal mail merge). | `Søren` |
| **Last Name** | Surname (for sorting/formal mail). | `Hansen` |
| **Entity/CO** | Company name or "Care of". | `Staldgården ApS` |
| **Street Name** | Strictly the road name (from `NavngivenVej`). | `Markvejen` |
| **House No.** | The number (from `Husnummer`). | `2` |
| **Unit** | Floor/Door (from `Adresse`). | `1. th` |
| **Postcode** | 4-digit code. | `4000` |
| **City** | Postal district. | `Roskilde` |

* **Pros:** 100% Geocoding match rate; perfect sorting; flexible communication.
* **Cons:** Takes more time to input manually.

---

### Cleaning Strategy: The "Un-tangling" Workflow
If you inherit a "messy" dataset (where everything is in one cell), do not rely on simple scripts or Excel formulas to fix it. Human entry is too unpredictable.

**Recommended Workflow:**
1.  **Analyze the Heterogeneity:** Look at the data. Is it consistent enough for a pattern?
2.  **Use AI Assistance:** LLMs (like ChatGPT) are excellent at parsing unstructured addresses. You can paste a batch of messy addresses and ask it to "Output this as a CSV with columns: Name, Street, Number, Postcode."
3.  **Manual Verification:** Always spot-check the results, especially for "C/O" addresses versus "Living at" addresses.

### ⚠️ Critical Concept: Legal Unit vs. Production Unit

When working with business data (farmers, factories, shops), you must distinguish between the **Administrative** address and the **Physical** address. In the Danish CVR register, these are two separate entities:

**1. The Legal Unit (_Virksomhed_ / CVR-nummer)**
- **What is it?** The economic and legal entity.
- **The Address:** Often points to an administration building, a holding company, or an **accountant**.
- **Use for:** Mailing contracts, legal notices, or invoices.
- **The Trap:** If you geocode this, your "farm" might appear in the middle of a city center (at the accountant's office).
    

**2. The Production Unit (_P-enhed_ / P-nummer)**
- **What is it?** The physical location where the activity takes place.
- **The Address:** Points to the actual farm, factory, or shop.
- **Use for:** Fieldwork, environmental analysis, and mapping "where the cows are."
    

**Best Practice:**
- Always check if your dataset contains CVR-numbers or P-numbers.
- For environmental projects, you almost always want the **P-enhed**.
    
- _Note:_ A single Legal Unit (Firm/) can own multiple Production Units (several distinct locations).
---
### ⚠️ The "No Newline" Rule

**Never use `Alt+Enter` (Line Breaks) within a single Excel cell.**
While this looks nice on a printed sheet, it breaks almost every data processing tool (GIS, Python, SQL). A line break is often interpreted by software as "End of Row," causing your dataset to scramble or truncate during import.

* **Bad:**
  `Markvejen 1 [Line Break] 4000 Roskilde`
* **Good:**
  `Markvejen 1, 4000 Roskilde`