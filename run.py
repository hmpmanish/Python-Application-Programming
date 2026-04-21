import subprocess
import os
import time

repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1503-Python-Application-Programming"

def run_git(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

os.chdir(repo_path)

while True:
    try:
        # Stage changes
        run_git(["git", "add", "."])

        # Check changes
        code, status, _ = run_git(["git", "status", "--porcelain"])

        if status:
            print("🔄 Changes detected...")

            run_git(["git", "commit", "-m", f"Auto backup - {time.strftime('%Y-%m-%d %H:%M:%S')}"])

            # Try push
            code, out, err = run_git(["git", "push"])

            if code == 0:
                print("✅ Pushed successfully!")

            else:
                print("⚠️ Push failed, pulling updates...")

                # Try pulling (NO rebase → safer)
                code, out, err = run_git(["git", "pull", "--no-rebase"])

                if "CONFLICT" in out or "CONFLICT" in err:
                    print("❌ Merge conflict detected! Resolve manually.")
                    break  # stop script

                # Try push again
                code, out, err = run_git(["git", "push"])

                if code == 0:
                    print("✅ Synced after pull!")
                else:
                    print("❌ Still failed. Check manually.")
                    break

        else:
            print("🟡 No changes.")

    except Exception as e:
        print(f"❌ Error: {e}")
        break

    time.sleep(60)