import os

dirName =input("What would you like to name your directory? ")
cur_direc = os.getcwd()
print(f"Making a folder called {dirName} in {cur_direc}")
os.system(f'mkdir {dirName}')
