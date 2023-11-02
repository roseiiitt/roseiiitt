print("Welcome to quiz!")
''' checking'''
play = input("Do you want to play? ")

if play.lower() != "yes" :
    print("See You Again")
    quit()

score=0
print("Let's play")

answer=input("What does CPU stands for? ")

if answer.lower() == "cpu" :
    print("Correct")
    score+=1
else :
    print("Not Correct!")

#next question

answer=input("What does RAM stands for? ")

if answer.lower() == "ram" :
    print("Correct")
    score+=1
else :
    print("Not Correct!")

#next question

answer=input("What does GPU stands for? ")

if answer.lower() == "gpu" :
    print("Correct")
    score+=1
else :
    print("Not Correct!")
    
print("You got " +  str(score) + " answers correct")

