# Code Refactored

import os
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog

def load_script():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            script_content = file.read()
            print(f"\nLoaded Script:\n{script_content}\n")
    reset_menu()

def make_script():
    print("\nEnter your script (type 'exit' to finish):")
    script_lines = []
    while True:
        line = input()
        if line.lower() == 'exit':
            break
        script_lines.append(line)
    print("\nYour Script:\n" + "\n".join(script_lines) + "\n")
    reset_menu()

def kill_script():
    print("\nScript has been removed.\n")
    reset_menu()

def reset_menu():
    input("Press Enter to return to the main menu...")
    main_menu()

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[94m")  # Set text color to blue
    print("▓█████▄  ▄▄▄        ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓▒██   ██▒")
    print("▒██▀ ██▌▒████▄    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▒▒ █ █ ▒░")
    print("░██   █▌▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░░░  █   ░")
    print("░▓█▄   ▌░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░  ░ █ █ ▒ ")
    print("░▒████▓  ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ▒██▒ ▒██▒")
    print(" ▒▒▓  ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   ▒▒ ░ ░▓ ░")
    print(" ░ ▒  ▒   ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    ░░   ░▒ ░")
    print(" ░ ░  ░   ░   ▒   ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░       ░    ░  ")
    print("   ░          ░  ░      ░  ░ ░         ░      ░                     ░    ░  ")
    print("░                         ░                                                 ")
    print("\033[94m")  # Reset text color
    print("Command Menu:")
    print("1. Load a Script")
    print("2. Make a Script")
    print("3. Kill a Script")

    while True:
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            load_script()
        elif choice == '2':
            make_script()
        elif choice == '3':
            kill_script()
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    main_menu()
