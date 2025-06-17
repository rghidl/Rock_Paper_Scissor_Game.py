import random

choices={"r":"🪨","p":"📃","s":"✂️"}


while True:
    try:
        user_choice=input("Choose Rock, Paper, or Scissors: (r,p,s):").lower()
        computer_choice=random.choice(list(choices.keys()))

        if user_choice not in choices:
            print("❌Invalid choice! Try again.\n")
            continue
        
        print(f"\n Your choice is:{choices[user_choice]}")
        print(f"\n computer choice is:{choices[computer_choice]}")

        if user_choice==computer_choice:
            print("It's a tie!") 
       
        elif ((user_choice == "r" and computer_choice=="s") or
               (user_choice=="p" and computer_choice=="r") or
               (user_choice=="s" and computer_choice=="p")):
            print("\n You win🎉.")
                  
        else:
            print("\n You lose‼️")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! 👋")
            break
    
    except ValueError:
        print("❌ Error")    

