"""
conflict_demo.py — File used to demonstrate merge conflicts.

INSTRUCTIONS FOR THE SPEAKER:

1. Start on 'main' with this file as-is.
2. Commit it: git add conflict_demo.py && git commit -m "Add greeting function"
3. Create branch-a: git switch -c branch-a
   - Change the greeting message to "Hello from Branch A!"
   - Commit: git commit -am "Update greeting in branch-a"
4. Switch back to main: git switch main
5. Create branch-b: git switch -c branch-b
   - Change the greeting message to "Hello from Branch B!"
   - Commit: git commit -am "Update greeting in branch-b"
6. Switch to main: git switch main
7. Merge branch-a: git merge branch-a  (succeeds — fast-forward)
8. Merge branch-b: git merge branch-b  (CONFLICT!)
9. Show the conflict markers in the file.
10. Resolve by choosing one version or combining both.
11. git add conflict_demo.py && git commit -m "Resolve merge conflict"
"""


def greet(name):
    """Greet a user with a message."""
    # ──────────────────────────────────────────────
    # EDIT THIS LINE on different branches to create
    # a merge conflict during the demo:
    message = "Hello, World!"
    # ──────────────────────────────────────────────
    return f"{message} Welcome, {name}!"


def farewell(name):
    """Say goodbye to a user."""
    return f"Goodbye, {name}! See you next time."


if __name__ == "__main__":
    print(greet("Seminar Participant"))
    print(farewell("Seminar Participant"))
