import random
    
name = input("Enter your name : ")

print("Good Luck", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

comp_word = random.choice(words)  # Function will choose one random word from this list of words

print("guess the characters")

user_guesses = ""
chances = 12

while chances > 0:
    wrong_guess = 0
    for char in comp_word:
        if char in user_guesses:
            print(f"Correct guess : {char}")
        else:
            wrong_guess += 1
            print("_")

    if wrong_guess == 0:
        print("you win the game")
        print("The word is ",comp_word)
        break
    guess = input(("Guess the character : "))
    user_guesses += guess
    
    if guess not in comp_word:
        chances -= 1
        print("wrong")
        print(f"you have {chances} more gusses")
        if chances == 0:
            print("game over")

