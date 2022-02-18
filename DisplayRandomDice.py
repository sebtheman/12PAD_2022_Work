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

lineOne = ''
lineTwo = ''
lineThree = ''
numbers = []

for i in range(6):
    randomNumber = random.randint(1,6)
    numbers.append(randomNumber)
    if (randomNumber == 1):
        lineOne += '|' + ' '*7 + '| '
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| '
        lineThree += '|' + ' '*7 + '| '
    elif (randomNumber == 2):
        lineOne += '|' + 'O' + ' '*6 + '| '
        lineTwo += '|' + ' '*7 + '| '
        lineThree += '|' + ' '*6 + 'O| '
    elif (randomNumber == 3):
        lineOne += '|' + 'O' + ' '*6 + '| '
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| '
        lineThree += '|' + ' '*6 + 'O| '
    elif (randomNumber == 4):
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
        lineTwo += '|' + ' '*7 + '| '
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
    elif (randomNumber == 5):
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| '
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
    elif (randomNumber == 6):
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
        lineTwo += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| '

print(f'Dice Values: {numbers}')

print('_'*9, '_'*9, '_'*9, '_'*9, '_'*9, '_'*9)
print(lineOne)
print(lineTwo)
print(lineThree)
print(chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9)

