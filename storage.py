import json, os

def load_sent():
    if os.path.exists("sent.json"):
        return set(json.load(open("sent.json")))
    return set()

def save_sent(s):
    with open("sent.json", "w") as f:
        json.dump(list(s), f)
