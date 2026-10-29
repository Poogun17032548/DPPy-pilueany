"""Main menu, document signing and game start."""

from datetime import datetime

from game import Game
from settings import default_settings, settings_menu
from ui import ask_int, pause


def sign_document():
    print("\n=== DOCUMENT ===")
    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Name can't be empty.")
    while True:
        surname = input("Surname: ").strip()
        if surname:
            break
        print("Surname can't be empty.")
    print("Document signed.")
    return name, surname


def start_game(signature, settings):
    name, surname = signature
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print("\nD - You have signed document.")
    print(f"Document from {now}, signed by {name} {surname} goes to dealer")
    print("D - Lights out.")
    pause(1.5)
    Game(name, settings).play()


def main_menu():
    settings = default_settings()
    signature = None
    while True:
        print("\n=== BUCKSHOT ROULETTE ===")
        print("1 - Play the roulette")
        print("2 - Sign document" + (f"  (signed: {signature[0]} {signature[1]})" if signature else ""))
        print("3 - Settings")
        print("4 - Exit")
        choice = ask_int("> ", 1, 4)
        if choice == 1:
            if signature is None:
                print("D - No signature, no game. Sign the document first.")
            else:
                start_game(signature, settings)
        elif choice == 2:
            signature = sign_document()
        elif choice == 3:
            settings_menu(settings)
        else:
            print("Bye.")
            return
