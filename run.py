import random
import time
WORDLISTS = ""

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