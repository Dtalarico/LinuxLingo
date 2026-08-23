import random
import subprocess

drills = [
    {
        "task": "Create a directory named workspace",
        "check": "test -d workspace",
        "solution": "mkdir workspace"
    },
    {
        "task": "Create a file named notes.txt",
        "check": "test -f notes.txt",
        "solution": "touch notes.txt"
    },
    {
        "task": "Create a directory named project inside ~/workspace",
        "check": "test -d ~/workspace/project",
        "solution": "mkdir ~/workspace/project"
    },
    {
        "task": "Create a file called log.txt inside workspace",
        "check": "test -f workspace/log.txt",
        "solution": "touch workspace/log.txt"
    },
    {
        "task": "Create two directories inside project named data and logs",
        "check": "test -d project/data && test -d project/logs",
        "solution": "mkdir -p project/{data,logs}"
    }
]

score = 0
attempts = 0

print("\nWelcome to LinuxLingo MVP\n")
print("Type 'exit' anytime to quit.\n")

while True:
    drill = random.choice(drills)

    print("\nTASK:")
    print(drill["task"])

    user_input = input("\nEnter command: ")

    if user_input.strip() == "exit":
        break

    try:
        subprocess.run(user_input, shell=True)
    except Exception:
        pass

    check = subprocess.run(drill["check"], shell=True)

    attempts += 1

    if check.returncode == 0:
        score += 1
        print("\nPASS")
    else:
        print("\nFAIL")
        print("Expected command example:")
        print(drill["solution"])

    print(f"\nScore: {score}/{attempts}")
