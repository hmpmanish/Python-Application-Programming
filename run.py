import subprocess
import time
import datetime

GIT = r"C:\Program Files\Git\bin\git.exe"

def run_cmd(command):
    result = subprocess.run(
        command,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip(), result.stderr.strip()

print("🔁 Auto Git Commit Script Started (Every 5 Minutes)")
print("⏳ Press CTRL + C to stop\n")

while True:
    status, err = run_cmd([GIT, "status", "--porcelain"])

    if status:
        run_cmd([GIT, "add", "."])

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"Auto commit at {now}"

        run_cmd([GIT, "commit", "-m", msg])
        run_cmd([GIT, "push"])

        print(f"✅ Changes committed & pushed at {now}")
    else:
        print("ℹ No changes detected")

    time.sleep(300)
