# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# conditional syntax (how it is written)
bill_amount = int(input("Please type in a bill tender (1s, 5s, or 10s):"))

# if usually indicates that something is a possible option
if bill_amount == 1:
    print("Here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quarters")
elif bill_amount == 10:
    print("here are 40 quarters")

elif bill_amount == 20:
    print("Sorry we dont accept 20s")
#else is ALWAYS your last option    

else:
    print("Sorry that type of bill is not accepted.")



def college():
    grade= int(input("Please type in your grade:"))
    if grade > 90:
        templeU()
    else:
        ccp()

def templeU():
    print("Congrats you meet the requirement for temple U")
    print("238293")

def ccp():
    print("It looks like your GPA does not meet the requirements, BUT you can apply your CCP code")
    print("a7ds78sd")

    
college()

    


def calculate_add():
    print("program has started: please type in 2 numbers to add")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("Program has ended")

def calculate_subtract():
    print("program has started: please type in 2 numbers to subtract")
    num1 = int(input())
    num2 = int(input())
    print( num1 - num2)
    print("Program has ended")

def calculate_multiplication():
    print("program has started: please type in 2 numbers to multiply")
    num1 = int(input())
    num2 = int(input())
    print( num1 * num2)
    print("Program has ended")

def calculate_division():
    print("program has started: please type in 2 numbers to divide")
    num1 = int(input())
    num2 = int(input())
    print( num1 / num2)
    print("Program has ended")

def mainCalculator():
    print("main calculator is running...")
    selection = int(input())
    if selection == 1:
        calculate_add()
    elif selection == 2:
        calculate_subtract()
    elif selection == 3:
        calculate_multiplication()
    elif selection == 4:
        calculate_division()
    else:
        print("sorry I dont understand your selection")

mainCalculator()



def movie_ticketprogram():
    print(Program has started: please type in a number)
    selection = int(input())
    if selecton = 1-7
        

   