import os
from datetime import datetime

# Git repo path
repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1503-Python-Application-Programming"

# Change working directory to repo
os.chdir(repo_path)

# Check for changes
status = os.popen("git status --porcelain").read()

if status.strip():  # Only commit if there are changes
    os.system("git add .")
    commit_msg = f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    os.system(f'git commit -m "{commit_msg}"')
    os.system("git push origin main")
    print(f"✅ Changes committed & pushed at {datetime.now().strftime('%H:%M:%S')}")
else:
    print(f"ℹ No changes detected at {datetime.now().strftime('%H:%M:%S')}")
