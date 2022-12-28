import rpyc
from constRPYC import * #-


def goodbye():
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
       ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
       "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `")
  print("\n                GOODBYE! HOPE TO SEE YOU AGAIN\n")
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
      ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
      "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")

def welcome():
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
       ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
       "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `")
  print("\n                WELCOME TO THE LIST MANAGER!\n")
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
      ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
      "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
  return menu()

def menu():
  return input("CHOOSE THE OPTION THAT BEST FITS YOUR NEEDS:\n1 - PRINT THE ENTIRE LIST.\n2 - SEARCH FOR A VALUE IN THE LIST.\n3 - ADD A VALUE TO THE LIST.\n" +
              "4 - APPEND ANOTHER LIST TO THE LIST. \n5 - REMOVE A VALUE FROM THE LIST. \n6 - SORT THE LIST \n0 - EXIT THE LIST MANAGER\n")

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  x = welcome()
  while(x != '0'):
    # Print the entire list
    if x == '1':
      print (conn.root.exposed_value(),"\n")
    # Search a value in the list
    elif x == '2':
      try:
        data = int(input("Enter the data you want to search for:\n"))
      except ValueError:
        print("The value must be a decimal number, try again!\n")
        continue
      if conn.root.exposed_search(data) == 1 :
        print("The value is in the list!\n")
      else: 
        print("The value is NOT in the list!\n")
    # Add a single value to the list
    elif x == '3':
      try:
        data = int(input("Enter the data you want to add to the list:\n"))
      except ValueError: 
        print("The value must be a decimal number, try again!\n")
        continue
      conn.root.exposed_insert(data)
      print("All done! The value has been inserted!\n")
    # Append a list to the list
    elif x == '4':
      data = []
      try:
        number_elements = int(input("Number of elements in the list:\n"))
      except ValueError:
        print("The value must be a decimal number, try again!\n")
        continue
      print("Enter the values from the list that you want to append: - Each value separated by an 'Enter'\n")
      for i in range(0, number_elements):
        try:
          l = int(input())
        except ValueError:
          print("An error has occurred! The value must be a decimal number! \nThe program is exiting... Try again!\n")
          exit(1)
        data.append(l)
      for values in data:
        conn.root.exposed_insert(values)
      print("All done! The list has been concatenated!\n")
    # Remove an value from list
    elif x == '5':
      try:
        data = int(input("Enter the value you want to remove from the list:\n"))
      except ValueError:
        print("The value must be a decimal number, try again!\n")
        continue
      while conn.root.exposed_search(data) == 1:
        conn.root.exposed_remove(data)
      print("All done! The value has been removed!\n")
    # Sort the list
    elif x == '6':
      order = input("Type \"ascending\" to sort the list in ascending order or type \"descending\" to sort the list in descending order: \n")
      while (order != "ascending" and order != "descending"):
        print("Wrong value! Try again!\n")
        order = input("Type \"ascending\" to sort the list in ascending order or type \"descending\" to sort the list in descending order: \n")
      if order == "ascending":
        conn.root.exposed_sort_ascending()
        print("Done! The list was sorted in ascending order\!n")
      else:
        conn.root.exposed_sort_descending()
        print("Done! The list was sorted in descending order!\n")
    # Enter a invalid value
    else: 
      print("You enter an invalid option! Let's try again.\n")

    x = menu()
  goodbye()