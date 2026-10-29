import random

def dice_rolling_game():
    score = 0
    
    print("Welcome to my Dice Rolling Game!")
    print("Rules: Roll a 7 to win 10 points. Roll anything else and lose 5 points.")
    
    while True:
        choice = input("Enter 'r' to roll the dice or 'q' to quit: ")
        
        if choice == 'q':
            print(f"Thanks for playing! Your final score is: {score} points.")
            break
            
        elif choice == 'r':
            roll = random.randint(1, 7)
            print(f"You rolled a: {roll}")
            
            if roll == 7:
                score += 10
                print(f"You win! +10 points. Current score: {score}")
            else:
                score -= 5
                print(f"You lose! -5 points. Current score: {score}")
                
        else:
            print("Invalid input. Please enter 'r' to roll or 'q' to quit.")

dice_rolling_game()
