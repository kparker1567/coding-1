# Loop - a loop is a construct (special function) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop and While loop

# While loop - a type of loop where so long as a condition is ewual
# to true it will keep running "forever".

# the keyword is while - - > do while

# syntax
num = 4
#while 2+2 == num: # Condition - -> operations -  must be TRUE
   # print("The program is now running")
  #  num = int(input("Please type in any number but 4 to stop the program"))


    # While loop will ALWAYS run unless you change the condition!
    # we can do this by writing instructions to manually change it.
    # The computer must ALWAYS complete their tasks before moving to the next step.

def guessingGame():
        correctAnswer = 8
        attempts = 0
        print("WELCOME TO THE GUESSING GAME")
        print("Please type in a number between 1 and 10")

        userGuess = int(input("Please type in a number:"))

        while userGuess != correctAnswer:
            print("Sorry, that isn't the correct answer. Guess again!")
            attempts+= 1
            print("attempts")
            userGuess = int(input("Please try another number:"))

            print("Congrats! You've guessed the correct answer. game overrr")

guessingGame()




# Question 1
# password reset function. Your function should take in a user password as an input.
# Within the function there should be a 
# variable that contains the correct password.
# the user should be able to attempt to enter the password 4 times.
# On the fourth attemot fof getting the passowrd incorect,
# it should print out a message telling the user that
# their accoutn has been lcoked. If the user gets the password
# correct it should print out a message telling them
# they can access their account.




def passwordReset():
        correctPassword = '9383'
        attempts = 4

        print("Welcome, please enter your password")
        userPassword = input()
    
        

        while userPassword != correctPassword and attempts > 0:
            print("Sorry, that isn't the correct Password")
            attempts -= 1
            print("number of attempts left: " + str(attempts))
            userPassword = input("Please try again")
        print("You are locked out, try again in the next 15 minutes...")

        else
        print("You now have access...")
            

            
        

            

passwordReset()   
