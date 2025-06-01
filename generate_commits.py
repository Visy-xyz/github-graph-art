import os
import subprocess
from datetime import datetime, timedelta

# Git identity
GIT_NAME = "Ervis Cela"
GIT_EMAIL = "ecela22@beder.edu.al"

# Set git identity
subprocess.run(["git", "config", "user.email", GIT_EMAIL])
subprocess.run(["git", "config", "user.name", GIT_NAME])

# Start date: June 2, 2024 (Sunday)
start_date = datetime(2024, 6, 2)

# Pixel art for "HIRE ME" (each character is 5 pixels wide, 1 space between)
pixels = [
    "01110 10001 11110 10001 11111 00000 01110 01110",  # Sunday
    "10000 10001 10000 10001 10000 00000 10001 10001",  # Monday
    "11100 11111 11100 11111 11100 00000 10001 10001",  # Tuesday
    "10000 10001 10000 10001 10000 00000 10001 10001",  # Wednesday
    "10000 10001 11110 10001 10000 00000 01110 01110",  # Thursday
    "00000 00000 00000 00000 00000 00000 00000 00000",  # Friday
    "00000 00000 00000 00000 00000 00000 00000 00000",  # Saturday
]

# Commit generator
def make_commit(date):
    with open("commit.txt", "a") as f:
        f.write(f"{date}\n")
    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run([
        "git", "commit", "--date", date.strftime("%Y-%m-%dT12:00:00"),
        "-m", f"Commit for {date}"
    ])

# Generate commits based on pixel grid
for row in range(7):
    for col in range(len(pixels[0])):
        if pixels[row][col] == "1":
            commit_date = start_date + timedelta(days=(col * 7 + row))
            for _ in range(5):  # Darker pixel = 5 commits
                make_commit(commit_date)
