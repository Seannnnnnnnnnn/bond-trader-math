def grade_answer(question, user_input):
    qtype = question["type"]

    if qtype == "futures_implied_yield":
        return grade_futures_implied_yield(question, user_input)

    if qtype == "bond_efp":
        return grade_bond_efp(question, user_input)

    if qtype == "dv01_hedge":
        return grade_dv01_hedge(question, user_input)

    return False, "Unknown question type."


def grade_futures_implied_yield(q, user_input):
    try:
        user_val = float(user_input)
    except:
        return False, "Please enter a valid number."

    true_val = q["true_yield"]
    if abs(user_val - true_val) <= 0.01:  # ±1 bp
        return True, f"Correct! True yield = {true_val:.2f}%."
    else:
        return False, f"Wrong. True yield = {true_val:.2f}%."


def grade_bond_efp(q, user_input):
    try:
        user_val = float(user_input)
    except:
        return False, "Please enter a valid number."

    true_val = q["efp"]
    if abs(user_val - true_val) <= 0.25:  # ±0.25 bp
        return True, f"Correct! EFP = {true_val:.2f} bps."
    else:
        return False, f"Incorrect. EFP = {true_val:.2f} bps."


def grade_dv01_hedge(q, user_input):
    # exact string match against one of the multiple-choice options
    correct_contracts = round(q["hedge_contracts"])
    correct_side = q["correct_side"]

    correct_text = f"{correct_side.capitalize()} {correct_contracts} futures"

    if user_input.lower() == correct_text.lower():
        return True, f"Correct! You should: {correct_text}"
    else:
        return False, f"Wrong. Correct answer is: {correct_text}"
