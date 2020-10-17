import random

words_list = 'codecool absolwenci mentorzy studenci'.split()   #lista słów do importowania

print("Welcome to the Cool world of the Hangman")   #powitanie
nick = input("Enter your nick: ")

def random_word():
     word = random.choice(words_list)
     return word
     

lifes = 6 #deinijuemy ilość żyć






                


        
        







def hangman(lifes):
    death = [ 
                """
                     +---+
                     X   |
                    /|\  |
                    / \  |
                         |
                 =========
                """,
                """
                     +---+
                     O   |
                    \|   |
                    / \  |
                         |
                 =========
                """,
                """
                     +---+
                     O   |
                     |   |
                    / \  |
                         |
                 =========
                """,
                """
                     +---+
                     O   |
                     |   |
                      \  |
                         |
                 =========
                """,
                """
                     +---+
                     O   |
                     |   |
                         |
                         |
                 =========
                """,
                """
                     +---+
                     O   |
                         |
                         |
                         |
                 =========
                """,
                """
                      +---+
                         |
                         |
                         |
                         |
                 =========
                """
]





        # letter = input("Give me a letter!: ")
        # if len(letter) == 1 and letter.isalpha():
        #     if letter in letters_guessed:
        #         print("It's already here!", letter)
        #     elif letter not in word:
        #         print(letter, "is not in it")
        #         lifes -= 1
        #         letters_guessed.append(letter)
        #     else:
        #         print("Wow", letter, " is in it")
        #         letters_guessed.append(letter)