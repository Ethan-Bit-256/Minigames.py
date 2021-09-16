print("WELCOME TO MY GUESSING GAME!!!")

secret_number = "7"

while True:
    Guess = input("Guess the number>>>")
    if Guess != secret_number:
        print("Wrong! Try Again!")
    if Guess == secret_number:
        print("Correct!")
        break

    if Guess != secret_number:
        print("Wrong! Try Again!")
    if Guess == secret_number:
        print("Correct!")
        break

    if Guess != secret_number:
        print("Wrong! Try Again!")
    if Guess == secret_number:
        print("Correct!")
        break
    print("Sorry, It's a loss for you!")
    break
