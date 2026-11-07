import random 
from pathlib import Path

# Fixed seed: we get the same random data everytime we run the script
random.seed(42)

NUM_JOBS = 400

COMPANIES = [
    "Nova Labs", "Pixel Forge", "CloudNest", "DataWave", "Brightside Tech",
    "Orbit Systems", "Greenbyte", "Skyline Digital", "CodeCraft", "BlueRiver Software",
    "Quantum Apps", "Lumen Works", "Nimbus Cloud", "Atlas Software", "Helix Digital",
    "Northwind Tech", "Silverline Systems", "Cobalt Labs", "Vertex Digital", "Mapleleaf Software",
    "Redwood Apps", "Pulse Analytics", "Ironclad Tech", "Fjord Software", "Sunrise Cloud",
    "Zenith Labs", "Kiwi Code", "Stonebridge Digital", "Alpine Data", "Tidal Software",
    "Cedar Works", "Beacon Systems", "Falcon Apps", "Harbor Tech", "Ember Labs",
    "Juniper Digital", "Meridian Software", "Opal Cloud", "Summit Data", "Willow Tech",
    "Aurora Systems", "Birchwood Labs", "Crimson Code", "Driftwood Digital", "Echo Software",
    "Fernhill Tech", "Granite Apps", "Horizon Data", "Indigo Works", "Jetstream Cloud",
    "Kestrel Labs", "Lighthouse Digital", "Marble Systems", "Nebula Apps", "Oakridge Tech",
    "Paperboat Software", "Quartz Labs", "Riverstone Digital", "Saffron Cloud", "Thistle Tech",
    "Umbra Systems", "Velvet Code", "Wildflower Labs", "Xenon Software", "Yarrow Digital",
    "Zephyr Apps", "Amber Works", "Bluebell Tech", "Copperfield Data", "Dandelion Labs",
    "Evergreen Systems", "Foxglove Software", "Glacier Cloud", "Hazel Digital", "Ivory Apps",
    "Jasper Tech", "Kite Labs", "Larkspur Software", "Moonstone Data", "Nightfall Works",
]

# Salary multiplier per country (1.0 = baseline)
COUNTRIES = {
    "Spain": 0.90, "Germany": 1.10, "Netherlands": 1.15, "France": 1.00,
    "Portugal": 0.80, "Ireland": 1.15, "United Kingdom": 1.15, "United States": 1.35,
    "Canada": 1.15, "Poland": 0.85, "Sweden": 1.10, "Brazil": 0.75,
    "Mexico": 0.75, "India": 0.70, "Australia": 1.20,
}

# Base yearly salary in EUR for each experience level
LEVELS = {"Junior": 35000, "Mid": 55000, "Senior": 80000}

# Main technologies and the job titles that go with each one
ROLES = {
    "JavaScript": ["JavaScript Developer", "Frontend Developer", "Full Stack Developer"],
    "TypeScript": ["TypeScript Developer", "Full Stack Developer", "Frontend Engineer"],
    "Python": ["Python Developer", "Backend Developer", "Data Engineer"],
    "React": ["React Developer", "Frontend Developer", "Frontend Engineer"],
    "Node.js": ["Node.js Developer", "Backend Developer", "Full Stack Developer"],
}

# Small salary adjustment per main technology
TECH_FACTOR = {
    "JavaScript": 0.95, "TypeScript": 1.05, "Python": 1.05, "React": 1.00, "Node.js": 1.00,
}

EXTRA_SKILLS = ["SQL", "Docker", "AWS", "PostgreSQL", "Git", "MongoDB", "GraphQL", "Jest"]
WORK_MODES = ["Remote", "Hybrid", "On-site"]