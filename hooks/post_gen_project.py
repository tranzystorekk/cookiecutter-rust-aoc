import subprocess

subprocess.run(["git", "init"])
subprocess.run(["git", "add", "-f", "*"])
subprocess.run(["git", "commit", "-m", "Initial project"])
