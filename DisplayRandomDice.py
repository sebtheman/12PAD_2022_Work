#Version of code where each die is printed on it's own line

# import random #import random module

# diceValues = [] #create diceValues list

# for i in range(6):
#     diceValues.append(random.randint(1,6)) #append random numbers to diceValues list

# print('Dice:\n')
# print('Dice Values:', diceValues) #Print Dice Values

# for i in range(6):
#     if (diceValues[i] == 1):
#         print('_________\n|\t|\n|   O   |\n|\t|\n' + chr(8254)*9) #Prints dice with a value of 1 on it's own line
#     elif (diceValues[i] == 2):
#         print('_________\n|O      |\n|\t|\n|      O|\n' + chr(8254)*9) #Prints dice with a value of 2 on it's own line
#     elif (diceValues[i] == 3):
#         print('_________\n|O      |\n|   O   |\n|      O|\n' + chr(8254)*9) #Prints dice with a value of 3 on it's own line
#     elif (diceValues[i] == 4):
#         print('_________\n|O     O|\n|\t|\n|O     O|\n' + chr(8254)*9) #Prints dice with a value of 4 on it's own line
#     elif (diceValues[i] == 5):
#         print('_________\n|O     O|\n|   O   |\n|O     O|\n' + chr(8254)*9) #Prints dice with a value of 5 on it's own line
#     elif (diceValues[i] == 6):
#         print('_________\n|O     O|\n|O     O|\n|O     O|\n' + chr(8254)*9) #Prints dice with a value of 6 on it's own line

#Version of code where the dice are printed on the same line

# import random  #Import random module

# lineOne = '' #Create the lineOne variable (will be used to print all dice on one line)
# lineTwo = '' #Create the lineTwo variable (will be used to print all dice on one line)
# lineThree = '' #Create the lineThree variable (will be used to print all dice on one line)
# numbers = [] #Create the dice numbers list

# for i in range(6):
#     randomNumber = random.randint(1,6) #Generate die numbers
#     numbers.append(randomNumber) #Append die numbers to the numbers list to print them out later
#     if (randomNumber == 1):
#         lineOne += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
#         lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
#         lineThree += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
#     elif (randomNumber == 2):
#         lineOne += '| ' + 'O' + ' '*5 + '| ' #Add a die line with | borders, an O at the left, and spacing
#         lineTwo += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
#         lineThree += '|' + ' '*5 + 'O | ' #Add a die line with | borders, an O at the right, and spacing
#     elif (randomNumber == 3):
#         lineOne += '|' + ' O' + ' '*5 + '| ' #Add a die line with | borders, an O on the left, and spacing
#         lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
#         lineThree += '|' + ' '*5 + 'O | ' #Add a die line with | borders, an O on the right, and spacing
#     elif (randomNumber == 4):
#         lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#         lineTwo += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
#         lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#     elif (randomNumber == 5):
#         lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#         lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
#         lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#     elif (randomNumber == 6):
#         lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#         lineTwo += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
#         lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing

# print(f'Dice Values: {numbers}') #Print the dice values

# print('_'*9, '_'*9, '_'*9, '_'*9, '_'*9, '_'*9) #Print the top of the dice
# print(lineOne) #Print the first line of all of the dice in one line
# print(lineTwo) #Print the second line of all of the dice in one line
# print(lineThree) #Print the third line of all of the dice in one line
# print(chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9) #Print a special underscore bottom border for the dice that is at the top so the special underscores are touching the | borders

##### Version of code that prints 5 rows of 6 dice #####

import random  #Import random module

lineOne = '' #Create the lineOne variable (will be used to print 6 dice on 5 lines)
lineTwo = '' #Create the lineTwo variable (will be used to print 6 dice on 5 lines)
lineThree = '' #Create the lineThree variable (will be used to print 6 dice on 5 lines)
numbers = [] #Create the dice numbers list

for i in range(30): #There is one for loop to generate the 30 dice numbers and then another one to print them. This is so you can print all 30 dice values in a single array and then print 6 dice on 5 lines instead of having to print 6 dice values per line
    randomNumber = random.randint(1,6) #Generate die numbers
    numbers.append(randomNumber) #Append die numbers to the numbers list to print them out later

print(f'Dice Values: {numbers}') #Print the dice values

for i in range(1, 31, 1):
    if (numbers[i-1] == 1): #If the number in the numbers list is 1 then add the die with a value of one to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
        lineThree += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
    elif (numbers[i-1] == 2): #If the number in the numbers list is 2 then add the die with a value of two to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '| ' + 'O' + ' '*5 + '| ' #Add a die line with | borders, an O at the left, and spacing
        lineTwo += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
        lineThree += '|' + ' '*5 + 'O | ' #Add a die line with | borders, an O at the right, and spacing
    elif (numbers[i-1] == 3): #If the number in the numbers list is 3 then add the die with a value of three to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '|' + ' O' + ' '*5 + '| ' #Add a die line with | borders, an O on the left, and spacing
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
        lineThree += '|' + ' '*5 + 'O | ' #Add a die line with | borders, an O on the right, and spacing
    elif (numbers[i-1] == 4): #If the number in the numbers list is 4 then add the die with a value of four to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
        lineTwo += '|' + ' '*7 + '| ' #Add a die line with | borders and spacing between them
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
    elif (numbers[i-1] == 5): #If the number in the numbers list is 5 then add the die with a value of five to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
        lineTwo += '|' + ' '*3 + 'O' + ' '*3 + '| ' #Add an O centered between | borders and spacing between them
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
    elif (numbers[i-1] == 6): #If the number in the numbers list is 6 then add the die with a value of six to the line strings. The -1 is to account for the for loop starting at 1 instead of 0
        lineOne += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
        lineTwo += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
        lineThree += '| ' + 'O' + ' '*3 + 'O' + ' ' + '| ' #Add a die line with | borders, an O on the left, an O on the right, and spacing
    if (i % 6 == 0): #If the number in the numbers list is divisible by 6 then print the line strings. This will print 6 dice on 5 lines (this if runs 5 times because the for loop will end at 30 and 30 / 6 = 5)
        print('_'*9, '_'*9, '_'*9, '_'*9, '_'*9, '_'*9) #Print the top of the dice
        print(lineOne) #Print the first line of 6 of the dice in one line
        print(lineTwo) #Print the second line of 6 of the dice in one line
        print(lineThree) #Print the third line of 6 of the dice in one line
        print(chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9, chr(8254)*9) #Print a special underscore bottom border for the dice that is at the top so the special underscores are touching the | borders
        lineOne = '' #Reset the lineOne variable to be used for the next 6 dice
        lineTwo = '' #Reset the lineTwo variable to be used for the next 6 dice
        lineThree = '' #Reset the lineThree variable to be used for the next 6 dice


