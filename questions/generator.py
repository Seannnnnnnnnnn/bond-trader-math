import random
from .templates import FuturesImpliedYield, BondEFP, DV01Hedge

TEMPLATES = [
    FuturesImpliedYield,
    BondEFP,
    DV01Hedge
]

def generate_question():
    template = random.choice(TEMPLATES)
    return template.generate()
