import glob
import os


data = glob.glob(os.getcwd()+'/**/*10.txt', recursive=True)

for f in data:
    print(f)

for f in data:
    with open(f, 'r') as d:
        print(d.read())

input()
