import os
import subprocess as sb
liste = os.listdir("Exercises/")
fileName = "first"
for item in liste:
    sb.run(["python",f"Exercises/{item}/{fileName}.py"])