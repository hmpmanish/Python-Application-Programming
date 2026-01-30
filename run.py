import os
import time

# Path to your repo
repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1503-Python-Application-Programming"

while True:
    os.chdir(repo_path)
    os.system("git add .")
    os.system('git commit -m "experiment_4_positive_negative_zero.py added"')
    os.system("git push origin main")
    print("✅ Code auto pushed to GitHub!")
    time.sleep(300)  # Wait for 5 minutes before next push
# git add .
# git commit -m "experiment_5experiment_6_flip_binary_digit.py"
# git push origin main