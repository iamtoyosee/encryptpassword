from rich.console import Console
from rich.table import Table
from mycrypto import encrypt_password, decrypt_password  # Assuming decrypt_password is available
import os

console = Console()

def print_menu():
    console.print("[1] Add a new password", style="bold cyan")
    console.print("[2] View all passwords", style="bold cyan")
    console.print("[3] View a password", style="bold cyan")
    console.print("[4] Delete a password", style="bold cyan")
    console.print("[5] Exit", style="bold cyan")

def add_password():
    name = input("Enter account name: ").strip()
    
    if password_exists(name):
        console.print(f"Account '{name}' already exists!", style="bold red")
        return
    
    password = input("Enter account password: ").strip()
    enc_pass = encrypt_password(password)
    
    with open("passwords.txt", "a") as f:
        f.write(f"{name}:{enc_pass}\n")
    
    console.print("\nPassword added successfully.", style="bold green")

def view_all_passwords():
    if not os.path.exists("passwords.txt"):
        console.print("Password file does not exist.", style="bold red")
        return
    
    with open("passwords.txt", "r") as f:
        table = Table(title="Account Information")
        table.add_column("Account Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Password", justify="left", style="magenta")
        
        for line in f:
            account, password = line.strip().split(":")
            dec_pass = decrypt_password(password)
            table.add_row(account, dec_pass if dec_pass else "[Unable to decrypt]")
        
        console.print(table)

def view_password():
    name = input("Enter the name of the account: ").strip()
    
    if not os.path.exists("passwords.txt"):
        console.print("Password file does not exist.", style="bold red")
        return
    
    with open("passwords.txt", "r") as f:
        for line in f:
            account, password = line.strip().split(":")
            if account == name:
                dec_pass = decrypt_password(password)
                table = Table(title="Account Information")
                table.add_column("Account Name", justify="left", style="cyan", no_wrap=True)
                table.add_column("Password", justify="left", style="magenta")
                table.add_row(account, dec_pass if dec_pass else "[Unable to decrypt]")
                console.print(table)
                return
        
    console.print(f"Account '{name}' not found.", style="bold red")

def delete_password():
    account_to_delete = input("Enter account name: ").strip()
    
    if not os.path.exists("passwords.txt"):
        console.print("Password file does not exist.", style="bold red")
        return
    
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    
    with open("passwords.txt", "w") as f:
        for line in lines:
            account, password = line.strip().split(":")
            if account != account_to_delete:
                f.write(line)
    
    console.print(f"Password for '{account_to_delete}' has been deleted.", style="bold green")

def password_exists(account_name):
    if not os.path.exists("passwords.txt"):
        return False
    
    with open("passwords.txt", "r") as f:
        for line in f:
            account, _ = line.strip().split(":")
            if account == account_name:
                return True
    return False

def main():
    console.print("\nWelcome to your favorite password manager! \n", style="bold green")
    
    while True:
        console.print("-----------------------------------", style="green")
        print_menu()
        console.print("-----------------------------------", style="green")
        print('\nWhat would you like to do:')
        
        try:
            choice = int(input("\nEnter choice: ").strip())
        except ValueError:
            console.print("Invalid input! Please enter a number.", style="bold red")
            continue
        
        if choice == 1:
            add_password()
        elif choice == 2:
            view_all_passwords()
        elif choice == 3:
            view_password()
        elif choice == 4:
            delete_password()
        elif choice == 5:
            console.print("Exiting the program. Goodbye!", style="bold blue")
            break
        else:
            console.print("Invalid choice! Please try again.", style="bold red")

if __name__ == '__main__':
    main()
