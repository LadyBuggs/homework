import random

users = {}

def print_instruction(username):
    print('\nWelcome', username, 'to the Guessing Game!')
    print("\nYou will have three chances to guess the randomly generated number.\nAfter each guess, you'll receive a hint.")
    print("\nWhen the game is over, you'll have the chance to play again.")
    print('Type "yes" to play again and "no" to end the game.')


def play_game():
    username = input('Hi! What is your name?\n').capitalize()
    users[username] = []

    print_instruction(username)

    while True:
        print('\n')
        computer_guess= random.randint(1,10)
        for tries in range(3):
            while True:
                try:
                    user = int(input('Guess a number between 1 thru 10. '))
                    break
                except ValueError:
                    print('Invalid input, try again.')
            if user > computer_guess:
                print('Nice try {}, but your guess is too high.'.format(username))
            elif user < computer_guess:
                print('Nice try {}, but your guess is too low.'.format(username))
            else:
                break
        if user == computer_guess:
            print('Congratulations {}! YOU WON!'.format(username.upper()))
            users[username].append(3-tries)
        else:
            print('Sorry {}. You lost.'.format(username))
            users[username].append(0)
        print('The number was {}'.format(computer_guess))

        if input("\nPlay again? ").lower()[0] == "n":
            print('\nGood-bye!')
            print(users)
            break

play_game()
#play_game()
