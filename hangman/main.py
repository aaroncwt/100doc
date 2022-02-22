import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

# Randomly choose a word from word_list
chosen_word = random.choice(word_list)

# Create blank fields for chosen_word
display = []
guesses = []

for letter in chosen_word:
    display.append("_")

print(f"{logo} \n\n Your word has {len(chosen_word)} letters \n {' '.join(display)} \n")

blanks = display.count('_')

end_of_game = False

while not end_of_game:

    # Prompt user to guess a letter and assign their answer to a variable called guess
    guess = input("Guess a letter: ").lower()
    print("\n")

    if guess in guesses:
        print(f"You've already guessed {guess}. Guess again.")

    else:
        
        guesses.append(guess)

        # Check if guess is one of the letters in chosen_word; replace display with correct guesses
        for count, letter in enumerate(chosen_word):
            if guess == letter:
                display[count] = letter
                
        # Check if guess is one of the letters in chosen_word; remove 1 life if not
        if guess not in chosen_word:
            print(f"{guess} is a wrong guess! You lose 1 life.")
            lives -= 1
        elif guess in chosen_word:
            print(f"{guess} is a good guess!")

        blanks = display.count('_')

        #print(display)
        print(f"{' '.join(display)}")
        
        print(stages[lives])

    if lives <= 0:
        end_of_game = True
        print("You died")       # End
    elif blanks == 0:
        end_of_game = True
        print("You've won!")    # End
