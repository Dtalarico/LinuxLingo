import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).parent
BANK_PATHS = [
    BASE_DIR / "scenario_bank.json",
    BASE_DIR / "scenario_bank_2.json",
]


def load_drills():
    combined = []

    for bank_path in BANK_PATHS:
        if not bank_path.exists():
            continue

        with bank_path.open("r", encoding="utf-8") as handle:
            drills = json.load(handle)

        if not isinstance(drills, list):
            raise ValueError(f"{bank_path.name} must contain a top-level JSON list.")

        combined.extend(drills)

    required = {"id", "prompt", "answers"}
    usable = []
    seen_ids = set()

    for drill in combined:
        if not isinstance(drill, dict):
            continue
        if not required.issubset(drill):
            continue
        if not isinstance(drill["answers"], list) or not drill["answers"]:
            continue
        if drill["id"] in seen_ids:
            raise ValueError(f"Duplicate drill id found: {drill['id']}")
        seen_ids.add(drill["id"])
        usable.append(drill)

    if not usable:
        raise ValueError("No usable drills were found in the configured scenario banks.")

    return usable


def normalize(text):
    """Normalize whitespace for answer comparison without changing command meaning."""
    return " ".join(text.strip().split())


def is_correct(user_input, answers):
    submitted = normalize(user_input)
    return any(submitted == normalize(answer) for answer in answers)


def main():
    drills = load_drills()
    score = 0
    attempts = 0

    print("\nWelcome to LinuxLingo MVP\n")
    print(f"Loaded {len(drills)} drills from configured scenario banks.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        drill = random.choice(drills)

        print(f"\n[{drill['id']}] {drill.get('category', 'uncategorized')} | {drill.get('difficulty', 'unrated')}")
        print("TASK:")
        print(drill["prompt"])

        user_input = input("\nEnter command or answer: ")

        if user_input.strip().lower() == "exit":
            break

        attempts += 1

        if is_correct(user_input, drill["answers"]):
            score += 1
            print("\nPASS")
        else:
            print("\nFAIL")
            print("Expected answer example:")
            print(drill["answers"][0])
            explanation = drill.get("explanation")
            if explanation:
                print(explanation)

        print(f"\nScore: {score}/{attempts}")


if __name__ == "__main__":
    main()
