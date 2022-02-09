def FindTheMaximumOfTwoNumbers(x: float, y: float):
    if (x > y):
        print(f'X is bigger with a value of {x}.')
    else:
        print(f'Y is bigger with a value of {y}.')

FindTheMaximumOfTwoNumbers(float(input('Enter the first number to find a maximum ')), float(input('Enter the second number to find a maximum ')))

def FindTheMaximumOfAnyAmountOfNumbers(amountOfNums: int):
    listOfNums = []
    if (amountOfNums <= 0):
        return 'You have to put in a number amount higher than 0.'
    else:
        for i in range(1, amountOfNums + 1, 1):
            listOfNums.append(float(input('Enter the ' + ('1st' if int(repr(i)[-1]) == 1 else '2nd' if int(repr(i)[-1]) == 2 else '3rd' if int(repr(i)[-1]) == 3 else f'{i}th') + ' number. ')))
    return (f'The max number in the list is {str(max(listOfNums))}.\nThe min number is {str(min(listOfNums))}.')

print(FindTheMaximumOfAnyAmountOfNumbers(int(input('How many numbers do you want to enter to find the maximum of? '))))

def IsNumPositiveNegativeOrZero(num: float):
    if (num == 0):
        return 'The number is zero.'
    elif (num > 0):
        return 'The number is positive.'
    else:
        return 'The number is negative.'

print(IsNumPositiveNegativeOrZero(float(input('Enter a number to find out if it is positive, negative, or 0. '))))

def CheckDivisibility(num: int):
    return 'The number is divisible by 5' if num % 5 == 0 else 'The number is divisible by 11' if num % 11 == 0 else 'The number is not divisble by 5 or 11'

print(CheckDivisibility(int(input('Enter a number to find out if it is divisible by 5, 11, or none of those '))))

def IsNumOddOrEven(num: int):
    return 'The number is odd' if num % 2 == 1 else 'The number is even'

print(IsNumOddOrEven(int(input('Enter a number to find out if it is odd or even. '))))

def IsYearLeapYear(num: int):
    return f'The year {num} is a leap year.' if num % 4 == 0 else f'The year {num} is NOT a leap year.'

print(IsYearLeapYear(int(input('Enter a year to find out if it is a leap year or not. '))))

def isPartOfAlphabet(string: str):
    return f'The input {string} is part of the alphabet' if string.isalpha() == True else f'The input {string} is not part of the alphabet.'

print(isPartOfAlphabet(input('Enter something to see if it is part of the alphabet or not ')))

def isUppercaseOrLowercase(string: str):
    return f'The input {string} is uppercase.' if string.isupper() == True else f'The input {string} is not uppercase.'

print(isUppercaseOrLowercase(input('Enter something to see if it is uppercase or not. ')))

def isTriangleAnglesValid(numOne: float, numTwo: float, numThree: float):
    return 'The triangle angles are valid' if numOne + numTwo + numThree == 180 else 'The triangle angles are NOT valid!'

print(isTriangleAnglesValid(float(input('Enter the first angle ')), float(input('Enter the second angle ')), float(input('Enter the third angle '))))

def IsTriangleSidesValid(numOne: float, numTwo: float, numThree: float):
    sides = [numOne, numTwo, numThree]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    return 'The sides of the triange are valid' if hypotenuse**2 == sides[0]**2 + sides[1]**2 else 'The sides of the triangle are not valid.'

print("See if a triangle is a right-angle triangle from it's side lengths")
print(IsTriangleSidesValid(float(input('Enter the first side length ')), float(input('Enter the second side length ')), float(input('Enter the third side length '))))

def GetTypeOfTriangle(sideOne: float, sideTwo: float, sideThree: float):
    sides = [sideOne, sideTwo, sideThree]
    longestSide = max(sides)
    sides.remove(longestSide)
    if (sideOne == sideTwo == sideThree):
        return'The triangle is an equillateral triangle'
    elif (sides[0] == sides[1]):
        return 'The triangle is isosceles.'
    else:
        return 'The triangle is scalene.'

print(GetTypeOfTriangle(float(input('Enter 1st side length')), float(input('Enter 2nd side length')), float(input('Enter 3rd side length'))))