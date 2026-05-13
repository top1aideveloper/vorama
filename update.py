# git_update.py
# Simple Git auto-update script
# Usage:
#   python git_update.py "your commit message"

import subprocess
import sys
from datetime import datetime

def run(cmd):
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True)
    
    if result.returncode != 0:
        print(f"\nCommand failed: {cmd}")
        sys.exit(1)

# Get commit message
if len(sys.argv) > 1:
    commit_message = " ".join(sys.argv[1:])
else:
    commit_message = f"update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

print("Starting Git update...")

# Git commands
run("git add .")
run(f'git commit -m "{commit_message}"')
run("git push")

print("\nDone! Changes pushed to GitHub.")