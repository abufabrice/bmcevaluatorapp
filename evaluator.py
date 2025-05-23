import random
import json

def load_rubric(path="rubric.json"):
    with open(path, "r") as f:
        return json.load(f)

def evaluate_bmc(text: str):
    rubric = load_rubric()
    scores = {section: random.randint(0, points) for section, points in rubric.items()}
    total = sum(scores.values())
    feedback = {k: f"Consider improving clarity in {k.lower()}." for k in scores}
    return total, scores, feedback
