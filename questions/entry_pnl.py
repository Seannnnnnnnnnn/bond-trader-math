from questions import register_question_type
import random

def entry_pnl():
    
    side = random.choice(["Bid", "Offer"])
    size = round(random.uniform(0.5, 50), 2)
    mid_yield = round(random.uniform(0, 9), 4)
    distance_from_mid = random.choice([-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])

    bond_bpv = round(random.uniform(450, 1500), 2)
    quoted_yield = mid_yield + distance_from_mid

    # calculate PnL
    bps = abs(distance_from_mid)
    pnl = bond_bpv * bps * size

    if (side == "Bid" and quoted_yield < mid_yield) or (side == "Offer" and quoted_yield > mid_yield): 
        pnl *= -1

    pnl = round(pnl)

    return {
        "question": f"A client is looking for you {side} in a bond with a mid-yield of {mid_yield}. You have quoted {quoted_yield}. What is your entry PnL? (answer to nearest $).",
        "answer": pnl,
        "type": "numeric",
        "tolerance": 0.00025  # 0.25 bps
    }

register_question_type("entry_pnl", entry_pnl)
