#Enter the command 'help' for help with using the address book

addressBook = {'sebastian': '1234', 'andrew': '4321', 'kovid': '123456789', 'hook': '987654321'}

command = ''

while command.lower() != 'exit':
    command = input('Enter a command: ')

    if not command:
        print('Please enter a command.')
        continue

    commandSplit = command.split()

    if commandSplit[0].lower() == 'query':
        try:
            print(addressBook.get(commandSplit[1].lower(), commandSplit[1].lower() + ' is not in the address book.'))
        except IndexError:
            print("Please enter a person's name to get their contact information.")
        except Exception as e:
            print('Unexpected error occured.')
            print(e)
    elif commandSplit[0].lower() == 'add':
        try:
            name = commandSplit[1].lower()
        except IndexError:
            print('Please enter a name for the new contact.')
            continue
        except Exception as e:
            print('Unexpected error occured.')
            print(e)
            continue
        try:
            number = commandSplit[2]
        except IndexError:
            print('Please enter a phone number for the new contact.')
            continue
        except Exception as e:
            print('Unexpected error occured.')
            print(e)
            continue
        if name in addressBook:
            print('That name is already in the address book.')
            print(name, ':', addressBook.get(name, 'Error occured.'))
            changeValue = ''
            while changeValue.lower() != 'y' and changeValue.lower() != 'n':
                changeValue = input('Would you like to change the number for ' + name + ' to ' + str(number) + '? (y/n): ')
                if changeValue.lower() == 'y':
                    addressBook[name] = number
                    print('The number for', name, 'is now', number)
                elif changeValue.lower() == 'n':
                    print(name + "'s number will stay the same.")
                else:
                    print('Please enter a y or an n.')
        else:
            addressBook[name] = number
            print(name + "'s", 'number is now', number)
    elif commandSplit[0].lower() == 'remove':
        if len(commandSplit) > 1:
            failedAttempts = []
            for i in range(1, len(commandSplit), 1):
                nameToRemove = commandSplit[i].lower()
                if nameToRemove in addressBook:
                    addressBook.pop(nameToRemove)
                    print('Removed', nameToRemove)
                else:
                    failedAttempts.append(nameToRemove)
            if len(failedAttempts) > 0:
                for attempt in failedAttempts:
                    print(attempt, 'was not found in the address book and therefore could not deleted.')
        else:
            print('Please state contact(s) to remove from the address book.')
    elif commandSplit[0].lower() == 'list':
        if len(addressBook) == 0:
            print('There are no contacts in the address book.')
        else:
            for contact in addressBook:
                print(contact + ':', addressBook.get(contact, 'Error occured while trying to get phone number.'))
    elif commandSplit[0].lower() == 'exit':
        continue
    elif commandSplit[0].lower() == 'help':
        print('Help:')
        print("To get a person's contact information, enter 'query' followed by their first name. Example: query Sebastian")
        print("To add a contact to the address book, enter 'add', then their name, then their phone number. Example: add Sebastian 12345")
        print("To remove a contact from the address book, enter 'remove' followed by the name of the contacts you want to delete seperated by spaces. Example: remove Sebastian Andrew Kovid Hook")
        print("To print the list of contacts in the address book, type 'list'.")
    else:
        print('Unrecognized command. Please try again')
print('You have now exited the address book.')

