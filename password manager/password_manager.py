#python project for managing passwords we are storing the passwords in encrypted form
#and decrpyting it when the user demands it 

from cryptography.fernet import Fernet

#generating key one time for encrypting and decrypting passwords
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add():
    name = input('account name: ') 
    pwd = input('password: ')
    
    with open('passwords.txt', 'a') as f: #create a file or open existing one
        #first it is encoded to bytes and encrypted, decoded and stored in the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')
        
def view():     
    #reads the txt file line by line and views all the passwords
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            
            #decrypt the password to show to the user 
            print(f"Your password for '{user}' account is '{fer.decrypt(passw.encode()).decode()}'")
            

def delete():
    account_names = []
    with open('passwords.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.rstrip()
            user, passw = data.split("|")
            account_names.append(user)

    print(account_names)
    del_acc = input("Which account's password would you like to delete? ").lower()

    # Store updated lines without the matched account
    updated_lines = []
    for line in lines:
        user, _ = line.strip().split("|")
        if del_acc not in user.lower():
            updated_lines.append(line)

    # Write the updated content back to the file
    with open('passwords.txt', 'w') as f:
        f.writelines(updated_lines)
        
    
def update():
    pass
        
while True:
    mode = input('''select the operation you would like to do
Enter 1 add password
Enter 2 to view passwords 
Enter 3 to delete a password 
or press q to exit. ''').lower()

    if mode == "q":
        break

    if mode == "1":
        add()

    elif mode == "2":
        view()
    
    elif mode == "3":
        delete()

    else:
        print("Invalid mode, please type for 1 to 3 or q")
        continue