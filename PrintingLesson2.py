import random

GConstant = 6.67 * 10**-11

a = 1
b = 2
print(a,b)

a, b = 1, 2
print(a, b)

x = 10
y = 5
x, y = y, x
print(x)
print(y)

a = 10
print(id(10))
print(id(a))

print(type(10))
print(type(10.5))
print(type(True))
print(type(False))
print("Hello World", "has a type", type("Hello World"))
print('Hello World', 'has a type', type('Hello World'))
print('word', 'has a type', type('word'))
print('a', 'has a type', type('a'))
print('@', 'has a type', type('@'))
print(23, 'has a type', type(23))
print('23', 'has a type', type('23'))
a = "23"
print(a, 'has a type', type(a))
b = 23
print(b, 'has a type', type(b))

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end='\nLets learn Python\n')

name = " you me "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(len(name))
print(name)
name = name.lstrip()
print(len(name))
print(name)
name = name.rstrip()
print(len(name))
print(name)
name = name.title()
print(len(name))
print(name)

def calculateGravitationalForce():
    massOne = 'hi'
    massTwo = 'hi'
    distance = 'hi'
    while (type(massOne) != float):
        try:
            massOne = float(input('Enter the mass of the first planet in kgs (number followed by e and then power e.g 2.4e10) '))
        except:
            print('Please put in a float')
    while (type(massTwo) != float):
        try:
            massTwo = float(input('Enter the mass of the second planet in kgs (number followed by e and then power e.g 2.4e10) '))
        except:
            print('Please put in a float')
    while (type(distance) != float):
        try:
            distance = float(input('Enter the distance between the two planets in metres squared (number followed by e and then power e.g 2.4e10) '))
        except:
            print('Please put in a float')
    force = GConstant * ((massOne + massTwo) / distance)
    return str(force) + 'N'

print(calculateGravitationalForce())

def calculateDiscount(price: float):
    if (price >= 300):
        discountedPrice = price * 0.7
    elif (price >= 200 and price < 300):
        discountedPrice = price * 0.8
    elif (price >= 100 and price < 200):
        discountedPrice = price * 0.9
    else: 
        discountedPrice = price * 0.95
    return 'The price was $' + str(price) + ' and the discounted price is $' + str(discountedPrice) + '.'

print(calculateDiscount(float(input('What is the price you want to discount? '))))

def rep_cat(x, y):
    x = str(x) * x
    y = str(y) * y
    result = x + y
    return result

print(rep_cat(int(input('Enter the first number ')), int(input('Enter the second number '))))

age = int(input('What is your age? '))
if (age >= 18):
    print('You are old enough to vote!')
else:
    print('You are not old enough to vote.')

user_action = None
while (user_action != 'rock' and user_action != 'paper' and user_action != 'scissors'):
    try:
        user_action = input('Enter a choice (rock, paper, scissors): ')
    except:
        print('Wrong input.')
possible_actions = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_actions)
print(f'\nYou chose {user_action}. The computer chose {computer_action}.\n')
if (user_action == computer_action):
    print(f"Both players selected {user_action}! It's a tie!")
elif (user_action == 'rock'):
    if (computer_action == 'scissors'):
        print('Rock smashes scissors! You win!')
    else:
        print('Paper covers rock! You lose!')
elif (user_action == 'scissors'):
    if (computer_action == 'paper'):
        print('Paper cuts scissors! You win!')
    else:
        print('Rock smashes scissors! You lose!')
elif (user_action == 'paper'):
    if (computer_action == 'rock'):
        print('Paper covers rock! You win!')
    else:
        print('Scissors cuts paper! You lose!')
else:
    print('Wrong input entered.')

user_action = None
while (user_action != 'rock' and user_action != 'paper' and user_action != 'scissors' and user_action != 'lizard' and user_action != 'spock'):
    try:
        user_action = input('Enter a choice (rock, paper, scissors, lizard, spock) ')
    except:
        print('Wrong input')
possible_actions = ['rock', 'paper', 'scissors', 'lizard', 'spock']
computer_action = random.choice(possible_actions)
print(f'\nYou chose {user_action}. The computer chose {computer_action}\n')
if (user_action == computer_action):
    print(f'Both players chose {user_action}! Both players tie!')
elif (user_action == 'rock'):
    if (computer_action == 'lizard' or computer_action == 'scissors'):
        print('Congratulations you win!')
    else:
        print('Oof you lose :(')
elif (user_action == 'paper'):
    if (computer_action == 'rock' or computer_action == 'spock'):
        print('Congratulations you win!')
    else:
        print('Oof you lose :(')
elif (user_action == 'scissors'):
    if (computer_action == 'paper' or computer_action == 'lizard'):
        print('Congratulations you win!')
    else:
        print('Oof you lose :(')
elif (user_action == 'lizard'):
    if (computer_action == 'spock' or computer_action == 'paper'):
        print('Congratulations you win!')
    else:
        print('Oof you lose :(')
elif (user_action == 'spock'):
    if (computer_action == 'rock' or computer_action == 'paper'):
        print('Congratulations you win!')
    else: 
        print('You lose')
else:
    print('Wrong input entered :(')