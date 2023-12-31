import random
import hangman_art
import openai
import os
from dotenv import load_dotenv

# loading env vars
load_dotenv()

# Get the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_word_list():
    # You can use ChatGPT to generate a list of words dynamically
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Generate a list of random, english words without special characters:",
        max_tokens=100
    )
    # Extract the generated words from the response
    generated_words = response.choices[0].text.split('\n')
    return [word.lower().strip() for word in generated_words if word.strip()]


# Get the word list generated by the AI or use a predefined list
word_list = generate_word_list() or ["apple", "banana", "cherry", "date", "elderberry"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

# Testing code
#  print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for _ in range(word_length)]

# Initialize variables for tracking incorrect guesses
incorrect_guesses = 0
max_incorrect_guesses = len(hangman_art.HANGMANPICS) - 1  # Maximum incorrect guesses allowed


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    found = False  # Flag to track if the guessed letter is found
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            found = True

    if not found:
        # Increment the incorrect guesses count and display the corresponding hangman art
        incorrect_guesses += 1
        print(hangman_art.HANGMANPICS[incorrect_guesses])

    print(" ".join(display))

    # Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif incorrect_guesses == max_incorrect_guesses:
        end_of_game = True
        print("You lose. The word was:", chosen_word)
