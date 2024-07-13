import random
def guessing_game():
    print("/nwelcome to the rock,paper,scissors game!")
    print("choices:rock,paper,scissor/n")
    items=["paper","rock","scissor"]
    rand=random.choice(items)
    attempts=0
    while True:
        user_choice=input("enter your choice:").lower()
        if user_choice=="exit":
            print("game ended:")
            break
        elif user_choice== rand:
            print("congratulations u won!")
            print(f"u won game by guessing correct output(user_choice) and in (attempts+1) attempts/n")
            play_again=input("if u want to play again,enter 'yes',else type 'exit' to quit:").lower()
            if play_again!='yes':
                print("thanks for playing!")

            else:
                guessing_game()
        else:
                print("try again!")
                attempts=attempts+1
guessing_game()
