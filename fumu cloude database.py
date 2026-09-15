"""
FUMU Sports Cloud Athlete Manager

A command-line Python application that manages athletes
using Google Firebase Cloud Firestore.

CRUD operations:
Create  - Add athlete
Read    - View/search athletes
Update  - Update athlete
Delete  - Delete athlete
"""

from firebase_admin.exceptions import FirebaseError

from firestore_service import (
    initialize_firestore,
    add_athlete,
    get_all_athletes,
    get_athlete,
    search_athletes,
    update_athlete,
    delete_athlete,
)


def print_header():
    """Display the application title."""

    print()
    print("=" * 50)
    print("       FUMU SPORTS CLOUD ATHLETE MANAGER")
    print("=" * 50)


def prompt_required(message):
    """
    Ask for required text input.

    The user cannot continue with an empty value.
    """

    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field is required. Please enter a value.")


def prompt_age(message="Age: "):
    """Ask for a valid athlete age."""

    while True:
        value = input(message).strip()

        try:
            age = int(value)

            if 1 <= age <= 120:
                return age

            print("Please enter an age between 1 and 120.")

        except ValueError:
            print("Please enter a valid whole number.")


def prompt_optional_age(current_age):
    """Ask for an optional new age during an update."""

    value = input(
        f"Age [{current_age}] - press Enter to keep current: "
    ).strip()

    if not value:
        return current_age

    try:
        age = int(value)

        if 1 <= age <= 120:
            return age

        print("Invalid age. Keeping the current age.")
        return current_age

    except ValueError:
        print("Invalid age. Keeping the current age.")
        return current_age


def add_athlete_menu(db):
    """Collect athlete information and create a Firestore record."""

    print("\n--- ADD ATHLETE ---")

    name = prompt_required("Name: ")
    age = prompt_age()
    gender = prompt_required("Gender: ")
    sport = prompt_required("Sport: ")
    club = prompt_required("Club: ")
    phone = prompt_required("Phone: ")
    email = prompt_required("Email: ")

    athlete_id = add_athlete(
        db,
        name,
        age,
        gender,
        sport,
        club,
        phone,
        email,
    )

    print("\nAthlete added successfully.")
    print(f"Firestore ID: {athlete_id}")


def print_athletes(athletes):
    """Display a list of athlete records."""

    if not athletes:
        print("\nNo athletes found.")
        return

    print()
    print("-" * 90)

    for number, athlete in enumerate(athletes, start=1):
        print(f"Athlete #{number}")
        print(f"ID:     {athlete.get('id', '')}")
        print(f"Name:   {athlete.get('name', '')}")
        print(f"Age:    {athlete.get('age', '')}")
        print(f"Gender: {athlete.get('gender', '')}")
        print(f"Sport:  {athlete.get('sport', '')}")
        print(f"Club:   {athlete.get('club', '')}")
        print(f"Phone:  {athlete.get('phone', '')}")
        print(f"Email:  {athlete.get('email', '')}")
        print("-" * 90)


def view_athletes_menu(db):
    """Retrieve and display all athletes."""

    print("\n--- ALL ATHLETES ---")

    athletes = get_all_athletes(db)

    print_athletes(athletes)


def search_athletes_menu(db):
    """Search the Firestore athlete collection."""

    print("\n--- SEARCH ATHLETES ---")

    search_text = prompt_required(
        "Search name, sport, club, phone, or email: "
    )

    results = search_athletes(db, search_text)

    print(f"\nFound {len(results)} athlete(s).")

    print_athletes(results)


def update_athlete_menu(db):
    """Find an athlete and update its information."""

    print("\n--- UPDATE ATHLETE ---")

    athlete_id = prompt_required("Enter athlete Firestore ID: ")

    athlete = get_athlete(db, athlete_id)

    if athlete is None:
        print("Athlete was not found.")
        return

    print("\nPress Enter to keep the current value.")

    name = input(
        f"Name [{athlete.get('name', '')}]: "
    ).strip()

    if not name:
        name = athlete.get("name")

    age = prompt_optional_age(
        athlete.get("age", "")
    )

    gender = input(
        f"Gender [{athlete.get('gender', '')}]: "
    ).strip()

    if not gender:
        gender = athlete.get("gender")

    sport = input(
        f"Sport [{athlete.get('sport', '')}]: "
    ).strip()

    if not sport:
        sport = athlete.get("sport")

    club = input(
        f"Club [{athlete.get('club', '')}]: "
    ).strip()

    if not club:
        club = athlete.get("club")

    phone = input(
        f"Phone [{athlete.get('phone', '')}]: "
    ).strip()

    if not phone:
        phone = athlete.get("phone")

    email = input(
        f"Email [{athlete.get('email', '')}]: "
    ).strip()

    if not email:
        email = athlete.get("email")

    update_athlete(
        db,
        athlete_id,
        name=name,
        age=age,
        gender=gender,
        sport=sport,
        club=club,
        phone=phone,
        email=email,
    )

    print("\nAthlete updated successfully.")


def delete_athlete_menu(db):
    """Delete an athlete after confirmation."""

    print("\n--- DELETE ATHLETE ---")

    athlete_id = prompt_required("Enter athlete Firestore ID: ")

    athlete = get_athlete(db, athlete_id)

    if athlete is None:
        print("Athlete was not found.")
        return

    print(
        f"\nAthlete selected: "
        f"{athlete.get('name', 'Unknown')}"
    )

    confirmation = input(
        "Type DELETE to confirm: "
    ).strip()

    if confirmation != "DELETE":
        print("Delete cancelled.")
        return

    deleted = delete_athlete(db, athlete_id)

    if deleted:
        print("Athlete deleted successfully.")
    else:
        print("Athlete could not be deleted.")


def print_menu():
    """Display the main application menu."""

    print()
    print("1. Add Athlete")
    print("2. View Athletes")
    print("3. Search Athletes")
    print("4. Update Athlete")
    print("5. Delete Athlete")
    print("0. Exit")


def run_application(db):
    """Run the application menu until the user chooses Exit."""

    while True:
        print_header()
        print_menu()

        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                add_athlete_menu(db)

            elif choice == "2":
                view_athletes_menu(db)

            elif choice == "3":
                search_athletes_menu(db)

            elif choice == "4":
                update_athlete_menu(db)

            elif choice == "5":
                delete_athlete_menu(db)

            elif choice == "0":
                print("\nThank you for using FUMU Athlete Manager.")
                break

            else:
                print("\nInvalid option. Please choose 0-5.")

        except FirebaseError as error:
            print("\nFirebase error occurred.")
            print(f"Details: {error}")

        except Exception as error:
            print("\nAn unexpected error occurred.")
            print(f"Details: {error}")

        input("\nPress Enter to continue...")


def main():
    """Application entry point."""

    print_header()

    try:
        db = initialize_firestore()

        print("Firebase connection successful.")

        run_application(db)

    except FileNotFoundError as error:
        print("\nFirebase setup error.")
        print(error)
        print(
            "\nMake sure serviceAccountKey.json is in "
            "the same folder as main.py."
        )

    except Exception as error:
        print("\nUnable to start the application.")
        print(f"Details: {error}")


if __name__ == "__main__":
    main()