
# Task-3: Pandas Data Analysis (Custom & Titanic Datasets)


## Project Structure
```
├── Task 3 folder          # Jupyter Notebook containing all code & outputs
    ├── Part_1_Dataset.ipynb
    ├── Part_2_Titanic.ipynb
    ├── Titanic-Dataset.csv   # Dataset used for Part 2
    └── README.md             
```

---

## Project Objectives
* **Part 1:** Learn how to build a DataFrame manually using a Python dictionary and assign custom row indices.
* **Part 2:** Perform a complete End-to-End Data Analysis pipeline on the Titanic dataset:
  * Data Exploration (`.head()`, `.info()`, `.describe()`)
  * Data Cleaning (Handling missing values, dropping columns)
  * Data Analysis (Using `groupby()` for survival rates)
  * Data Filtering (Extracting specific subsets of passengers)
  * Deriving actionable Insights

---

## Part 1: Creating a Custom Dataset
* Created a dataset of 15 students with 5 features (`Name`, `Age`, `Subject`, `Score`, `Grade`).
* Built it using a Python dictionary (key-value pairs).
* Assigned custom string indices (`STU001` to `STU015`) instead of default numeric `0, 1, 2...` to make the data more readable.

---

##  Part 2: Titanic Data Cleaning Strategy
Real-world data is messy. Here is how the missing values were handled:
1. **Age (177 missing):** Filled with the **Median (28.0)** instead of the Mean. *Why?* Because extreme outliers (like an 80-year-old) artificially pull the average up. The median is immune to outliers.
2. **Embarked (2 missing):** Filled with the **Mode ('S')**. *Why?* Because 'S' (Southampton) was the most common boarding port.
3. **Cabin (687 missing):** **Dropped** entirely. *Why?* Over 77% of the data was missing. Filling it would mean making up data, which ruins analysis.
4. **Duplicates:** Checked and removed (Found: 0).

---

## Key Insights from the Titanic Data

After analyzing the data using `groupby()` and filtering, here are the answers to the core questions:

**1. Who was more likely to survive? (Gender)**
* **Females** had a significantly higher survival rate (~74%) compared to males (~19%). This proves the historical "Women and children first" protocol was followed during the evacuation.

**2. Did class affect survival?**
* **Yes, massively.** Your ticket class dictated your fate. 
  * 1st Class: ~63% survival
  * 2nd Class: ~47% survival
  * 3rd Class: ~24% survival
* 3rd class passengers were physically located at the bottom of the ship, farthest from the lifeboats.

**3. Were children prioritized?**
* **Yes.** Children (ages 0-12) had a ~58% survival rate, which is much higher than the ship's overall average of ~38%. 

**4. What combination had the highest survival rate?**
* **Females in 1st Class.** This specific group had a staggering **~96.8% survival rate**. Out of 94 women in 1st class, 91 survived. Being wealthy and female almost guaranteed survival on the Titanic.

---
