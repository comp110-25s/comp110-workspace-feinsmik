"""Making A Wordle Program EX02"""

__author__: str = "730431256"


def contains_char(search_string: str, char: str) -> bool:
    """
    A function that checks if a given character is present in the provided string.

    Parameters:
    search_string (str): The string in which to search for the character.
    char (str): A single character to search for in the string.

    Returns:
    bool: True if the character is found, False otherwise.
    """

    assert len(char) == 1, f"len('{char}') is not 1"

    idx: int = 0

    while idx < len(search_string):  # Iterate through search_string
        if search_string[idx] == char:
            return True  # Return True if character found
        idx += 1

    return False  # If loop completes, character was not found


"""EMOJIFIED FUNCTION. RETURNS STR OF EMOJI
THAT COLOR CODES RESULTS OF A GUESSED WORD USING the prior contains char function"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Generates an emoji string of the comparison of the guess and secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    emoji_result = ""
    idx: int = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX

        idx += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Continuously prompts user for guess of expected length"""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again:")
        guess = input(f"Enter a {expected_length} character word: ")

        if guess is None:
            guess = ""

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    MAX_TURNS = 6  # Max attempts
    turns = 1  # Starting at Turn 1

    while turns <= MAX_TURNS:
        print(f"=== Turn {turns}/{MAX_TURNS} ===")  # Print current turn
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)  # results

        if guess == secret:  # if the guess is correct
            print(f"You won in {turns}/{MAX_TURNS} turns!")
            return

        turns += 1

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
