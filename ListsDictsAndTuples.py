import random

#Tuples are immutable and are used to group together values that are not going to be changed.
#tuple = ('this', 'is', 'a', 'tuple')

#Dictionaries are unordered mappings of keys to values.
#They are like objects in JavaScript.
#Dictionaries are mutable meaning they can be changed
#You cannot treat dictionaries like lists because they are unordered. Meaning dictionary[0] will not work unless you have a key that is 0 in the dictionary.
#dictionary = {'key1': 'value1', 'key2': 'value2'}

#Lists are ordered collections of values.
#Lists are like arrays in JavaScript.
#Lists are mutable meaning they can be changed.
#list = ['this', 'is', 'a', 'list']

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') #This is a tuple with months in it

odds = [1, 3, 5, 7, 9] # A list with the odd numbers 1, 3, 5, 7, 9
print(odds) # Prints the odds list

things = ['red', 3, 7.9, 'yellow'] # A list
print(things) # Prints the things list

authors = []
print(len(authors)) # Prints the length of the authors list

colors = ['red', 'green', 'blue', 'yellow']
print(len(colors))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(len(primes))
print(primes)
print(primes[0]) #Acessing a specific element in a list (in this case the 1st one because list elements count up from 0 instead of 1)
print(primes[-1]) #Acessing the last element in the list
print(primes[:4]) #Slicing from the start
print(primes[3:]) #Slicing to the end
print(primes[2:5]) #Accessing a range of elements from a list (in this case elements 2 - 5)

print(list('Hamlet')) #Create a list with the list function and print it

line = "to be or not to be"
print(line.split()) #Splits the string into a list of words

name = list('Hamlet')
name[0] = 'Z'
print(name) #The output will now be ['Z', 'a', 'm', 'l', 'e', 't']

line = "to be or not to be"
words = line.split()
print('be' in words) #Checks if the word 'be' is in the list of words. Prints True if it is and False if it is not.
print('tree' in words) #Prints False because 'tree' is not in the list of words

pets = ['dog', 'mouse', 'fish']
pets.append('cat')
print(pets)

pets = ['dog', 'mouse', 'fish', 'cat', 'bird']
pets.insert(2, 'snake') #Inserts snake at index 2 of the list pets
print(pets)

pets.sort() #Sorts the list pets in alphabetical order (A-Z)
print(pets)

pets.reverse() #Reverses the order of the list pets (Z-A)
print(pets)

print(' '.join(pets)) #Joins the list pets into a string with a space between each element
print('-'.join(pets)) #Joins the list pets into a string with a dash between each element

robotCheckerInput = input('Enter a sentence: ')
robotCheckerInput = robotCheckerInput.split() #Create a list of words from the input
robotCheckerInputLowercase = [] #Create an empty list for all of the words in lowercase
for i in robotCheckerInput: #For every word in the list of words from the input, add the lowercase version of that word to the lowercase list
    robotCheckerInputLowercase.append(i.lower())
if 'robot' in robotCheckerInput:
    print('Found a small robot')
    print('Recommended attack strategy: Unplug their power cord and they will never notice you as long as you stay behind them.')
elif 'ROBOT' in robotCheckerInput:
    print('Found a big robot')
    print('Recommended attack strategy: Big robots are powered by batteries. You are going to have to run around the room and let them go after you so they eventually run out of power.')
elif 'robot' in robotCheckerInputLowercase:
    print('Found a medium sized robot')
    print('Recommended attack strategy: Unplug their power cord but they have cameras behind them so they will see you. Get your fastest soldier so they can sprint and unplug it.')
else:
    print('No robot found here')
    print('The army can safely leave')

colors = ['red', 'green', 'blue', 'yellow']
for w in colors: #For every color in the colors list, run this code
    print(w, w.count('e')) #Print the color and how many e's are in the color

line = input('Enter a line:')
count = 0
for c in line: #For every letter in the string input, run this code
    if c.isdigit():
        count += 1
print(('There is' if count == 1 else 'There are'), count, ('digit' if count == 1 else 'digits')) #If there is one digit in the input then say 'there is one digit' otherwise say 'there are X digits'

print(list(range(9)))
print(list(range(3, 9)))
print(list(range(3, 9, 2)))
print(list(range(9, 3)))
print(list(range(9, 3, -1)))

word = 'antidisestablishmentarianism'
for i in range(0, len(word), 2):
    print(i, word[i])

def displayElevatorFloorNumbers(currentFloor: int, destinationFloor: int):
    print(f'Current floor: {currentFloor}')
    print(f'Destination floor: {destinationFloor}')
    for i in range(currentFloor, destinationFloor, 1):
        print(f'Level {i}')

displayElevatorFloorNumbers(int(input('Enter the current floor you are on: ')), int(input('Enter the floor you want to go too: ')))

#Repeating things (while)
a,b = 0,1
while b < 10:
    print(b)
    new = a + b
    a = b
    b = new

guess = input("What's the password: ")
while guess != 'password':
    guess = input('Wrong try again: ')
print('You got it!')

choices = ['spaghetti', 'macaroni', 'chicken', 'beef', 'burgers', 'sushi', 'steak', 'mcdonalds', 'caviar', 'electricity', 'food']
computerChoice = random.choice(choices)
guess = input('Guess my favorite food: ')
while guess.lower() != computerChoice:
    print('Not even close.')
    guess = input('Guess? ')
print(f'Congratulations! The answer was {computerChoice}')