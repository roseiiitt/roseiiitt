import random
guess=0
upper_limit=input("Enter a number: ")

if upper_limit.isdigit():
    print("digit")
    upper_limit=int(upper_limit) 

    if upper_limit <= 0:
        print("Type larger than 0")
        quit()

else:
    print("enter a digit next time:")
    quit()

random_number=random.randrange(upper_limit)
print(random_number)

while True:
    guess+=1
    user_input = input("Make a guess: ")
    if user_input.isdigit():
        user_input=int(user_input) 

    else:
        print("enter a digit next time:")
        continue

    if user_input == random_number:
        print("You nailed it:")
        break
    
    else :
        print("It doesn't match:")
    
    if guess >= 3:
        quitting=input("Do you want to continue guessing: ").upper()
        if quitting != "YES":
            quit()
      


print("You got it in ",guess,"guesses")
