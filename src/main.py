from rich.console import Console
from rich.table import Table


console = Console()

passwords = {}
def printMenu():
  print("[1] Add a new password")
  print("[2] View all passwords")
  print("[3] View a password")
  print("[4] Delete a password")
  print("[5] Exit")
  
def addPassword():
  name = str(input("Enter account name: "))
  password = str(input("Enter account password: "))
  with open("passwords.txt","a") as f:
    f.write(f"{name}:{password}\n")
  print("")
  
  
  # Create a table with two columns: Account Name and Password
  table = Table(title="Account Information")

  # Add the columns
  table.add_column("Account Name", justify="left", style="cyan", no_wrap=True)
  table.add_column("Password", justify="left", style="magenta")

  # Add rows with account name and password pairs
  table.add_row(f"{name}", f"{password}")


  # Print the table to the console
  console.print(table)
  console.print("\nPassword added successfully",style="green")
  
def viewPassword():
  try:
    with open("passwords.txt", "r") as f:
      
# Create a table with two columns: Account Name and Password
        table = Table(title="Account Information")

        # Add the columns
        table.add_column("Account Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Password", justify="left", style="magenta")
        for line in f:
          account, password = line.strip().split(":")
          # Add rows with account name and password pairs
          table.add_row(f"{account}", f"{password}")


        # Print the table to the console
        console.print(table)
        console.print("\nPassword added successfully",style="green")
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
  console.print("\nWelcome to your favorite password manager! \n", style="bold green")
  print("What would you like to do?\n")
  console.print("-----------------------------------", style="green")
  printMenu()
  console.print("-----------------------------------", style="green")
  choice = int(input("\nEnter Choice: "))
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