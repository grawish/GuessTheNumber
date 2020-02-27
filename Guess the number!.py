secret_number = 6                             #this is the secret number 
guess_count = 0                             #number of guess count made
guess_limit = 3                                #maximum number of guess 
while guess_count < guess_limit :              #while loop
    guess = int(input("enter the number : "))  #enter the number
    guess_count += 1                           #increment every guess
    if guess ==secret_number:                  #if statement
        print(" Voila ! You won!")             #print statement
        break                                  #break statement
else:                                          #else statement
    print("Sorry! You Lose!")                  #print statement