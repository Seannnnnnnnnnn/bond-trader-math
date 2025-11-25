from questions import register_question_type
import random

def generate_efp():
    
    price = round(random.uniform(90, 100), 2)
    bond_yield = round(random.uniform(0, 9), 2)
    contract = random.choice(["YM", "XM"])

    # calculate efp spread
    fut_yield = 100 - price

    efp = (fut_yield - bond_yield) * 100

    return {
        "question": f"The {contract} contract is trading at ${price}. A given bond is trading at a yield of {bond_yield}%. What is the EFP Spread?",
        "answer": efp,
        "type": "numeric",
        "tolerance": 0.00025  # 0.25 bps
    }

register_question_type("efp_spread", generate_efp)
