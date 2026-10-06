import random


def encrypt_caesar(text, shift):
    encrypted = ""

    for character in text:
        position = ord(character) - ord("a")
        new_position = (position + shift) % 26
        encrypted += chr(ord("a") + new_position)

    return encrypted


def main():
    key = random.randint(1, 25)
    print(key)
    # The clue has no spaces.
    clue = "turnleftturnrightturnleftturnrightturnleft"
    answer = "lrlrl"

    cipher_text = encrypt_caesar(clue, key)

    print("=== Locked Cabinet ===")
    print("A screen shows an encrypted instruction:")
    print(cipher_text)
    print("You found the Caesar-cipher key in an earlier room.")
    print("Decode the instruction, then enter L for left and R for right.")
    print("Enter five letters with no spaces, for example: LRLRL")

    attempts = 0

    while True:
        guess = input("Rotation sequence: ").strip().lower()

        # After hints appear, the player can enter the numeric key.
        if guess.isdigit():
            if attempts < 3:
                print("The screen does not react. Try decoding the instruction first.")

            elif int(guess) == key:
                print("The screen deciphers the message:")
                print(clue)
                print("Now enter its L/R abbreviation.")

            else:
                print("That key does not decipher the message.")

            continue

        # Check that the player entered exactly five L/R letters.
        if len(guess) != 5 or any(letter not in "lr" for letter in guess):
            print("Enter exactly five letters, using only L and R.")
            continue

        # Correct answer.
        if guess == answer:
            print("The cabinet unlocks.")
            print("You find a fuse. New inventory item: fuse")
            break

        # Incorrect answer.
        attempts += 1
        print("The cabinet remains locked.")

        if attempts == 3:
            print("Hint: You may need the Caesar-cipher key found in the earlier room.")

        elif attempts >= 4:
            print("Hint: Try entering that numeric key to reveal the decrypted instruction.")


if __name__ == "__main__":
    main()