import random


def print_ascii(inputs):
    if inputs == 1:
        print("""
            __________
        ---'   _______)
              (________)
              (________)
              (_______)
        ---.__(_____)
        """)
    elif inputs == 2:
        print("""
             _______
        ---'    ____)________
                   __________)
                  ____________)
                 ___________)
        ---.____________)
        """)
    elif inputs == 3:
        print("""
            _______
        ---'   ____)_________
                  ___________)
               ______________)
              (_____)
        ---.__(____)
        """)
    else:
        print("*Invalid input*")


status = True

while status:
    user_input = int(input("What do you choose? Type 1 for rock, 2 for paper or 3 for scissors\n"))
    computer_choice = random.randint(1, 3)
    print_ascii(user_input)
    print("Computer chooses:")
    print(computer_choice)
    print_ascii(computer_choice)

    # result part
    if user_input == computer_choice:
        print("It's a tie!")
    elif user_input == 1 and computer_choice == 2:
        print("You lose.")
    elif user_input == 1 and computer_choice == 3:
        print("You win!")
    elif user_input == 2 and computer_choice == 1:
        print("You win!")
    elif user_input == 2 and computer_choice == 3:
        print("You lose.")
    elif user_input == 3 and computer_choice == 1:
        print("You lose.")
    elif user_input == 3 and computer_choice == 2:
        print("You win!")
    else:
        print("Invalid input was entered.")

    print("Do you want to play again? Type 1 for yes, 2 for no")
    user_in = int(input())
    if user_in == 2:
        status = False
        print("Thanks for playing!")
        continue
    elif user_in == 1:
        status = True
        continue
    else:
        status = False
        print("Invalid input. Anyway... Bye.")
        continue
