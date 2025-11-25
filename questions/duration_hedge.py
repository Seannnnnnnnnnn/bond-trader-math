from questions import register_question_type
import random
import math

def generate_duration_hedge():
    
    vol = round(random.uniform(0.5, 100), 2)
    fut_dv01  = round(random.uniform(83, 89), 2)
    bond_dv01 = round(random.uniform(450, 1500), 2)

    num_contracts = (vol * bond_dv01) / fut_dv01
    num_contracts = math.floor(num_contracts)

    return {
        "question": f"The XM contract has a DV01 of ${fut_dv01}. A client buys ${vol}m of a bond with BPV of ${bond_dv01}. How many XM contracts must be bought? (Nearest whole number)",
        "answer": num_contracts,
        "type": "numeric",
        "tolerance": 0.00025  # 0.25 bps
    }

register_question_type("duration_hedge", generate_duration_hedge)
