import time #Import time module
codeToRun = [11, 12, 13] #List of codes to run

if 0 in codeToRun: #Blastoff
    n = 5
    while n > 0:
        time.sleep(1)
        print(n)
        n = n - 1
    time.sleep(1)
    print(n)
    print('Blastoff!')

if 1 in codeToRun: #Breaks in a loop
    while True:
        text = input('>')
        if text == 'done':
            break
        print(text)
    print('done')

if 2 in codeToRun: #Break and continues in a loop
    while True:
        text = input('>')
        if text[0] == '#':
            continue
        if text == 'done':
            break
        print(text)

if 3 in codeToRun: #Looping through a set
    print('Before')
    for thing in [9, 10, 15, 6, 'hi', 10.5, True, False, None, 20]:
        print(thing)
    print('After')

if 4 in codeToRun: #Finding the largest number in a set
    largest_so_far = -1
    print('Before', largest_so_far)
    for the_num in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52]:
        if the_num > largest_so_far:
            largest_so_far = the_num
        print(largest_so_far, the_num)
    print('After', largest_so_far)

if 5 in codeToRun: #Counting how many times the loop runs / counting how many items are in the list
    zork = 0
    print('Before', zork)
    for thing in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52]:
        zork = zork + 1
        print(zork, thing)
    print('After', zork)

if 6 in codeToRun: #Create a sum of a list of numbers
    zork = 0
    print('Before', zork) #Create a running total
    for thing in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52]:
        zork = zork + thing
        print(zork, thing)
    print('After', zork)

if 7 in codeToRun: #Create an average number from a list of numbers
    count = 0
    sum = 0
    print('Before', count, sum)
    for value in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52]:
        count = count + 1
        sum = sum + value
        print(count, sum, value)
    print('After', count, sum, sum / count)

if 8 in codeToRun: #Create a list of numbers from 1 to 10
    print('Before')
    for value in range(1, 11):
        print(value)
    print('After')

if 9 in codeToRun: #Filtering in a loop
    print('Before')
    for value in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52]:
        if value > 20:
            print(value)
    print('After')

if 10 in codeToRun: #Search using a boolean variable
    found = False
    print('Before', found)
    for value in [9, 10, 15, 6, 10.5, 20, -20, 30, 40, 52, 3]:
        if value == 3:
            found = True
            break
    print('After', found)

if 11 in codeToRun or 12 in codeToRun or 13 in codeToRun: #If you want to run code 11, 12, or 13 then create the listOfNums variable
    listOfNums = [10, 20, 30, 40, 50, -10, 21, -20, -30, -40, -50, 60]

if 11 in codeToRun: #Find the smallest number in a list of numbers using a for loop
    smallest = None
    print('Before', smallest)
    for value in listOfNums:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print(smallest, value)
    print('After', smallest)

if 12 in codeToRun: #Find the smallest number in a list of numbers using the built-in min function
    print('The smallest number in listOfNums is:', min(listOfNums))

if 13 in codeToRun: #Find the amount of items in a list using the built-in len function
    print('There are', len(listOfNums), 'items in listOfNums')