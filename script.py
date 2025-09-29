import os

path = "network_security"

for dir in os.listdir(path):
    if not dir.endswith(".py"):
        newPath = f'{path}\{dir}\__init__.py'
        
        with open(newPath,"w") as f:
            f.write("")
