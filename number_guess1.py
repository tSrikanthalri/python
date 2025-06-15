import random #Python’s random module, which gives you tools to generate random numbers.


secret_number = random.randint(1,100) #This picks a random number between 1 and 100
print("WELCOME TO THE GAME NUMBER GUESS")

while True:  #This loop keeps asking the player to guess until they get it right.

    guess_number = input("ENTER YOUR GUESS NUMBER : ")

    if not guess_number.isdigit():   #Checks if the input is a number. If not (like text or symbols), it shows an error and restarts the loop using continue.
        print("ENTER VALID NUMBER")
        continue

    guess_number = int(guess_number) #Converts the valid numeric input from a string to an integer, so you can compare it with the secret number.
    
    if (guess_number < 1 or guess_number > 100): #Ensures the number is within the allowed range (1–100). If not, gives a warning and restarts the loop
        print("YOUR GUESS IS OUT OF RANGE ! TRY BETWEEN 1 TO 100")
        continue

     
    if guess_number < secret_number:  #If the guess is less than the secret number, it tells the user it’s too small.
         print("TOO SMALL GUESS TRY AGAIN")
    elif guess_number > secret_number:  #If the guess is less than the secret number, it tells the user it’s big small.
         print("TOO BIG GUESS TRY AGAIN")
    else:                              #If the guess matches the secret number, it congratulates the user and break statement ends the while loop and finishes the game.
        print("CONGRATULATIONS YOU WIN")
        break


