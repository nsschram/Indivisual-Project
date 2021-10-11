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
            print(f"x = {x} y = {y}")
            writer.writerow({'x': x, 'y': y, 'weight': weight})
    pass

"""
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
"""



if __name__ == "__main__":
    randomDirectory()




