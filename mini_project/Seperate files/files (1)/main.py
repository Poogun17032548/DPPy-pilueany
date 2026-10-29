#!/usr/bin/env python3
"""Entry point: python3 main.py"""

from menu import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nBye.")
