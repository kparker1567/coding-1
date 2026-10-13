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
    