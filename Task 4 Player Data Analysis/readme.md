# FIFA 2019 Player Data Analysis

A data science project that analyses **18,207 FIFA 2019 players** using 7 advanced analytical techniques to find real, actionable insights about the football transfer market.

---

## Project Overview

Imagine you work as a data analyst for a football club. Your boss hands you one file — `fifa_data.csv` — and says: *"Find me value. Who should we sign? Who is overpaid? Where is the hidden opportunity?"*

This project answers all of those questions using Python, pandas, matplotlib, and seaborn.

---

## Dataset

| Property | Value |
|---|---|
| File | `fifa_data.csv` |
| Rows | 18,207 players |
| Columns | 88 |
| Source | FIFA 19 ratings database |

**Key columns used:**
- `Name`, `Age`, `Nationality`, `Club`
- `Overall` — current ability rating (1–99)
- `Potential` — maximum possible rating (1–99)
- `Value` — market value (stored as string e.g. `€110.5M`)
- `Wage` — weekly wage (stored as string e.g. `€565K`)
- `Position` — specific position code (GK, CB, CM, ST…)
- `Preferred Foot` — Left or Right
- `International Reputation` — scale 1–5
- `Release Clause` — buyout clause value

---

## Setup

**Requirements:**
```
python 3.8+
pandas
numpy
matplotlib
seaborn
```

**Install dependencies:**
```bash
pip install pandas numpy matplotlib seaborn
```

**Run the notebook:**
```bash
jupyter notebook fifa_analysis.ipynb
```

Or run the script directly:
```bash
python fifa_analysis.py
```

---

## Project Structure

```
fifa-2019-analysis/
│
├── fifa_data.csv               ← the raw dataset
├── fifa_analysis.ipynb         ← main Jupyter notebook (with charts)
├── fifa_analysis.py            ← plain Python script version
├── README.md                   ← this file
│
└── outputs/
    ├── T1_cross_tabulation.png
    ├── T2_correlation_analysis.png
    ├── T3_percentile_analysis.png
    ├── T4_cohort_analysis.png
    ├── T5_outlier_investigation.png
    ├── T6_ratio_derived_metrics.png
    ├── T7_missing_data_patterns.png
    └── T0_summary_dashboard.png
```

---

## Data Cleaning

Before any analysis, three things had to be fixed:

**1. Money columns stored as strings**

The `Value` and `Wage` columns look like `€110.5M` — text, not numbers. Python cannot do maths on text. We wrote a `parse_money()` function to convert them:

```python
def parse_money(val):
    if pd.isna(val) or val == '0':
        return 0
    val = str(val).replace('€', '').strip()
    if val.endswith('M'):
        return float(val[:-1]) * 1_000_000
    elif val.endswith('K'):
        return float(val[:-1]) * 1_000
    return 0

df['Value_num'] = df['Value'].apply(parse_money)
df['Wage_num']  = df['Wage'].apply(parse_money)
```

**2. Position codes simplified**

The dataset has 27 different position codes (GK, CB, LCB, RCB, CDM…). We grouped them into 4 simple categories using a dictionary lookup:

```python
pos_map = {
    'GK': 'Goalkeeper',
    'CB': 'Defender', 'LCB': 'Defender', 'RWB': 'Defender', ...
    'CM': 'Midfielder', 'CAM': 'Midfielder', 'CDM': 'Midfielder', ...
    'ST': 'Forward', 'LW': 'Forward', 'CF': 'Forward', ...
}
df['Position_Group'] = df['Position'].map(pos_map)
```

**3. New derived columns created**

```python
df['Age_Group']     = pd.cut(df['Age'], bins=[0,21,25,29,33,50], labels=[...])
df['Potential_Gap'] = df['Potential'] - df['Overall']
df['Value_to_Wage'] = df['Value_num'] / df['Wage_num'].replace(0, 1)
df['RC_missing']    = df['RC_num'].apply(lambda x: 1 if x == 0 else 0)
```

---

## The 7 Techniques

### Technique 7 — Missing Data Patterns

**Question asked:** Is missing data random, or does it tell us something?

**What we did:**
```python
missing_pct = (df.isnull().mean() * 100).round(1)

rc_comparison = df.groupby('RC_missing')[['Overall', 'Value_num', 'Wage_num']].mean()
```

**The math:**
```
Players missing Release Clause = 1,564
1,564 ÷ 18,207 × 100 = 8.59% missing

isnull() marks True (missing=1) or False (present=0)
.mean() of those 1s and 0s = fraction missing
× 100 = percentage
```

**What we found:**

| Group | Avg Overall | Avg Value | Avg Wage/wk |
|---|---|---|---|
| RC Present | 66.2 | €2.44M | €9.6K |
| RC Missing | 67.3 | €2.14M | €11.3K |

**Insight:** Missing Release Clause is NOT random. These players earn more per week but are worth less overall — they are on short-term deals. The club pays them now but has made no long-term commitment. In a predictive model, `RC_missing = 1` is a useful feature flag.

---

### Technique 6 — Ratio and Derived Metrics

**Question asked:** What efficiency columns can we create that the raw data does not already have?

**What we did:**
```python
# Potential Gap — how much room to grow?
df['Potential_Gap'] = df['Potential'] - df['Overall']

# Value-to-Wage — how much market value per euro of wage?
df['Value_to_Wage'] = df['Value_num'] / df['Wage_num'].replace(0, 1)

# Young gems filter
young_gems = df[
    (df['Age'] <= 23) &
    (df['Potential_Gap'] >= 8) &
    (df['Wage_num'] < 30_000)
]

# Median ratio by position
vw_by_pos = df.groupby('Position_Group')['Value_to_Wage'].median()
```

**The math (worked example):**
```
Player earns €10,000/week, worth €2,500,000 on market.

Value-to-Wage = 2,500,000 ÷ 10,000 = 250×

The club gets 250 euros of market value per 1 euro of wage paid.
```

**Results by position:**

| Position | Value-to-Wage Ratio |
|---|---|
| Forward | 250× |
| Midfielder | 222× |
| Defender | 200× |
| Goalkeeper | 177× |

**Insight:** Forwards give clubs the most market value per euro of salary. Players aged ≤23 with a Potential Gap ≥8 and wage under €30K/week are the best return on investment of all — young, cheap, and still improving.

---

### Technique 4 — Cohort Analysis

**Question asked:** Do different age groups behave differently from each other?

**What we did:**
```python
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[0, 21, 25, 29, 33, 50],
    labels=['Teen (≤21)', 'Young (22-25)', 'Peak (26-29)', 'Senior (30-33)', 'Veteran (34+)']
)

cohort = df.groupby('Age_Group', observed=True).agg(
    Players      = ('Overall',   'count'),
    Avg_Overall  = ('Overall',   'mean'),
    Avg_Value_M  = ('Value_num', lambda x: x.mean() / 1_000_000),
    Avg_Wage_K   = ('Wage_num',  lambda x: x.mean() / 1_000),
    Potential_Gap = ('Potential_Gap', 'mean')
).round(2)

vw_cohort = df[df['Wage_num'] > 0].groupby('Age_Group', observed=True)['Value_to_Wage'].median()
```

**The math (worked example):**
```
Young (22-25) group example player:
Value = €2,800,000 / Wage = €9,400/week
Ratio = 2,800,000 ÷ 9,400 = 297.9

Median of ALL ratios in the group = 262×
```

**Results:**

| Age Group | Players | Avg Overall | Avg Value | Avg Wage/wk | Value-to-Wage |
|---|---|---|---|---|---|
| Teen (≤21) | 4,738 | 60.8 | €1.16M | €4.2K | 190× |
| Young (22-25) | 5,328 | 66.7 | €2.79M | €9.4K | **262× ★** |
| Peak (26-29) | 4,593 | 69.0 | €3.32M | €13.6K | 222× |
| Senior (30-33) | 2,599 | 69.7 | €2.86M | €14.3K | 177× |
| Veteran (34+) | 889 | 68.7 | €0.93M | €8.4K | 75× |

**Insight:** The Young (22-25) cohort is the sweet spot — good skill, low wages, highest value-to-wage ratio of 262×. Veteran players (34+) drop to just 75× — they cost nearly as much in wages but their market value is collapsing.

---

### Technique 3 — Percentile Analysis

**Question asked:** What does the real distribution look like, not just the average?

**What we did:**
```python
# Overall rating percentiles
for p in [10, 25, 50, 75, 90, 95, 99]:
    val = df['Overall'].quantile(p / 100)
    print(f'P{p}: {val}')

# Wage inequality
top5        = df.nlargest(int(len(df) * 0.05), 'Wage_num')
top5_wages  = top5['Wage_num'].sum()
total_wages = df['Wage_num'].sum()
share       = top5_wages / total_wages * 100
```

**The math:**
```
How .quantile() works:
Sort all 18,207 Overall values from lowest to highest.

P50  → position = 0.50 × 18,207 = 9,104th value  = 66
P90  → position = 0.90 × 18,207 = 16,386th value = 75
P95  → position = 0.95 × 18,207 = 17,297th value = 77

Wage inequality:
5% of players  = 0.05 × 18,207  = 910 players
Top 910 wages  ÷  all wages × 100  = 41.1%
Gap: €39,000 ÷ €3,000 = 13× between P95 and median
```

**Results:**

| Percentile | Overall Rating | Weekly Wage |
|---|---|---|
| P10 | 57 | — |
| P50 (median) | 66 | €3,000 |
| P75 | 71 | €9,000 |
| P90 | 75 | €23,000 |
| P95 | 77 | €39,000 |
| P99 | 83 | €105,000 |

**Insight:** The mean wage (€12K/week) describes nobody accurately. The median is €3K/week. The top 5% of earners consume 41% of all wages. Messi earns €565K/week — 188× the median player. A player rated 80 Overall is not "slightly above average" — they are in the top 5% of all professionals in the world.

---

### Technique 2 — Correlation Analysis

**Question asked:** Which variables are linked — and how strongly?

**What we did:**
```python
cols = ['Overall', 'Potential', 'Age', 'Value_num', 'Wage_num',
        'International Reputation', 'Skill Moves', 'Potential_Gap']

corr_matrix = df[cols].corr()
overall_corr = corr_matrix['Overall'].drop('Overall').sort_values(ascending=False)

# Youth premium — controlled experiment
same_skill = df[(df['Overall'] >= 83) & (df['Overall'] <= 87)]
young_val  = same_skill[same_skill['Age'] <= 25]['Value_num'].mean() / 1_000_000
senior_val = same_skill[same_skill['Age'] >= 30]['Value_num'].mean() / 1_000_000
```

**The math:**
```
Pearson r formula:
r = Σ((x − x̄)(y − ȳ)) / (n × σx × σy)

r = +1.0  →  perfect positive link
r =  0.0  →  no relationship at all
r = −1.0  →  perfect negative link

Youth premium calculation:
Filter: players rated 83–87 Overall (skill held constant)
Young (≤25): avg value = €40.0M
Senior (≥30): avg value = €23.0M

Ratio = 40.0 ÷ 23.0 = 1.74×
Age alone adds 74% extra value at identical skill.
```

**Correlations with Overall rating:**

| Variable | r value | Direction |
|---|---|---|
| Potential | +0.661 | Positive |
| Market Value | +0.627 | Positive |
| Wage | +0.572 | Positive |
| International Reputation | +0.500 | Positive |
| Age | +0.453 | Positive |
| Skill Moves | +0.414 | Positive |
| Potential Gap | −0.528 | Negative |

**Insight:** At identical skill (83–87 Overall), players aged ≤25 are worth 1.74× more than players aged ≥30. Clubs are not just buying current ability — they are buying future years of performance.

---

### Technique 1 — Cross-Tabulation Analysis

**Question asked:** What patterns appear when we look at two categories at the same time?

**What we did:**
```python
# Preferred foot by position (as percentages)
foot_pos = pd.crosstab(
    df['Position_Group'],
    df['Preferred Foot'],
    normalize='index'
) * 100

# Average Overall by reputation and position
rep_pos = pd.crosstab(
    df['International Reputation'].astype(int),
    df['Position_Group'],
    values=df['Overall'],
    aggfunc='mean'
).round(1)

# Left vs right foot market value for forwards
lf_value = df[df['Position_Group'] == 'Forward'].groupby('Preferred Foot')['Value_num'].median() / 1_000_000
```

**The math:**
```
normalize='index' converts raw counts to row percentages:

Without normalize: Forward | Left=790  | Right=3,738
With normalize:    Forward | Left=17.4% | Right=82.6%
Every row adds up to 100%.

Scarcity premium:
Left-footed forwards:  median value = €1.50M
Right-footed forwards: median value = €1.20M

Premium = (1.50 − 1.20) ÷ 1.20 × 100 = 25%
```

**Preferred foot by position:**

| Position | Left % | Right % |
|---|---|---|
| Goalkeeper | 10.2% | 89.8% |
| Defender | 32.1% | 67.9% |
| Midfielder | 22.3% | 77.7% |
| Forward | 17.4% | 82.6% |

**Insight:** Only 17.4% of forwards are left-footed. But left-footed forwards command a 25% higher median market value than right-footed ones at the same skill level. Defenders train all week against right-footers — a left-footer attacks from angles they are not used to. Scarcity creates a tactical advantage which creates a price premium.

---

### Technique 5 — Outlier Investigation

**Question asked:** Are extreme values mistakes, or the most important finding?

**What we did:**
```python
# IQR method
Q1  = df['Wage_num'].quantile(0.25)
Q3  = df['Wage_num'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

wage_outliers  = df[df['Wage_num'] >  upper_limit]
normal_players = df[df['Wage_num'] <= upper_limit]

# Compare the two groups
compare = pd.DataFrame({
    'Normal':  normal_players[['Overall', 'Potential', 'International Reputation']].mean(),
    'Outlier': wage_outliers[['Overall',  'Potential', 'International Reputation']].mean()
}).round(2)
```

**The math step by step:**
```
Q1  =  €3,000/week   (25th percentile)
Q3  =  €9,000/week   (75th percentile)
IQR =  €9,000 − €3,000  =  €6,000

upper_limit  =  €9,000 + (1.5 × €6,000)
             =  €9,000 + €9,000
             =  €18,000/week

Players earning above €18,000/week = wage outliers.

Wage share calculation:
Outliers = 2,038 ÷ 18,207 = 11.2% of players
Their wages = 59.1% of total wage bill
```

**Results:**

| Metric | Normal Players | Wage Outliers | Difference |
|---|---|---|---|
| Count | 16,109 (88.8%) | 2,038 (11.2%) | — |
| Avg Overall | 64.9 | 76.9 | +12.0 points |
| Avg Potential | 68.5 | 80.1 | +11.6 points |
| Int. Reputation | 1.1 | 2.8 | +1.7 levels |
| Share of wages | 40.9% | 59.1% | 11% take 59% of money |

**Insight:** Wage outliers are NOT data errors. They average Overall 76.9 vs 64.9 for normal players — a gap of 12 full rating points. They are a genuinely separate market segment: the VIP tier of professional football. Deleting them would have destroyed the most interesting part of the dataset.

---

## The 5 Key Insights

| # | Insight | Techniques Used |
|---|---|---|
| 1 | Top 5% of earners consume 41% of all wages. Median player earns €3K/wk — 13× less than P95. | T3 + T5 |
| 2 | At the same skill level, players aged ≤25 are worth 1.74× more than players aged ≥30. | T2 + T4 |
| 3 | Left-footed forwards are only 17% of all forwards but command 25% higher median market value. | T1 |
| 4 | Missing Release Clause is not random — it flags players on short contracts with no long-term value. | T7 |
| 5 | Young gems (age ≤23, potential gap ≥8, wage <€30K) have the highest value-to-wage ratio of all. | T6 |

---

## What a Club Should Actually Do

Based on the analysis:

1. **Target the 22–25 age bracket** — best value-to-wage ratio (262×), proven skill, still affordable wages.
2. **Use the young gems filter** — Age ≤23 AND Potential Gap ≥8 AND Wage <€30K/week finds hidden stars before they get expensive.
3. **Scout left-footed youth forwards early** — they are rare (17%), carry a 25% price premium, and are cheapest before they reach the top level.
4. **Sell veteran stars before age 30** — market value drops sharply after 30. Sell while value is high, reinvest in youth.
5. **Do not compete on wages alone** — the top 5% take 41% of all wages. A budget club cannot win a wage war. Win with smarter analytics instead.

---

## Charts Generated

Each technique produces a chart that visualises the finding:

| File | What it shows |
|---|---|
| `T0_summary_dashboard.png` | All 5 insights in one overview |
| `T1_cross_tabulation.png` | Foot preference by position, value comparison |
| `T2_correlation_analysis.png` | Heatmap and bar chart of correlations |
| `T3_percentile_analysis.png` | Rating and wage distributions with percentile lines |
| `T4_cohort_analysis.png` | 4-panel age group breakdown |
| `T5_outlier_investigation.png` | Box plot, skill comparison, nationality breakdown |
| `T6_ratio_derived_metrics.png` | Potential gap distribution, value-to-wage by position |
| `T7_missing_data_patterns.png` | Missing % bar chart, RC present vs missing comparison |

---

## Key Python Concepts Used

| Concept | Where it appears |
|---|---|
| `pd.read_csv()` | Loading the dataset |
| `.apply(lambda x: ...)` | Cleaning money columns, flagging missing RC |
| `.map(dictionary)` | Converting position codes to groups |
| `pd.cut()` | Creating age buckets |
| `.groupby().agg()` | Calculating cohort statistics |
| `.quantile()` | Finding percentiles |
| `.corr()` | Building the correlation matrix |
| `pd.crosstab()` | Cross-tabulation with normalize |
| `.isnull().mean()` | Measuring missing data percentage |
| `plt.subplots()` | Creating multi-panel charts |
| `sns.heatmap()` | Drawing the correlation heatmap |
| `sns.boxplot()` | Visualising distributions by group |

---
