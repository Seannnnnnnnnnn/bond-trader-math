from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
from questions import choose_random_question

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"
app.permanent_session_lifetime = timedelta(days=7)

# ---------------------------
# Helper: grade answers
# ---------------------------

def grade_answer(qdata, user_answer):
    """
    qdata = {
        "question": str,
        "answer": any,
        "type": "numeric" or "multiple_choice",
        "choices": optional list,
        "tolerance": optional float (bps)
    }
    """

    correct = qdata["answer"]

    # MULTIPLE CHOICE
    if qdata["type"] == "multiple_choice":
        return str(user_answer).strip() == str(correct).strip()

    # NUMERIC
    try:
        user_val = float(str(user_answer).replace(",", "").strip())
        correct_val = float(correct)

        tol = qdata.get("tolerance", 0.0001)  # default = small tolerance
        return abs(user_val - correct_val) <= tol

    except Exception:
        return False


# ---------------------------
# Routes
# ---------------------------

@app.route("/")
def index():
    # Reset score if not present
    if "score" not in session:
        session["score"] = 0
        session["attempts"] = 0

    # Generate a new question
    qdata = choose_random_question()
    session["current_question"] = qdata
    return render_template("index.html", question=qdata["question"],
                           qtype=qdata["type"],
                           choices=qdata.get("choices", None))


@app.route("/submit", methods=["POST"])
def submit():
    user_answer = request.form.get("answer", "").strip()
    qdata = session.get("current_question")

    if not qdata:
        return redirect(url_for("index"))

    is_correct = grade_answer(qdata, user_answer)

    session["attempts"] += 1
    if is_correct:
        session["score"] += 1

    feedback = "Correct!" if is_correct else f"Incorrect. Correct answer was {qdata['answer']}."

    # Prepare next question
    next_q = choose_random_question()
    session["current_question"] = next_q

    return render_template(
        "index.html",
        question=next_q["question"],
        qtype=next_q["type"],
        choices=next_q.get("choices", None),
        feedback=feedback,
        score=session["score"],
        attempts=session["attempts"]
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
