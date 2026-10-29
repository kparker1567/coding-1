def vending_Machine():
    B3 = "nachochips"
    G4 = "bbqchips"
    G7 = "plainchips"
    D3 = "water"
    G5 = "colasoda"
    Q = 'Quit'
    
    print("Welcome to our vending machine!")
    
    userChoice = ""
    while userChoice != 'Q':
        print("Please enter an item code: ")
        userChoice = input()
        
        if userChoice == 'B3':
            print("Here are your Nachos, would you like anything else?")

        elif userChoice == 'G4':
            print("Here are your barbecue chips, would you like anything else?")

        elif userChoice == 'G7':
            print("Here are your Plain chips, would you like anything else?")

        elif userChoice == 'D3':
            print("Here is your water, would you like anything else?")
            
        elif userChoice == 'G5':
            print("Here is your coca cola, would you like anything else?")
            
        elif userChoice == 'Q':
            print("Have a good day.")
            break
        else:
            print("Invalid Input. Please enter a valid input to proceed with your purchase.")
        

vending_Machine()

# I searched up what break meant so I could use it to end the loop. I was kind of confused on how to end the loop any other way
                
        

