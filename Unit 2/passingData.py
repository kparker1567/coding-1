# when we are building complex programs, we need a 
# way to pass in data that is NOT always
# from the user

# Function arguments and parameters are ways to
# pass in data to a function from possibly
# another function.

# fUNCTION PARAMETERS- tHIS IS placeholder data FOR
# A FUNCTION. VARIABLES INSIDE THE CURLY BRACKETS

# MEMORY TRICK- PARAMETER AND PLACEHOLDER BOTH
# START WITH THE LETTER P

def check_Water_Depth(depth, volume, acidic, temperature):
    print(depth)
    print(acidic)
    print(temperature)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth



    #Function arguments- This is the REAL DATA that we pass into
    # the function call.
    # memory trick- if you make a REAL world argument with a person
    # you need to come with REAL facts (data)
check_Water_Depth(7, 100, False, 78)

    # return - this keyword allows us to pass data from INSIDE 1 function 
    # into another function

def username():
    name = input('plesae type in user name:')
    return name

def confirmLogin():
    name = username()
    print(name)
    
#username()
confirmLogin()








