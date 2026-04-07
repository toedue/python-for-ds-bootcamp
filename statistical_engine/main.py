import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def main():
    print("=== Simple Startup Salary Analysis ===\n")

    # 1. Load the salary data
    with open("data/sample_salaries.json", "r") as f:
        salaries = json.load(f)

    # 2. Create the calculator
    engine = StatEngine(salaries)

    # 3. Show the results
    print("Number of salaries:", len(salaries))
    print("Mean Salary     :", engine.getmean())
    print("Median Salary   :", engine.getmedian())
    print("Mode            :", engine.get_mode())
    print("Standard Deviation :", engine.getstandarddeviation(is_sample=True))

    # 4. Show outliers
    outliers = engine.get_outliers(threshold=2)
    print("\nOutliers found:", len(outliers))
    if outliers:
        print("Outlier salaries:", outliers)

    # 5. Server crash simulation
    print("\n=== Server Crash Simulation (Law of Large Numbers) ===\n")

    for days in [30, 1000, 10000]:
        prob = simulate_crashes(days)
        print("After", days, "days → Crash rate =", round(prob*100, 2), "%")

if __name__ == "__main__":
    main()