import random
import hangman_art
import hangman_words
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
display = []
end_of_game = False
lives = 6
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
for letter in chosen_word:
    display += "_"
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    word_length = len(chosen_word)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"Number of lives: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose!")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    # TODO-2: - Import the stages from hangman_art.py
    print(hangman_art.stages[lives])