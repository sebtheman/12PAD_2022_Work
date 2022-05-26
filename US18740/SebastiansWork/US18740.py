import shutil

def printCenteredText(textToCentre, lineSpacesAfterText = 0, lineSpacesBeforeText = 0):
        if lineSpacesBeforeText > 0: print('\n' * lineSpacesBeforeText)
        print(textToCentre.center(shutil.get_terminal_size().columns))
        if lineSpacesAfterText > 0: print('\n' * lineSpacesAfterText)

def printOneCharacterAcrossTerminal(character):
    if len(character) != 1:
        raise Exception('printOneCharacterAcrossTerminal function must only have 1 character passed to it.')
    else:
        print(character * shutil.get_terminal_size().columns)

def main():
    storeNames = ['On A Roll', 'Bread 4U', 'Upper Crust', 'Knead 2 Know']
    printAlphabeticalOrder = None
    storeValues = {}
    daysInAWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    def addStores():
        userInput = None
        while True:
            while userInput != 'Y' and userInput != 'N':
                userInput = input('Would you like to add a new store? Y or N: ')

                if userInput != 'Y' and userInput != 'N': 
                    #If input is not a Y or N tell the user they entered the wrong value then start from the top of the while loop
                    print('Please enter a Y or N.')
                    continue

                if userInput == 'Y':
                    userInput = None

                    storeNameInput = ''

                    while len(storeNameInput.strip()) == 0 and all(letter.isalpha() or letter.isspace() or letter == "'" for letter in storeNameInput):
                        storeNameInput = input("Please enter the name of the store you want to add: ")

                        if storeNameInput == 'xxx':
                            break

                        if len(storeNameInput.strip()) == 0:
                            #Store name is empty so tell the user the store name must not be empty and then start from the top of the while loop
                            print('Store name must not be empty')
                            storeNameInput = ''
                            continue

                        if all(letter.isnumeric() for letter in storeNameInput):
                            #Store name is all numbers so tell the user the store name must not only be all numbers and then start from the top of the while loop
                            print('Store name must not only contain numbers.')
                            storeNameInput = ''
                            continue
                        
                        if any(letter.isalpha() == False and letter.isspace() == False and letter != "'" and letter.isnumeric() == False for letter in storeNameInput):
                            #Store name is not a string so tell the user the store name must be a string and then start from the top of the while loop
                            print('Store name must only contain letters, spaces, numbers, and apostrophes.')
                            storeNameInput = ''
                            continue

                        storeNameInput = storeNameInput.strip() #Get rid of any trailing whitespace

                        if storeNameInput in storeNames:
                            #You cannot have duplicate store names so tell the user that there cannot be 2 stores with the same name and then start from the top of the while loop
                            print('You cannot have 2 stores with the same name.')
                            storeNameInput = ''
                            continue

                        #Store name is a string and is not empty so ask the user to confirm that they want to add the store
                        confirmAddStoreInput = None
                        while confirmAddStoreInput != 'Y' and confirmAddStoreInput != 'N':
                            confirmAddStoreInput = input(f'Are you sure you want to add {storeNameInput} as a store? Y or N: ')

                            if confirmAddStoreInput != 'Y' and confirmAddStoreInput != 'N':
                                #User did not enter a Y or N so tell them they entered the wrong value and start from the top of the while loop
                                print('Please enter a Y or N.')
                                continue

                            if confirmAddStoreInput == 'Y':
                                storeNames.append(storeNameInput)
                                break
                            else:
                                #The user does not want to add the store so break the loop
                                break
                        
                        #Break out of this while loop and go back to the "Would you like to add a new store" loop
                        break
                    break
                else:
                    if len(storeNames) == 0:
                        #Tell the user that they must have at least one store to continue and then go back to the top of the while loop
                        print('You must have more than one store to continue.')
                        userInput = None
                        continue
            
            tempStoreNames = storeNames
            for item in tempStoreNames:
                correctStore = None

                while correctStore != 'Y' and correctStore != 'N':
                    correctStore = input(f'Is {item} a correct store? Y or N: ')

                    if correctStore != 'Y' and correctStore != 'N':
                        print('You must enter only a Y or an N.')

                    if correctStore == 'N':
                        correctStoreConfirm = input('Enter Y to confirm deleting this store: ')
                        if correctStoreConfirm == 'Y':
                            storeNames.remove(item)
                        else:
                            correctStore = None

            if len(storeNames) == 0:
                printOneCharacterAcrossTerminal('-')
                printCenteredText('You must have at least one store to continue', 1, 1)
                printOneCharacterAcrossTerminal('-')
                userInput = None
            else:
                print('Continuing')
                break

    def addStoreInformation(listToUse):
        for store in listToUse:
            storeValues[store] = {}
            for day in daysInAWeek:
                salesNumbers = -1
                while salesNumbers <= 0:
                    try:
                        salesNumbers = float(input(f'What was the sales numbers on {day} for store {store}: $'))
                    except:
                        salesNumbers = -1
                        print('Sales numbers must be a number.')
                        continue

                    if salesNumbers <= 0:
                        #Sales numbers is 0 or less than 0 so reset salesNumbers back to an empty string and then restart the loop
                        print('Sales numbers must be greater than 0.')
                        salesNumbers = -1
                
                storeValues[store][day] = salesNumbers

            printOneCharacterAcrossTerminal('-')
            printCenteredText(f'Sales numbers for store {store}:', lineSpacesBeforeText=1)
            for key, value in storeValues[store].items():
                printCenteredText(f'Sales numbers for {key} for store {store} are: ${value}')
            print('\n')
            printOneCharacterAcrossTerminal('-')

            confirmSalesNumbersAreCorrect = None
            while confirmSalesNumbersAreCorrect != 'Y' and confirmSalesNumbersAreCorrect != 'N':
                confirmSalesNumbersAreCorrect = input('Are these numbers correct? Y or N: ')

                if confirmSalesNumbersAreCorrect != 'Y' and confirmSalesNumbersAreCorrect != 'N':
                    print('Please only enter a Y or an N.')
                    confirmSalesNumbersAreCorrect = None
                    continue

                if confirmSalesNumbersAreCorrect == 'N':
                    try:
                        storeValues.pop(store)
                    except KeyError:
                        print('A major error has occured (cannot find key in storeValues dictionary). If this is getting printed this is very very bad. Quitting program.')
                        quit()

    printCenteredText('Welcome to the Mr Knead Store Success Calculator Program!', 1, 1)

    addStores()

    printCenteredText('List of stores: ' + ', '.join(storeNames), 1, 1)

    while printAlphabeticalOrder != 'A' and printAlphabeticalOrder != 'Z':
        printAlphabeticalOrder = input('Would you like the final print to be A-Z or Z-A? Enter A for A-Z and Z for Z-A: ')

        if printAlphabeticalOrder != 'A' and printAlphabeticalOrder != 'Z':
            #User didn't enter a A or Z. Tell the user they entered the wrong value and then start back from the top of the while loop
            print('Please enter an A for A-Z or Z for Z-A.')
            printAlphabeticalOrder = None
            continue

    addStoreInformation(storeNames)

    #If any stores had incorrect information, let the user fill in correct information now
    incorrectStores = ['dummy item'] #Dummy item is placed here to get the while loop to run
    while len(incorrectStores) > 0:
        incorrectStores = [] #Get rid of dummy item
        for store in storeNames:
            try:
                #If this succeeds then the stores information was correct
                readValue = storeValues[store]
            except KeyError:
                incorrectStores.append(store)
        if len(incorrectStores) > 0:
            addStoreInformation(incorrectStores)
            incorrectStores = ['dummy item'] #Add dummy item to get list to run one more time to check for any stores that may have wrong information entered again

    for key, value in storeValues.items(): #Calculates the total, GST, GST inclusive, max, min, mean, and averages of the sale numbers for each store
        salesNumbersList = []
        for secondKey, value in storeValues[key].items():
            salesNumbersList.append(int(value))
        storeValues[key]['total'] = sum(salesNumbersList)
        storeValues[key]['gst'] = storeValues[key]['total'] * 0.15
        storeValues[key]['gst-inclusive'] = storeValues[key]['total'] - storeValues[key]['gst']
        storeValues[key]['max'] = max(salesNumbersList)
        storeValues[key]['best-day'] = daysInAWeek[salesNumbersList.index(storeValues[key]['max'])]
        storeValues[key]['min'] = min(salesNumbersList)
        storeValues[key]['worst-day'] = daysInAWeek[salesNumbersList.index(storeValues[key]['min'])]
        storeValues[key]['mean'] = storeValues[key]['total'] / len(daysInAWeek)
        storeValues[key]['average'] = (storeValues[key]['max'] + storeValues[key]['min']) / 2

    #Sort the stores alphabetically or in descending alphabetical order depending on what the user wanted
    stores = []
    for key in storeValues:
        stores.append(key)
    if printAlphabeticalOrder == 'A':
        stores.sort()
    else:
        stores.sort(reverse=True)

    newStoreValues = {}
    for key in stores:
        newStoreValues[key] = storeValues[key]

    #Print the information
    for key, value in newStoreValues.items():
        total = value['total']
        gst = value['gst']
        gstInclusive = value['gst-inclusive']
        maxValue = value['max']
        bestDay = value['best-day']
        minValue = value['min']
        worstDay = value['worst-day']
        mean = value['mean']
        average = value['average']
        printOneCharacterAcrossTerminal('-')
        printCenteredText(f'Statistics for store {key}:', 1, 1)
        printCenteredText(f'Total sales for the week: ${total} | GST: ${gst} | GST inclusive: {gstInclusive}', lineSpacesAfterText=1)
        printCenteredText(f'The best day for {key} was {bestDay} which made ${maxValue}.')
        printCenteredText(f'The worst day for {key} was {worstDay} which made ${minValue}.')
        printCenteredText(f'The mean (sum of sales from the week divided by days in the week) is: ${mean}')
        printCenteredText(f'The average (max sale day plus min sale day divided by 2) is: ${average}', lineSpacesAfterText=1)
        printOneCharacterAcrossTerminal('-')

    #Get the best and worst performing stores and print them if there is more than one store
    if len(newStoreValues) > 1:
        storeTotalSales = []
        storeTotalSalesNames = []
        for key, value in newStoreValues.items():
            storeTotalSales.append(value['total'])
            storeTotalSalesNames.append(key)

        bestPerformingSales = max(storeTotalSales)
        bestPerformingStore = storeTotalSalesNames[storeTotalSales.index(bestPerformingSales)]
        worstPerformingSales = min(storeTotalSales)
        worstPerformingStore = storeTotalSalesNames[storeTotalSales.index(worstPerformingSales)]

        printOneCharacterAcrossTerminal('-')
        printCenteredText(f'The best performing store was {bestPerformingStore} with a sales total of ${bestPerformingSales}', lineSpacesBeforeText=1)
        printCenteredText(f'The worst performing store was {worstPerformingStore} with a sales total of ${worstPerformingSales}', 1, 1)
        printOneCharacterAcrossTerminal('-')


    printCenteredText('Program finished. Goodbye!', 1, 1)

if __name__ == '__main__':
    main()