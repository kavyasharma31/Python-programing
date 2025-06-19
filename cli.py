import os

def touch(filename):
    open(filename, 'w').close()
    print(f"Created file: {filename}")

def read(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")

def rm(filename):
    try:
        os.remove(filename)
        print(f"Deleted file: {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

def mkdir(dirname):
    try:
        os.makedirs(dirname)
        print(f"Created directory: {dirname}")
    except FileExistsError:
        print(f"Directory already exists: {dirname}")

def cd(dirname):
    try:
        os.chdir(dirname)
        print(f"Changed to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {dirname}")

def ls():
    print("Contents:")
    for item in os.listdir():
        print(item)

def help_menu():
    print("""
Available commands:
touch <filename>  - Create file
read <filename>    - Show file contents
rm <filename>     - Delete file
mkdir <dirname>   - Create directory
cd <dirname>      - Change directory
ls                - List files
help              - Show help
exit              - Quit
""")

commands = {
    'touch': touch,
    'read': read,
    'rm': rm,
    'mkdir': mkdir,
    'cd': cd,
    'ls': ls,
    'help': help_menu
}

while True:
    cmd = input("Welcome! > ").strip().split()
    if not cmd:
        continue
    name, *args = cmd

    if name == 'exit':
        print("Exiting terminal. !")
        break
    elif name in commands:
        try:
            commands[name](*args)
        except TypeError:
            print("Invalid usage. Type 'help' for instructions.")
    else:
        print("Unknown command. Type 'help' to see available commands.")
