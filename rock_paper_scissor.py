import random

opt=["rock", "paper", "scissor"]
user=0
compt=0
draw=0
while True:
    inputt=input("Type rock/paper/scissors or q to quit: ").lower()
    if inputt == "q":
        break
         
    if inputt not in ["rock", "paper", "scissor"]:
        print("Please choose correctly")
        continue
    rand_num=random.randint(0,2)
    # 0 -> Rock  1 -> paper  2 -> scissor 
    com_guess = opt[rand_num]
    print("Computer picked",com_guess,".")


    if inputt == "paper" and com_guess=="rock":
        print("You win:")
        user+=1
        continue
    
    elif inputt == "rock" and com_guess=="scissor":
        print("You win:")
        user+=1
        continue 

    elif inputt == "scissor" and com_guess=="paper":
        print("You win:")
        user+=1
        continue

    elif inputt == "scissor" and com_guess=="scissor":
        print("Draw")
        draw+=1
    elif inputt == "paper" and com_guess=="paper":
        print("Draw")
        draw=draw+1
    elif inputt == "rock" and com_guess=="rock":
        print("Draw")
        draw=draw+1

    else:
        print("You Lose:")
        compt+=1
        continue


print("You wins",user,"times")
print("Computer wins",compt,"times") 
print("Draw = ",draw)







print("Bye!")
     
