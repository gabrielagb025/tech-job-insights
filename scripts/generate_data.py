"""
Generate a synthetic dataset of tech job offers and save it as data/jobs.csv.

Usage (from the project root):
    python scripts/generate_data.py
"""


import random 
from pathlib import Path
import pandas as pd
from sample_data import (
    COMPANIES,
    COUNTRIES,
    EXTRA_SKILLS,
    LEVELS,
    ROLES,
    TECH_FACTOR,
    WORK_MODES
)

# Fixed seed: we get the same random data everytime we run the script
random.seed(42)

NUM_JOBS = 400


def generate_job():
    """Create one fake job offer as a dictionary."""
    # Weights make some options more likely than others (e.g. more Mid than Senior)
    technology = random.choice(list(ROLES.keys()))
    level = random.choices(list(LEVELS.keys()), weights=[35, 40, 25])[0]
    country = random.choice(list(COUNTRIES.keys()))
    work_mode = random.choices(WORK_MODES, weights=[45, 35, 20])[0]

    salary = (
        LEVELS[level]
        * COUNTRIES[country]
        * TECH_FACTOR[technology]
        * random.uniform(0.85, 1.15)
    )
    salary = max(30000, int(round(salary, -3)))  # round to the nearest 1000, minimum 30k

    stack = [technology] + random.sample(EXTRA_SKILLS, k=random.randint(2, 3))

    return {
        "Job Title": f"{level} {random.choice(ROLES[technology])}",
        "Company": random.choice(COMPANIES),
        "Country": country,
        "Salary (EUR)": salary,
        "Tech Stack": ", ".join(stack),
        "Work Mode": work_mode,
        "Experience Level": level,
        "Main Technology": technology,
    }


# Generate all the job offers and turn them into a pandas table
jobs = [generate_job() for _ in range(NUM_JOBS)]
df = pd.DataFrame(jobs)

# Save the table as a CSV in the data/ folder, at the project root
BASE_DIR = Path(__file__).resolve().parent.parent
output_path = BASE_DIR / "data" / "jobs.csv"
output_path.parent.mkdir(exist_ok=True)
df.to_csv(output_path, index=False)

print(df.head())
print(f"Saved {len(df)} job offers to {output_path}")