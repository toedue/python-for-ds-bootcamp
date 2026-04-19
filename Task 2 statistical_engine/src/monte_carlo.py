import random

def simulate_crashes(days: int) -> float:
    """
    Simulates daily server crashes.
    Each day has exactly 4.5% chance of crashing.
    Returns the simulated crash rate (between 0 and 1).
    """
    if days <= 0:
        raise ValueError("Number of days must be positive!")
    
    crashes = 0
    for _ in range(days):
        # random.random() returns a number between 0.0 and 1.0
        # So < 0.045 means 4.5% chance
        if random.random() < 0.045:
            crashes += 1
    
    return crashes / days   # crash rate = crashes / total days