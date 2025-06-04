# main.py
from models import create_tables
from cli.menu import main_menu
def main():
    create_tables()
    main_menu()
    print("Welcome to Gym Tracker!")
    # CLI menu will go here

if __name__ == "__main__":
    main()
