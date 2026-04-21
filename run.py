import subprocess
import os
import time

repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1503-Python-Application-Programming"

def run_git_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

os.chdir(repo_path)

while True:
    try:
        # Stage changes
        run_git_command(["git", "add", "."])

        # Check status
        status, _ = run_git_command(["git", "status", "--porcelain"])

        if status:
            print("🔄 Changes detected, committing...")

            run_git_command(["git", "commit", "-m", "Auto commit by script"])
            run_git_command(["git", "push"])

            print("✅ Changes pushed successfully!")
        else:
            print("🟡 No changes.")

    except Exception as e:
        print(f"❌ Error: {e}")

    time.sleep(60)  # increased delay