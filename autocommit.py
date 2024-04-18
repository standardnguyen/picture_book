import time
import subprocess
from config import name_of_book
import os

def git_operations():
    filename = name_of_book  # Modify this path to the file you want to track
    commit_message = "Automated commit by script"

    while True:
        try:
            # Sleep for 120 seconds


            # Run Git commands
            subprocess.check_call(['git', 'add', filename])
            subprocess.check_call(['git', 'commit', '-m', commit_message])
            subprocess.check_call(['git', 'push'])
            print("Changes committed and pushed successfully.")
        
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        time.sleep(120)

if __name__ == "__main__":
    git_operations()
