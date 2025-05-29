import random 

emojis = {"r": "🪨", "p" : "📄", "s": "✂️"}

while True:
    choices = ("r", "p", "s")
    user_choice = input("choose (r,p,s): ")

    if user_choice not in choices:
        print("INVALID INPUT")
        exit()

    computer_choice = random.choice(choices)

    print(f"you chose {emojis[user_choice]}")
    print(f"computer chose {emojis[user_choice]}")

    if computer_choice == user_choice:
        print("Tie!!!")
    elif ((user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p")):
        print("you won")
    elif ((user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r")):
        print("you lost")

    should_continue = input("Do you want to continue (Y/N): ").lower()
    if should_continue == "n":
        break


