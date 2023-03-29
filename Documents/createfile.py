import os
liste = os.listdir("Exercises/")
fileName = "first"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as fileContent:
        fileContent.write("""""")
    

