#Version of code where each die is printed on it's own line

# import random

# diceValues = []

# for i in range(6):
#     diceValues.append(random.randint(1,6))

# print('Dice:\n')
# print('Dice Values:', diceValues)

# for i in range(6):
#     if (diceValues[i] == 1):
#         print('_________\n|\t|\n|   O   |\n|\t|\n' + chr(8254)*9)
#     elif (diceValues[i] == 2):
#         print('_________\n|O      |\n|\t|\n|      O|\n' + chr(8254)*9)
#     elif (diceValues[i] == 3):
#         print('_________\n|O      |\n|   O   |\n|      O|\n' + chr(8254)*9)
#     elif (diceValues[i] == 4):
#         print('_________\n|O     O|\n|\t|\n|O     O|\n' + chr(8254)*9)
#     elif (diceValues[i] == 5):
#         print('_________\n|O     O|\n|   O   |\n|O     O|\n' + chr(8254)*9)
#     elif (diceValues[i] == 6):
#         print('_________\n|O     O|\n|O     O|\n|O     O|\n' + chr(8254)*9)

#Version of code where the dice are printed on the same line

import random

diceValues = []
diceArrangement = [[], []. [], []]

for i in range(6):
    diceValues.append(random.randint(1,6))


print('Dice:\n')
print('Dice Values:', diceValues)

for i in range(6):
    print('_________')
    if (diceValues[i] == 1):
        print('|\t|\n|   O   |\n|\t|')
    elif (diceValues[i] == 2):
        print('|O      |\n|\t|\n|      O|')
    elif (diceValues[i] == 3):
        print('|O      |\n|   O   |\n|      O|')
    elif (diceValues[i] == 4):
        print('|O     O|\n|\t|\n|O     O|')
    elif (diceValues[i] == 5):
        print('|O     O|\n|   O   |\n|O     O|')
    elif (diceValues[i] == 6):
        print('|O     O|\n|O     O|\n|O     O|')
    print(chr(8254)*9)

