"""Prototype: the first puzzle in Escape the Research Station.

Run with: python3 first_puzzle_prototype.py
"""


def show_help():
    print("Commands: look, examine plaque, examine locker, enter code, inventory, help, quit")


def main():
    has_id_card = False

    print("=== Escape the Research Station ===")
    print("You are in the Entrance Hall. The station is in emergency lockdown.")
    print("Your first goal is to find a way into the Records Archive.")
    show_help()

    while True:
        command = input("\n> ").strip().lower()

        if command == "look":
            print("You see a reception desk, a station plaque and a locked staff locker.")

        elif command == "examine plaque":
            print("The plaque reads: 'Orion Research Station - established 1987.'")

        elif command == "examine locker":
            if has_id_card:
                print("The locker is open. It is now empty.")
            else:
                print("A note on the locker says: 'Emergency code = the station's founding year.'")

        elif command == "enter code":
            if has_id_card:
                print("You have already opened the locker.")
            else:
                code = input("Enter the four-digit code: ").strip()
                if code == "1987":
                    has_id_card = True
                    print("The locker clicks open. You take a staff ID card.")
                    print("New access: the staff ID card can open the Records Archive.")
                else:
                    print("The locker beeps. That code is not correct.")

        elif command == "inventory":
            if has_id_card:
                print("Inventory: staff ID card")
            else:
                print("Inventory: empty")

        elif command == "help":
            show_help()

        elif command == "quit":
            print("Prototype closed.")
            break

        else:
            print("I do not understand that command. Type 'help' to see the commands.")


if __name__ == "__main__":
    main()
