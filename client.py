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
  return input("CHOOSE THE OPTION THAT BEST FITS YOUR NEEDS:\n1 - PRINT THE ENTIRE LIST.\n2 - SEARCH FOR SOME VALUE IN THE LIST.\n3 - ADD A VALEU TO THE LIST.\n" +
              "4 - APPEND ANOTHER LIST TO THE LIST. \n0 - TO EXIT THE LIST MANAGER\n")


class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  
  x = welcome()
  while(x != '0'):

    # Print the entire list
    if x == '1':
      print ("\n",conn.root.exposed_value(),"\n")
    
    # Search a value in the list
    elif x == '2':
      data = input("\nEnter the data you want to search for:\n")
      answear = conn.root.exposed_search(data)
      if(answear == 1): print("\nThe value is in the list!\n")
      else: print("\nThe value is NOT in the list!\n")
    
    # Add a single value to the list
    elif x == '3':
      try:
        data = int(input("\nEnter the data you want to add to the list:\n"))
      except ValueError: 
        print("\nThe value must be a decimal number, try again!\n")
        continue
      conn.root.exposed_insert(data)
      print("\nAll done! The value has been inserted!\n")

    # Append a list to the list
    elif x == '4':
      data = []
      try:
        number_elements = int(input("Number of elements in the list:\n"))
      except ValueError:
        print("\nThe value must be a decimal number, try again!\n")
        continue

      print("\nEnter the values from the list that you want to append: - Each value separated by an 'Enter'\n")
      for i in range(0, number_elements):
        try:
          l = int(input())
        except ValueError:
          print("\nAn error has occurred! The value must be a decimal number! \nThe program is exiting... Try again!\n")
          exit(1)
        data.append(l)
      for values in data:
        conn.root.exposed_insert(values)
      print("\nAll done! Values have been inserted!\n")
    
    else: 
      print("\nYou enter an invalid option! Let's try again.\n")

    x = menu()
  goodbye()