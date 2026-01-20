---
title: " Best Practice: Handling Address & Contact Data"
draft: true
tags:
---
 
# Best Practice: Handling Address & Contact Data

[[Geospatial Practice/Project Stewardship/index|Project Stewardship]] > [[Geospatial Practice/Data Modelling/index|Data Modelling]]

### The Principle: Don't Mix "Who" with "Where"
In many environmental projects, stakeholder data is collected haphazardly. A common mistake is treating a database cell like a postal label.
* **The Mistake:** Lumping the person's name, the "Care of" (C/O), and the street address into a single column.
* **The Consequence:**
    * **Geocoding fails:** The GIS cannot find a coordinate for "Farmer Jensen".
    * **Mail Merge fails:** You cannot write "Dear Mr. Jensen" automatically.
    * **Sorting fails:** You cannot group stakeholders by city or street.

---

### ⚠️ The "No Newline" Rule
**Never use `Alt+Enter` (Line Breaks) within a single Excel cell.**
While this looks nice on a printed sheet, it breaks almost every data processing tool (GIS, Python, SQL). A line break is often interpreted by software as "End of Row," causing your dataset to scramble or truncate during import.

* **Bad:**
  `Søren Jensen [Line Break] Markvejen 1`
* **Good:**
  `Søren Jensen` in Column A, `Markvejen 1` in Column B.

---

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

### A Note on Farmers: CVR vs. BBR
In agricultural projects, be aware of the "Accountant Trap":
* **CVR Address:** Often points to the farm's *accountant* or a holding company in the city. Good for legal notices.
* **BBR/Matrikel Address:** Points to the *physical farmhouse*. Good for field work and environmental analysis.
* **Best Practice:** Maintain two sets of columns: `Legal_Address` and `Site_Address`.