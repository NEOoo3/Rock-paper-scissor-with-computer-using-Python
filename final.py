import random
while True:
        user_action=input("Enter Your Choice;  rock , paper  or  scissors   : ")
        count1=0
        count2=0
    
        possible_action=["rock","paper","scissors"]
        computer_action=random.choice(possible_action)
        print(f"\nYou chose {user_action}, computer chose {computer_action}")
        print(" ")

        if user_action == computer_action:
            print(f"BOTH PLAYERS SELECTED {user_action}. It's a tie !!!\n")
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||\n ")

        elif user_action=="rock":
            if computer_action == "scissors":
                print("ROCK SMASHES SCISSORS! YOU WIN !!\n")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||| \n")
                count1+=1

            else:
                print("PAPER COVERS ROCK , YOU LOSE.\n")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||| \n")
                count2+=1

        elif user_action=="paper":
            if computer_action == "scissors":
                print("SCISSORS CUT PAPER! YOU LOSE.\n")
                print("||||||||||||||||||||||||||||||||||||||||||||||||||||\n ")
                count2+=1

            else:
                print("PAPER COVERS ROCK , YOU WIN !!\n")
                print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
            count1+=1

        elif user_action =="scissors":
            if computer_action== "paper":
                print("SCISSORS CUT PAPER!, YOU WIN !!!\n")
                print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                count1+=1

            else:
                print("ROCK SMASHES SCISSORS! YOU LOSE.\n") 
                print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                count2+=1

        else:
            print(" WRONG INPUT ")
            print("-_-")
            print("MIND THE SPELLING :P\n")
            print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
            print("            ")
        print("SCORES")
        print("\n \nScore Board: \n ---------------- \n| Your Score:",count1,"|"," \n ---------------- \n| Comp  Score:",count2,"|\n ---------------- \n")
        print("                        ")
        print("---------------------------------------------------------------------------------------------------------------------")




#random : used to import random function in order to get random values 
#random.choice=The choice() method returns a randomly selected element from the specified sequence.
#The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
#count1: to count score of player 
#count2: to count the score of computer
#class: to create an object
#iterable is an object which can be looped over or iterated over with the help of a for loop
#contains a countable number of values 
#