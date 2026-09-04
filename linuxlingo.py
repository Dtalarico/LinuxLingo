import json
import random
from pathlib import Path

BANK_PATH = Path(__file__).with_name("scenario_bank.json")


def load_drills():
    with BANK_PATH.open("r", encoding="utf-8") as handle:
        drills = json.load(handle)

    if not isinstance(drills, list):
        raise ValueError("scenario_bank.json must contain a top-level JSON list.")

    required = {"id", "prompt", "answers"}
    usable = []

    for drill in drills:
        if not isinstance(drill, dict):
            continue
        if not required.issubset(drill):
            continue
        if not isinstance(drill["answers"], list) or not drill["answers"]:
            continue
        usable.append(drill)

    if not usable:
        raise ValueError("No usable drills were found in scenario_bank.json.")

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
    print(f"Loaded {len(drills)} drills from scenario_bank.json.")
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
