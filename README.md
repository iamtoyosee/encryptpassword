## Encrypt Password Manager

### Overview

The Encrypt Password Manager is a Python-based command-line application that allows you to securely store and manage your passwords. The passwords are encrypted using the `cryptography` library (Fernet symmetric encryption) and stored in a local file. You can add, view, and delete encrypted passwords, ensuring that your sensitive information remains secure.

### Features

- **Add a new password**: Encrypts the password before storing it.
- **View all passwords**: Displays all saved account names and their associated decrypted passwords.
- **View a specific password**: Retrieves and decrypts the password for a specific account.
- **Delete a password**: Removes an account and its associated password.
- **Command-line interface**: Easy-to-use CLI powered by the `rich` library for styled output.

### Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [How it Works](#how-it-works)
- [License](#license)

### Requirements

To run this project, you'll need to install the following dependencies:

- Python 3.6+
- Cryptography library
- Rich library

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/encrypt-password-manager.git
    cd encrypt-password-manager
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **Linux/macOS**:

        ```bash
        source venv/bin/activate
        ```

    - **Windows**:

        ```bash
        .\venv\Scripts\activate
        ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. To start the password manager, run the `main.py` script:

    ```bash
    python main.py
    ```

2. You'll be presented with a menu to choose from the following options:
    - Add a new password
    - View all passwords
    - View a specific password
    - Delete a password
    - Exit

3. **Adding a new password:**
   - You'll be prompted to enter the account name and password. The password will be encrypted and stored securely in `passwords.txt`.

4. **Viewing passwords:**
   - You can view either all passwords or a specific one by account name. The passwords will be decrypted and displayed in a readable format.

5. **Deleting a password:**
   - Provide the account name, and the associated password will be deleted from the storage.

### Example

#### Add a New Password:

```bash
$ python main.py
-----------------------------------
[1] Add a new password
[2] View all passwords
[3] View a password
[4] Delete a password
[5] Exit
-----------------------------------

Enter choice: 1

Enter account name: Gmail
Enter account password: mypassword123

Password added successfully
```