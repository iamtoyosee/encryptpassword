from exceptions import PasswordNotLongEnough

passwords = {}
def printMenu():
  print("1. Add a new password")
  print("2. View a password")
  print("3. Delete a password")
  print("4. Exit \n")
  
def addPassword():
  name = str(input("Enter account name: "))
  password = str(input("Enter account password: "))
  with open("passwords.txt","a") as f:
    f.write(f"{name}:{password}")

  
  
  print("")
  print(f"{name}:{password}")
  print("Password added successfully")
  
def viewPassword():
  name = str(input("Enter account name: "))
  try:
    with open("passwords.txt", "r") as f:
      for line in f:
        [name, password] = line.strip().split(":")
  except FileNotFoundError:
    print("Password file does not exist")
    


def deletePassword():
  account_to_delete = str(input("Enter account name: "))
  try:
    # Step 1: Read all lines from the file
    with open("passwords.txt", "r") as f:
        lines = f.readlines()

    # Step 2: Filter out the line containing the account to delete
    with open("passwords.txt", "w") as f:
        for line in lines:
            name, password = line.strip().split(":")
            if name != account_to_delete:
                f.write(line)  # Write back all other accounts except the one to delete

    print(f"Password for {account_to_delete} has been deleted.")
  except FileNotFoundError:
    print("Password file does not exist.")
  except Exception as e:
    print(f"An error occurred: {e}")


def main():
  print("Welcome to your favorite password manager! \n")
  print("What would you like to do?")
  printMenu()
  choice = int(input("Enter Choice: "))
  print("")

  if choice == 1:
    addPassword()
  elif choice == 2:
    viewPassword()
  elif choice == 3:
    deletePassword()
  else:
    quit()

  main()
  
if __name__ == '__main__':
  main()