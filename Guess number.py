number = 18
number_of_Attempt = 1
while number_of_Attempt <= 9:
    guesses = int(input("enter the number\n"))

    if guesses > 18:
        print("your guesses is greater than number ")


    elif guesses < 18:
        print("your guesses is lesser than number")
    else:
        print("nice! you won.")
        print(number_of_Attempt, "number of guesses you took to finish")
        break
    print(9 - number_of_Attempt, "number of guesses left")
    number_of_Attempt = number_of_Attempt + 1

if number_of_Attempt > 9:
    print("game over")
