import os
import subprocess
from datetime import datetime, timedelta

# Git identity
GIT_NAME = "Ervis Cela"
GIT_EMAIL = "ecela22@beder.edu.al"

# Set git config
subprocess.run(["git", "config", "user.name", GIT_NAME])
subprocess.run(["git", "config", "user.email", GIT_EMAIL])

# Start date (must be a Sunday to align with GitHub graph)
start_date = datetime(2023, 1, 1)

# "HIRE ME" pixel grid (each string = a day row from Sun to Sat)
pixels = [
    "01110 10001 11110 10001 11111 00000 1110 1110",  # Sunday
    "10000 10001 10000 10001 10000 00000 1001 1001",  # Monday
    "11100 11111 11100 11111 11100 00000 1110 1110",  # Tuesday
    "10000 10001 10000 10001 10000 00000 1000 1000",  # Wednesday
    "10000 10001 11110 10001 10000 00000 1000 1000",  # Thursday
    "00000 00000 00000 00000 00000 00000 0000 0000",  # Friday
    "00000 00000 00000 00000 00000 00000 0000 0000",  # Saturday
]

# Prepare for correct column count
columns = len(pixels[0].replace(" ", ""))

def make_commit(date):
    with open("commit.txt", "a") as f:
        f.write(f"{date}\n")
    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run([
        "git", "commit", "--date", date.strftime("%Y-%m-%dT12:00:00"),
        "-m", f"Commit for {date}"
    ])

# Loop over each column (week), then each row (day)
for col in range(columns):
    for row in range(7):
        # Remove spaces to align correctly
        if pixels[row].replace(" ", "")[col] == "1":
            commit_date = start_date + timedelta(days=(col * 7 + row))
            for _ in range(5):  # More commits = darker green
                make_commit(commit_date)
