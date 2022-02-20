import random

count = 0
sum = 0
average = 0

for i in range(100000000):
    randomNumber = random.randint(5,13)
    sum += randomNumber
    count += 1
    average = sum/count
    if i % 10000 == 0:
        print(average)