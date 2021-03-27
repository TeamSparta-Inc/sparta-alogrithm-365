import os

for user_directory in os.listdir("./01_spartan/users"):
    os.system(f"python3 -m unittest discover 01_spartan/users/{user_directory}")

