import os
import time

# Path to your repo
repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1503-Python-Application-Programming"

while True:
    os.chdir(repo_path)
    os.system("git add .")
    os.system('git commit -m "experiment_3_distance.py"')
    os.system("git push origin main")
    print("✅ Code auto pushed to GitHub!")
    time.sleep(19) 