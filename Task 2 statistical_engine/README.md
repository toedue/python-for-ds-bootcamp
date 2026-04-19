# Statistical Engineering & Simulation Project

## Project Overview
This project is a **pure-Python statistical engine** built from scratch without using any external libraries (only built-in Python modules like `math`, `random`, `json`, and `unittest`).

It includes:
- A `StatEngine` class that calculates mean, median, mode, variance, standard deviation, and detects outliers.
- A Monte Carlo simulation to demonstrate the **Law of Large Numbers** using a server crash probability scenario.
- Proper data cleaning, error handling, and unit tests.

The goal is to show strong understanding of statistical concepts and clean coding practices.

## Features
- Calculates **mean**, **median** (handles both odd and even length lists), and **mode** (supports multimodal and "all unique" case).
- Supports both **sample variance** (Bessel’s correction, divide by n-1) and **population variance** (divide by n).
- Outlier detection using standard deviations from the mean.
- Graceful handling of empty lists and mixed/invalid data types.
- Monte Carlo simulation showing how larger sample sizes give results closer to the true probability (4.5% server crash rate).
- Salary dataset.

## Folder Structure
```
statistical_engine/
├── data/
│   └── sample_salaries.json          # 50 salary values
├── src/
│   ├── __init__.py
│   ├── stat_engine.py                # Main StatEngine class
│   └── monte_carlo.py                # Server crash simulation
├── tests/
│   ├── __init__.py
│   └── test_stat_engine.py             # Unit tests using unittest
├── main.py                           # Entry point to run analysis + simulation
└── README.md
```

## Mathematical Logic Explained
- **Mean**: Sum of all values divided by count.
- **Median**: 
  - Odd number of values → middle value after sorting.
  - Even number of values → average of the two middle values.
- **Variance**:
  - Population variance: Divide by `n`.
  - Sample variance: Divide by `n-1` (Bessel’s correction – more accurate for samples).
- **Standard Deviation**: Square root of variance.
- **Outliers**: Values more than 2 standard deviations away from the mean.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/statistical_engine.git
   cd statistical_engine
   ```
2. Run the main program:
   ```bash
   python main.py
   ```

## How to Run Tests
```bash
python -m unittest tests.test_stat_engine -v
```

## Example Output (when you run `python main.py`)
```
=== Simple Startup Salary Analysis ===

Number of salaries: 50
Mean Salary     : $74,500
Median Salary   : $74,500
Mode            : No unique mode: all values are unique
Std Deviation   : $14,577

Outliers detected: 0

=== Server Crash Simulation (Law of Large Numbers) ===

After    30 days  →  Crash rate =  6.67%
After  1000 days  →  Crash rate =  3.90%
After 10000 days  →  Crash rate =  4.12%
```

## Law of Large Numbers Explanation
The server has a true crash probability of **exactly 4.5%** each day.

- With a small sample (30 days), the simulated crash rate can be quite far from 4.5% (e.g. 6.67%).
- With a large sample (10,000 days), the crash rate gets much closer to the true 4.5%.

**Why this matters for the startup**:  
Relying on a short 30-day dataset to predict yearly maintenance budget is dangerous. The result can be misleading. Larger datasets give more reliable predictions.


## Technologies Used
- Python 3 (Standard Library only)
- `math`, `random`, `json`, `collections`, `unittest`, `os`

## Author
Abdulkadir
