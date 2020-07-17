import random
import time
print("\n\n ______ Welcome To Rock Paper Scissor game  ________\n\n")
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

choices = ["Rock","Paper","Scissor"]
while True: 
    print("\n\nEnter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
    user_choice = int(input("User: "))
    user = choices[user_choice-1]
    print(f"User choice is : {user} ")

    # Computer chooses randomly any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = random.randint(0, 2)
    computer = choices[comp_choice]
    print("\n now its computer turn................")
    time.sleep(2)
    print(f"Computer choice is: {computer}")
    if user == computer:
        print("\n\n >>> Opps,its a tie")
    
    else:  # checking who is the Winner
        if user == "Paper" and computer == "Rock":
            print("\n\nWinner => hurray! you win")
        elif user == "Rock" and computer == "Paper":
            print("\n\nopps! you loss \n Winner =>  Computer win")
        elif user == "Scissor" and computer == "Paper":
            print("\n\nWinner => hurray! you win")
        elif user == "Paper" and computer == "Scissor":
            print("\n\nopps! you loss \n Winner =>  Computer win")
        elif user == "Rock" and computer == "Scissor":
            print("\n\nWinner => hurray! you win")
        elif user == "Scissor" and computer == "Rock":
            print("\n\nopps! you loss \n Winner =>  Computer win")


    ans = input("\n\n Do you want to play again? 'Y' or 'N'\n ans: ")
    if ans == 'y':
        continue
    else:
        break