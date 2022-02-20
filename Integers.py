# Questions taken from https://quescol.com/interview-preparation/python-coding-question/

# Q8: MODIFIED: Program that finds the greatest of X amount of integers (Original question: Write a program in Python to find greatest among three integers)

numsList = [0, 10, -20, 39, 31.5, 22.3, 31.6, 40, 2, 4]
greatestNums = []
integersToGet = 5

for i in range(integersToGet):
    biggestNum = max(numsList)
    greatestNums.append(biggestNum)
    numsList.remove(biggestNum)

print(f'The biggest {integersToGet} numbers are {greatestNums}')

#Q19: Python Program to check a given number is even or odd

numEvenOrOdd = 1
if (numEvenOrOdd % 2 == 0):
    print(f'The number {numEvenOrOdd} is even.')
else:
    print(f'The number {numEvenOrOdd} is odd.')

#Q22: Python Program to find the smallest among three

listOfNums = [0, 1, 2, 3, 4, 5, -2, -10, 50, 30, 21.5, 11.2, -11.2, -11.3]

print(min(listOfNums))

