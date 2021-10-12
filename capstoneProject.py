import csv
import random
import numpy as np



def randomDirectory():
    with open('randDir.csv', 'w', newline='') as csvfile:
        fieldnames = ["x", "y", "weight"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer. writeheader()
        for i in range(10):
            x = str(random.randint(0,100))
            y = str(random.randint(0,100))
            weight = str(random.randint(0,10))
            print(f"x = {x} y = {y} weight = {w}")
            writer.writerow({'x': x, 'y': y, 'weight': weight})
    pass

def readDir():
    x = []
    y = []
    w = []
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(row['x'])
            y.append(row['y'])
            w.append(row['weight'])
    return x, y, w



if __name__ == "__main__":
    randomDirectory()
    x, y, w = readDir()
    print(f"x = {x} y = {y} weight = {w}")



