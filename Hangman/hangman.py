import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
print("\nWelcome to the Hangman Game! The computer will pick a random word and you have to guess it. Remember: you only have 6 lives! Good luck!\n");

end_game = False;
num_lives = 6;
stages_index = -1;
picked_word = random.choice(word_list)
word_length = len(picked_word)
display = []

for _ in range(word_length):
    display += "_"

while not end_game:

    print(" ".join(display))
    
    print(stages[stages_index])

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed this letter!")
    
    if guess not in picked_word:
        num_lives -= 1;
        stages_index -=1;
        if num_lives == 0:
            end_game = True
            print(stages[0])
            print(f"You lose! The word was {picked_word}.")
    else:
        for i in range(word_length):
            if guess == picked_word[i]:
                display[i] = guess
    
    if "_" not in display:
        print("You win!")