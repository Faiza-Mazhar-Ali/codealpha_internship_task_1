
import random

# Global list of words (Can be moved inside setup_game if preferred)
WORD_LIST = ["python", "intern", "codealpha", "script", "hangman", "developer", "project"] 
MAX_INCORRECT_GUESSES = 6

def setup_game():
    """Sets up the initial game state."""
    
    secret_word = random.choice(WORD_LIST).lower()
    guessed_letters = set()
    incorrect_guesses_made = 0
    
    print("\n" + "="*40)
    print("Welcome to Hangman!")
    print("Type 'skip' to quit, or 'hint' for a clue.")
    print(f"The word has {len(secret_word)} letters. Start guessing.")
    print("="*40)
    
    return secret_word, guessed_letters, MAX_INCORRECT_GUESSES, incorrect_guesses_made

def display_word(secret_word, guessed_letters):
    """Generates the current state of the word (with underscores/letters)."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_available_letters(guessed_letters):
    """Calculates and returns a string of available letters."""
    import string
    all_letters = set(string.ascii_lowercase)
    available = all_letters - guessed_letters
    return " ".join(sorted(list(available)))

def hangman_visual(incorrect_guesses_made):
    """Prints a simple ASCII representation of the Hangman."""
    stages = [
        # Stage 0: Starting
        """
           -----
           |   |
               |
               |
               |
               -
        """,
        # Stage 1: Head
        """
           -----
           |   |
           O   |
               |
               |
               -
        """,
        # Stage 2: Body
        """
           -----
           |   |
           O   |
           |   |
               |
               -
        """,
        # Stage 3: Left Arm
        """
           -----
           |   |
           O   |
          /|   |
               |
               -
        """,
        # Stage 4: Right Arm
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               -
        """,
        # Stage 5: Left Leg
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               -
        """,
        # Stage 6: Full Hangman (Game Over)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               -
        """
    ]
    print(stages[incorrect_guesses_made])


# --- Main Game Loop ---
def play_hangman():
    """The main function to run the Hangman game."""
    
    secret_word, guessed_letters, max_guesses, incorrect_count = setup_game()
    hint_used = False
    
    while incorrect_count < max_guesses:
        
        current_display = display_word(secret_word, guessed_letters)
        
        print("\n" + "="*40)
        hangman_visual(incorrect_count)
        print("Word: ", current_display)
        
        # New Feature: Count of Incorrect Letters
        print(f"Incorrect guesses made: **{incorrect_count}** out of {max_guesses}")
        
        # New Feature: Letters Left Option
        available_letters = get_available_letters(guessed_letters)
        print("Available letters: ", available_letters)
        print("=" * 40)

        # Get user input
        guess = input("Guess a letter or command ('skip'/'hint'): ").lower().strip()

        # New Feature: Skip Game Option
        if guess == 'skip':
            print(f"\nGame skipped. The word was **{secret_word.upper()}**.")
            return

        # New Feature: Hint Option
        if guess == 'hint':
            if hint_used:
                print("Hint already used for this word!")
            else:
                # Find the first unguessed letter and reveal it
                for letter in secret_word:
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        print(f"\n💡 Hint used! Revealing the letter: **{letter.upper()}**")
                        hint_used = True
                        break
                # Check for win immediately after a hint
                if all(letter in guessed_letters for letter in secret_word):
                    print("\n🎉 Congratulations! You guessed the word with a little help:")
                    print(secret_word.upper())
                    return
            continue # Continue to the next loop iteration after handling hint/skip

        # Standard Guess Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter, 'skip', or 'hint'.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a new letter.")
            continue
        
        # Add the valid guess
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in secret_word:
            print("✨ Correct guess!")
        else:
            print("❌ Incorrect guess!")
            incorrect_count += 1

        # Check for Win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You guessed the word:")
            print(secret_word.upper())
            return

    # Loss condition
    print("\n" + "="*40)
    hangman_visual(incorrect_count)
    print("Game Over! You ran out of guesses.")
    print(f"The secret word was: **{secret_word.upper()}**")
    print("=" * 40)

if __name__ == "__main__":
    play_hangman()