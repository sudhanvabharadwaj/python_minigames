#Hello! This is my amateur attempt at creating the game Mastermind using Python. I wrote this code for my first semester Python AAT:) And when I was asked to write a CUI game for the Gradient tech recruitment, I thought why not reuse it.
#Mastermind is originally a guessing game played among two players. One player creates a sequence of colors or numbers and the other player should guess the number in a fixed number of tries.
import random

def generate_code():
    secret_code = random.randrange(1000, 10000)
    return secret_code

def compute_matches(secret_code, guess):
    matches = 0
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            matches += 1
    return matches

def main():
    print("\nWelcome to Mastermind.")
    print("The secret code is a 4 digit number which you have to guess in 20 attempts.")
    print("Try to guess the secret code in as few attempts as possible.")
    secret_code=generate_code()
    attempts=0
    max_attempts=20
    while attempts<max_attempts:
        guess=int(input("\nEnter your guess: "))
        guess=str(guess)
        secret_code=str(secret_code)
        if len(guess)!=4:
            print("Invalid guess. Please enter a valid guess.")
            continue
        attempts+=1
        matches=compute_matches(secret_code,guess)      
        print(f"Attempt {attempts}: {guess} --> Matches: {matches}")
        if matches == 4:
            print("Damn! You've cracked the code! You're a Mastermind!")
            break
    if attempts == max_attempts and matches != 4:
        print(f"\nOut of attempts!! The secret code was {secret_code}.")
main()