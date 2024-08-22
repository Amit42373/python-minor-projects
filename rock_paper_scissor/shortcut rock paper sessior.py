import random

"""
rock = 1
paper = 0
scissor = -1

"""
computer = random.choice([0, -1, 1])
yourint = input("Enter your choice:" )
mydict = { "s":-1, "p": 0, "r": 1}       
reversedict = { -1:"scissor", 0:"paper", 1:"rock"}

you = mydict[yourint]

# now we have two number "you" and "computer"

print(f"you choose {reversedict[you]}\ncompter choose {reversedict[computer]}")

if you == computer:
    print("game draw")

else:
    if (you - computer) == -1 or (you - computer) == 2:
        print("you win")

    elif (you - computer) == 1 or (you - computer) == -2:
        print("you lose")
    else:
        print("something went wrong")


# else:
#     if you == 0 and computer == 1:       #-1
#         print("you win")
    
#     elif you == 0 and computer == -1:    #1
#         print("you lose")

#     elif you == 1 and computer == 0:     #1
#         print("you lose")

#     elif you == 1 and computer == -1:    #2
#         print("you win")

#     elif you == -1 and computer == 1:    #-2
#         print("you lose")

#     elif you == -1 and computer == 0:    #-1
#         print("you win")

#     else:
#         print("something went wrong")