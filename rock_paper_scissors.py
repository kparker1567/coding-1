#In Rock, Paper, and Scissors, you must choose either of the objects, and make it with your hands. If the object you chose counters your opponents object, you win. For instance,
# Rock beats scissors, paper beats rock, scissors beats paper, etc.



import random

def rockpaper_scissors():
    score = 0
    cpu_score = 0
    rounds = 0
    
    print("Welcome to Rock, Paper, and Scissors!")
    print("Rules: Enter r, p, or s to play. Beat the CPU to win points!")
    
    while True:
        if rounds == 3:
            print(" Game Over...")
            print(f"Final Score -> You: {score} points | CPU: {cpu_score} points")
            break

        choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
        
        if choice == 'q':
            print(f"Thanks for playing! Your final score is: {score} points. CPU score: {cpu_score} points.")
            break
            
        elif choice == 'r' or choice == 'p' or choice == 's':
            roll = random.randint(1, 3)
            
            if roll == 1:
                cpu_choice = 'r'
                print("CPU chose: rock")
            elif roll == 2:
                cpu_choice = 'p'
                print("CPU chose: paper")
            else:
                cpu_choice = 's'
                print("CPU chose: scissors")
            
            if choice == cpu_choice:
                print(f"It's a tie! Current score: {score}")
            elif (choice == 'r' and cpu_choice == 's') or (choice == 'p' and cpu_choice == 'r') or (choice == 's' and cpu_choice == 'p'):
                score += 1
                print(f"You win! +1 point. Current score: {score}")
            else:
                cpu_score += 1
                print(f"You lose! CPU wins +1 point. Current score: {score}")
                
            rounds += 1
                
        else:
            print("Invalid input. Please enter 'r', 'p', 's' to play or 'q' to quit.")

rockpaper_scissors()
