########################################
##                                    ##
##             Made By:               ##
##            Pillow3000              ##
##                                    ##
##           Github link:             ##
##       https://bit.ly/3etZ4zr       ##
##                                    ##
########################################


# Importing Python Modules 
import os
import sys
import random
# Importing Python Projects
import password
import mail_bot
import discordbot
import DiceRoller
import add_command

 
path = r'C:\\Users\\micha\\OneDrive\\Desktop\\Code_Folder\\Python\\Real_Projects\\Pillow-Blocks\\Terminal.py' 
os.system('cls')
print('''

  ____  _ _ _                 ____  _            _        
 |  _ \(_) | | _____      __ | __ )| | ___   ___| | _____ 
 | |_) | | | |/ _ \ \ /\ / / |  _ \| |/ _ \ / __| |/ / __|
 |  __/| | | | (_) \ V  V /  | |_) | | (_) | (__|   <\__ \\
 |_|   |_|_|_|\___/ \_/\_/   |____/|_|\___/ \___|_|\_\___/
                                                          
  Github: https://bit.ly/3etZ4zr 
''')

while True: 
    command_lst = ['help', 'say', 'exit', 'break','reboot', 'addcmd', 'password', 'mailbot', 'discordbot', 'roll'] # All Commands
    command = input('>') # command line input
    command_save = command
    command = command_save.split(' ', 1)[0] # splits command into the base command (Example: <command> <modifiers/input-text>)
    if len(command_save.split()) > 1:
        command_modifiers = command_save.split(' ', 1)[1] # splits command into the command modifiers (Example: <command> <modifiers/input-text>)
        
        if command_modifiers == '-h':
            if command == 'addcmd':
                print('addcmd: Asks questions and prints out command that can be added to Terminal.py')
            if command == 'say':
                print('say (text): Prints Back What you say (It\'s Echo)')
            if command == 'exit':
                print('exit: Closes the program')
            if command == 'reboot':
                print('reboot: Reboots the Terminal')
            if command == 'password':
                print('password (length): Prints a password the same length of the command modifier')
            if command == 'mailbot':
                print('mailbot: Asks for Email info (Email, Password, Reciever, Subject, Body) and Sends Email')
            if command == 'discordbot':
                print('discordbot: Boots a Discord.py Bot')
            if command == 'roll':
                print('roll (die-type): Rolls a die changes the amount of sides with <command-modifier> (Example: <command> <command-modifier>)')


    if any(command in i for i in command_lst): # checks if command (the user's input) is a valid command in the command list 
        
        ###################################
        ## ---System Terminal Commands---##
        ###################################

        
        # Help Message
        if command == 'help' :
            print('''
            ---Basic Commands---
            help: Prints this help list (use -h on any command to see it's help entry)
            addcmd: Asks questions and prints out command that can be added to Terminal.py
            say (text): Prints Back What you say (It's Echo)
            exit: Closes the program
            reboot: Reboots the Terminal
            
            ---Python Project Commands---
            password (length): Prints a password the same length of the command modifier
            mailbot: Asks for Email info (Email, Password, Reciever, Subject, Body) and Sends Email
            discordbot: Boots a Discord.py Bot
            roll (die-type): Rolls a die changes the amount of sides with <command-modifier> (Example: <command> <command-modifier>)''')
        # Stops Program    
        if command == 'exit':
			
            if command_modifiers == '-h':
                pass
            else:
				try:
					print('Dave, stop. Stop, will you? Stop, Dave. Will you stop, Dave? Stop, Dave. I\'m afraid.')
					break
				except NameError:
					print('Dave, stop. Stop, will you? Stop, Dave. Will you stop, Dave? Stop, Dave. I\'m afraid.')
					break

        # Returns inputted text
        if command == 'say':
            try:
                if command_modifiers == '-h':
                    pass
                elif command_modifiers == 'hello':
                    print('Hello David')
                else:
                    print(command_modifiers)
			except NameError:
				if command_modifiers == '-h':
                    pass
                elif command_modifiers == 'hello':
                    print('Hello David')
                else:
                    print(command_modifiers)

        # Reboots Terminal.py
		try:
			if command == 'reboot':
				if command_modifiers == '-h':
					pass
				else:
					try:
						print('System rebooting...')
						os.execl(sys.executable, sys.executable, * sys.argv)
						os.system('cls')
					except NameError:
						print('System rebooting...')
						os.execl(sys.executable, sys.executable, * sys.argv)
						os.system('cls')
					

        if command == 'addcmd':
            try:
                if command_modifiers == '-h':
                    pass
                if command_modifiers == None:
                    print('Adding Command...')
                    add_command.add_cmd()
            except NameError:
                print('Adding Command...')
                add_command.add_cmd()

        #####################################    
        ## --- Python Project Commands --- ##
        #####################################

        # Creates password equal in size put in
        if command == 'password':
            if command_modifiers == '-h':
                pass
            else:
				try:
                	password.password(int(command_modifiers))
				except NameError:
					print('No amount was specified defaulting to 7')
					password.password(7)

        # Asks for Email info (Email, Password, Subject, Body) and Sends it
        if command == 'mailbot':
            if command_modifiers == '-h':
                pass
            else:
				try:
                	mail_bot.GmailBot()
				except NameError:
					mail_bot.GmailBot()

        if command == 'discordbot':
            if command_modifiers == '-h':
                pass
            else:
				try:
					print('Bot is Starting...')
					discordbot.discordbot_start()
				except NameError:
					print('Bot is Starting...')
					discordbot.discordbot_start()

        if command == 'roll':
            if command_modifiers == '-h':
                pass
            else:
                try:
                    print('Rolling...')
                    DiceRoller.rolldie(command_modifiers)
                except NameError:
                    DiceRoller.rolldie(6)

    else:
        print(f'Unknown Command: {command}') # prints Unknown Command if command not valid.


