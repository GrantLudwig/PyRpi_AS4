# File Name: ludwig_grant_AS04.py
# File Path: /home/ludwigg/Python/PyRpi_AS4/ludwig_grant_AS04.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS4/ludwig_grant_AS04.py

# Grant Ludwig
# 10/04/2019
# AS.04
# Intro to For Loops

import random

colors = ["Red",
          "Green",
          "Blue",
          "Purple",
          "Pink",
          "White",
          "Black",
          "Yellow",
          "Orange",
          "Brown",
          "Cyan",
          "Gray",
          "Magenta",
          "Tan",
          "Fuchsia",
          "Teal",
          "Aqua",
          "Silver",
          "Gold",
          "Navy",
          "Lime",
          "Olive",
          "Beige"]

numColors = input("How many colors do you want printed? ")
print()

#Check if numColors is Ggreater than our list
if (int(numColors) > len(colors)):
	print("There are only", len(colors), "colors to choose from. Displaying", len(colors), "colors.")
	numColors = len(colors)

#Sample gets non-repeating values from the list
colorsList = random.sample(colors, int(numColors))
for i in range(len(colorsList)):
    print(str(i+1) + ".", colorsList[i])