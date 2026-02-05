import random
def play_game():
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]
    print("--- Welcome to Rock-Paper-Scissors! ---")
    #print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("\n--- Final Results ---")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")
if __name__ == "__main__":
    play_game()
