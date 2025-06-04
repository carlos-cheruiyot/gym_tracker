# cli/menu.py
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from database.db import Session
from models.member import Member

def add_member():
    session = Session()
    print("\n--- Add New Member ---")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    join_date_str = input("Join Date (YYYY-MM-DD): ").strip()

    try:
        join_date = datetime.strptime(join_date_str, "%Y-%m-%d").date()
        new_member = Member(
            first_name=first_name,
            last_name=last_name,
            email=email,
            join_date=join_date
        )
        session.add(new_member)
        session.commit()
        print(f"✅ Member '{first_name} {last_name}' added successfully.")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
    except IntegrityError:
        session.rollback()
        print("❌ Error: Email must be unique.")
    finally:
        session.close()

def view_members():
    session = Session()
    print("\n--- All Members ---")
    members = session.query(Member).all()
    if not members:
        print("No members found.")
    else:
        for member in members:
            print(f"{member.id}: {member.first_name} {member.last_name} | {member.email} | Joined: {member.join_date}")
    session.close()

def main_menu():
    while True:
        print("\n===== Gym Tracker Menu =====")
        print("1. Add Member")
        print("2. View Members")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
