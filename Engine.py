import random
from hangman_art import logo, stages
import os
def main():
    Dic_file = open("hangman_words.py", "r")

    word_list = []

    for words in Dic_file:
      line_list = words.split()
      word_list.extend(line_list)

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    # print(chosen_word)
    end_of_game = False
    lives = 6
    already_guessed = []
    print (f"{logo}{stages[0]}")

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
      guess = input("Guess a letter: ").lower()

      if len(guess) == 1:
        if os.name == 'nt':
          os.system('cls')
        else:
          os.system('clear')
        if guess in already_guessed:
          print("You have already guess this letter")
        else: #preven list duplication
          already_guessed.extend(guess)
        # print(already_guessed)
        #Check guessed letter
        for position in range(word_length):
          if chosen_word[position] == guess:
            display[position] = guess

        if guess not in chosen_word:
            print(f"'{guess}' is not part of the word")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(chosen_word)

        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
        print(stages[lives])
      else:
        print("only one letter allowed")
