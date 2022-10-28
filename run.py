import random
import time
WORD_LISTS = ""
SCORE = 6
CC = "CHARACTERS"
X = "EXIT"
CHARACTERS = ""
EXIT = ""
CATEGORY = ""
RANDOM_WORD = ""
PLAY_GAME = ""


# welcome / greeting
print("Welcome to the Hangman Game!\n")
time.sleep(1)
print("Instructions: guess the correct wordchosen by the computer.")
print("The player can only guess one letter or word at a time.")
time.sleep(1)
name = input("\nWhat is your name: ").upper()
print("\nBest of Luck " + name)
time.sleep(1)
print("\nThe Hangman Game is about to start.\n")
time.sleep(1)

# choose a random word
while SCORE > 0:
    if WORD_LISTS.upper() == "CC":
        RANDOM_WORD = random.choice("CATEGORY")
        break
    else:
        WORD_LISTS = input("Slect CATEGORY: CC for CHARACTERS; X for exit, _")
    if WORD_LISTS == "X".upper()
        print("Goodbye, please visit again!")
        PLAY_GAME = False
        break
        print("----------")
