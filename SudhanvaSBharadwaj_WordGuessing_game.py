import random 
from collections import Counter 
someWords = '''ford volkswagen toyota mercedes honda tesla nissan bmw hyundai kia renault volvo tata suzuki mahindra skoda mazda porsche ferrari audi'''
someWords=someWords.split(' ') 
word=random.choice(someWords) 
print("\nGuess the word!") 
print("The theme is Car Manufacturer")
for i in word: 
    print('_', end=' ') 
print("\n")
playing=True
letters_guessed='' 
chances=len(word)+5
correct=0
word_correct=0
while (chances!=0) and word_correct==0:
    print() 
    chances-=1
    try: 
        guess=str(input("Enter your guess: ")) 
    except: 
        print("Pls enter a letter only!") 
        continue
    if not guess.isalpha(): 
        print("Pls enter a letter only!") 
        continue
    elif len(guess)>1: 
        print("Pls enter a single letter only!") 
        continue
    elif guess in letters_guessed: 
        print("You have already guessed that letter") 
        continue
    if guess in word: 
        k=word.count(guess) 
        for _ in range(k): 
            letters_guessed+=guess
    for char in word: 
        if char in letters_guessed and (Counter(letters_guessed)!=Counter(word)): 
            print(char, end=' ') 
            correct+=1
        elif (Counter(letters_guessed) == Counter(word)): 
            print("The word is: ", end=' ') 
            print(word) 
            flag=1
            print("You\'re absolutely right!") 
            break
        else: 
            print("_", end=' ')
    if (Counter(letters_guessed) == Counter(word)):
        break
if chances==0 and (Counter(letters_guessed)!=Counter(word)): 
    print() 
    print("Game Over!") 
    print(f"The word was {format(word)}") 