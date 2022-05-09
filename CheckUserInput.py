# def checkIfInt():
#     global val
#     userInput = input('Enter a number: ')
#     try:
#         val = int(userInput)
#     except ValueError:
#         print('That input is not an int')
#         checkIfInt()

# checkIfInt()
# print(val)

#------------------------------------------------

# def checkIt2(userInput):
#     global val

#     try:
#         val = int(userInput)
#     except ValueError:
#         print("That's not an int!")
#         checkVal()

# def checkVal():
#     userInput = input('Enter an int:')
#     checkIt2(userInput)

# checkVal()
# print(val)


#------------------------------------------------



# def checkAge():
#     while True:
#         try:
#             age = int(input('Enter your age:'))
#         except ValueError:
#             print('I did not understand that. Please try again.')
#             continue

#         if age < 0:
#             print('Sorry, your answer must not be negative')
#             continue
#         else:
#             print('Your age has been successfully parsed. Thank you.')
#             break
#     if age >= 16:
#         print('You are able to leave school!')
#     else:
#         print('You are not allowed to leave school')

# checkAge()

#------------------------------------------------

# def isInt():
#     while True:
#         try:
#             userInput = int(input('Enter a number:'))
#         except ValueError:
#             print('That is not an int :(')
#         else:
#             print('That is an int! Yay!')
#             break

# isInt()

#------------------------------------------------

# def iden_type():
#     userInput = input('Enter a number: ')
#     print(type(userInput))
#     try:
#         userInput = int(userInput)
#         print(type(userInput))
#         print('User Input is an int')
#     except ValueError:
#         try:
#             userInput = float(userInput)
#             print(type(userInput))
#             print('User Input is a float')
#         except ValueError:
#             print('User Input is not an int')

# iden_type()

#------------------------------------------------

# def checkFor0():
#     while True:
#         userInput = input('Enter a 0.. ')
#         try:
#             userInput = int(userInput)
#             break
#         except ValueError:
#             print('Please enter a number')
#             continue
#     if userInput == 0:
#         print('correct')
#     else: 
#         print('try again')
#         checkFor0()

# checkFor0()

#------------------------------------------------

# def checkRangeValues(userInput):
#     try:
#         val = int(userInput)
#         if val > 0 and val < 101:
#             valid = True
#             print('Between 0 and 101')
#         else:
#             valid = False
#     except Exception:
#         valid = False
    
#     if valid == False:
#         print('wrong')

# checkRangeValues(input('Enter a number between 0 and 101: '))

#------------------------------------------------

# def checkInputIsString():
#     userInput = str(input('Enter your name...'))
#     strippedUserInput = userInput.replace(' ', '') #Gets rid of spaces
#     if not strippedUserInput.isalpha():
#         print('Your name can only consist of letters')
#         checkInputIsString()
#     else:
#         print('Thank you for entering your name')

# checkInputIsString()

#------------------------------------------------

def test():
    while True:
        try:
            amount = int(input('Enter amount: '))
            if (amount < 0):
                print('Number must not be negative')
            else:
                break
        except:
            print('Amount must be a number')
            continue
        
    print(amount)
    return amount

test()