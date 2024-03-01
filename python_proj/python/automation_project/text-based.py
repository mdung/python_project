import random
import sys

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a mysterious building with three rooms.")
    print("Your goal is to navigate through the rooms and reach the exit.")
    print("Be cautious with your choices; the outcome depends on them!\n")

def choose_room():
    print("Choose a room:")
    print("1. Room 1")
    print("2. Room 2")
    print("3. Room 3")

    choice = input("Enter the number of the room: ")
    return choice

def room_1():
    print("\nYou entered Room 1.")
    print("In this room, you see a friendly NPC.")

    # Random event
    event = random.choice(["talk", "ignore"])
    if event == "talk":
        print("The NPC gives you a key! It may be useful later.")
        return True
    else:
        print("You ignore the NPC and continue to the next room.")
        return False

def room_2(has_key):
    print("\nYou entered Room 2.")
    print("In this room, there is a locked door.")

    if has_key:
        print("You use the key to unlock the door.")
        return True
    else:
        print("The door is locked. You need a key to proceed.")
        return False

def room_3():
    print("\nYou entered Room 3.")
    print("In this room, you encounter a dangerous creature.")

    # Random event
    event = random.choice(["fight", "run"])
    if event == "fight":
        print("You bravely fight the creature and succeed!")
        return True
    else:
        print("You choose to run away from the creature.")
        print("Unfortunately, it catches up with you.")
        return False

def main():
    introduction()

    current_room = 1
    has_key = False

    while current_room <= 3:
        choice = choose_room()

        if choice == "1":
            result = room_1()
        elif choice == "2":
            result = room_2(has_key)
            if result:
                has_key = True
        elif choice == "3":
            result = room_3()

        if not result:
            print("Game Over! Better luck next time.")
            sys.exit(0)

        current_room += 1

    print("\nCongratulations! You successfully navigated through all rooms and reached the exit.")

if __name__ == "__main__":
    main()
