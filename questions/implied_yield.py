from questions import register_question_type
import random

def generate_implied_yield():
    # Generate the random price ONCE
    price = round(random.uniform(90, 100), 2)

    # Example logic: traded yield = 100 - price
    implied_yield = round(100 - price, 2)
    contract = random.choice(["XM", "YM"])

    return {
        "question": f"ASX {contract} Contract is ${price:.2f}. What is the implied yield?",
        "answer": implied_yield,
        "type": "numeric",
        "tolerance": 0.00025  # 0.25 bps
    }

register_question_type("implied_yield", generate_implied_yield)
