import random

print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                     
''')

def fullhangman():
    print('''
----------
    |
    |
    O
   /|\ 
   / \ 
''')
    
def hangman1():
    print('''
----------
    |
    |
    O
''')
    
def hangman2():
    print('''
----------
    |
    |
    O
   /|\  
''')

words = ["batman", "robin", "joker", "scarecrow", "nightwing", "harley", "alfred", "oracle"]
a = random.randint(0, len(words) - 1)
word_selection = words[a]


s = set(word_selection)

score = 0
inputted = ["_"] * len(word_selection)
print("Current Progress:", "".join(inputted))

while(1):
    
    if("".join(inputted) == word_selection):
        print("You win! :) Woohoo!")
        exit(1)
    
    input_taken = input("Please enter a character as a guess: ")
    
    if(input_taken in s and input_taken not in inputted):
        for i in range(len(word_selection)):
            if(word_selection[i] == input_taken):
                inputted[i] = input_taken
        print("Current Progress:", "".join(inputted), "\n")
    else:
        score += 1
        if(score == 1):
            hangman1()
        elif(score == 2):
            hangman2()
        elif(score == 3):
            fullhangman()
            print("\nYou lose! :(")
            exit(1)