import os
from tkinter import Y

def HourToSeconds(hour: int):
    seconds = hour * 60 * 60 #Get seconds from the hour input
    return seconds

print("Jack and Jill")
print("Went up the hill")

print("Jack and Jill\n")
print("Went up the hill")

print("Jack and Jill\n".rstrip())
print("Went up the hill")

print("Hello " + os.getlogin() + "! Weclome to Python.")
print(f"Hello {os.getlogin()}! Welcome to Python.")

try:
    print('My age is ' + 42)
except:
    print('The line above will throw an error.')

print('My age is ' + str(42))
print('The line above will print just fine without an error being thrown')

print('My name is', os.getlogin(), 'and I am', 88, 'years old.')

print('hello', 'world')
print('hello', 'world', sep='')
print('hello', 'world', sep='\n')

print('home', 'user', 'documents', sep='/')

print(1, 'Python', '12PAD', sep='/')

print('node', 'child', 'child', sep=' ----> ')

print("12PAD : %2d, Portal: %5.2f" % (1, 5.333))

numberOne = int(input('Enter the 1st number '))
numberTwo = int(input('Enter the 2nd number '))
multiplicationAnswer = numberOne * numberTwo
print(f'The answer is {multiplicationAnswer}')
print(HourToSeconds(int(input('Enter hours that you want to convert to seconds '))))
print('{:0.2f}'.format(4234.3425623))

totalMoney = 1000
quantity = 3
price = 450

print(f'I have {totalMoney} dollars so I can buy {quantity} items at ${price} dollars')

def GetYFromXSquared(x: float):
    y = x**2
    return ('{:0.3f}'.format(y) + ' is the Y.\n' + '{:0.3f}'.format(x) + ' is the X')

print(GetYFromXSquared(float(input('Enter an X value. Y will equal X squared. '))))

print(input('Enter a username ')[::-1])