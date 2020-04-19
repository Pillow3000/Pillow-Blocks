import pyperclip
def add_cmd():

    cmd_name = input('What do you want your command to be called? ')
    cmd_module = input('What is the name of your Module? ')
    cmd_function = input('What is the name of your function? ')
    cmd_function = cmd_function + '()'


    print('Printing Result...') 
    print(f"""
    if command == '{cmd_name}':
        {cmd_module}.{cmd_function}
    
    (This command is already copied to your clipboard)
    """)

    text = f"""
    if command == '{cmd_name}':
        {cmd_module}.{cmd_function}
    """ 
    pyperclip.copy(text)


    