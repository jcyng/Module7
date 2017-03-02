"""
This script takes entries of users and corresponding usernames in a "database", and allows the user to add, remove, and lookup entries from this "database".
The user must reference the menu options (i.e. 1 - 5) presented to determine the action he/she wants to take. 
If the user enters an integer that is not between 1 - 5, the script will re-display the menu and ask the user to input a integer.
If the user enters a non-integer, for example a float or a string, a value error would be captured and asks user to rerun script.
Note that capitalization matters when looking up users and corresponding usernames.

"""
try: 
    from sortedcontainers import SortedDict
except ImportError:
    print("Import Error")

# Show menu options
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup Username')
    print('5. Quit')
    print()

# Dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# Counter for menu choice
menu_choice = 0

#display menu
print_menu()

# User input options results

try:
    while menu_choice != 5:
    # get menu choice from user
        menu_choice = int(input("Type in a number (1-5): "))

        # view current entries
        if menu_choice == 1:
            try:
                print("Current Users:")
                for x,y in usernames.items():
                    print("Name: {} \tUser Name: {} \n".format(x,y))
            except KeyError:
                print("Key Error") 

        # add an entry
        elif menu_choice == 2:
            try:
                print("Add User")
                name = input("Name: ")
                username = input("User Name: ")
                usernames[name] = username
            except KeyError:
                print("Key Error")
           
        # remove an entry
        elif menu_choice == 3:
            try:
                print("Remove User")
                name = input("Name: ")
                if name in usernames:
                    del usernames[name]
            except KeyError:
                print("Key Error")

        # look up user name from user      
        elif menu_choice == 4:
            try:
                print("Lookup User")
                name = input("Name: ")
                if name in usernames:
                   print("User Name: {}".format(usernames[name]))
                else:
                  print("username not found")
            except KeyError:
                print("Key Error")

        # if user enters something strange, show them the menu
        elif menu_choice != 5:
            print_menu()

except ValueError:
    print("Value Error: Re-run script and type in an integer between 1 and 5")