import random

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

def calculateGravitationalForce(gravitationalConstant: float, massOne: float, massTwo: float, distance: float):
    force = gravitationalConstant * ((massOne + massTwo) / distance)
    return force

print(calculateGravitationalForce(6.67 * 10**-11, float(input('Enter the mass of the first planet in kgs ')), float(input('Enter the mass of the second planet in kgs ')), float(input('Enter the distance between the two planets in metres squared '))))

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

user_action = input('Enter a choice (rock, paper, scissors): ')
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