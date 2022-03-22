import os
import subprocess
from pathlib import Path

current = Path(".")
env_script = Path("./text_transcriber/Scripts")
main = Path("main.py")
#
# os.system(f"cmd /k active")
# os.system(f"cmd /k cd {current}")
# os.system(f"cmd /k python {main}.py")

subprocess.run(f"cd {current}", shell=True)
subprocess.run(f"cd {env_script}", shell=True)
# subprocess.run("active", shell=True)
# subprocess.run(f"cd {current}", shell=True)
# subprocess.run("active", shell=True)


input("wait")

