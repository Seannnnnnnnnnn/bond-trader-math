import random

# GLOBAL REGISTRY FOR QUESTION TYPES
QUESTION_TYPES = {}

def register_question_type(name: str, generator_func):
    """
    Register a question generator function under a given name.
    - name: string identifier for the question type
    - generator_func: function that returns
        {
          "question": str,
          "answer": any,
          "type": "numeric" or "multiple_choice",
          "choices": optional list
        }
    """
    QUESTION_TYPES[name] = generator_func


def choose_random_question():
    """
    Randomly select one registered question type and produce a question dict.
    """
    if not QUESTION_TYPES:
        raise ValueError("No question types registered.")

    name = random.choice(list(QUESTION_TYPES.keys()))
    generator = QUESTION_TYPES[name]
    return generator()

# -------------------------
# EXPLICIT MODULE IMPORTS
# -------------------------
# Every question file should import itself here
from . import efp_spread
from . import implied_yield
