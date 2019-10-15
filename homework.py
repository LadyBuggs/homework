import random

users = {}

def number_of_players():
    number = input('How many players? ')
    return int(string_to_numbers(number))

def print_instruction(username):
    print('\nWelcome', username, 'to the Guessing Game!')
    print("\nYou will have three chances to guess the randomly generated number.\nAfter each guess, you'll receive a hint.")
    print("\nWhen the game is over, you'll have the chance to play again.")
    print('Type "yes" to play again and "no" to end the game.')

def string_to_numbers(arg):
    switch = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
        'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
    return switch.get(arg.lower(), arg)

def end_game_results(data):
    for name in data:
        game_round = 1
        total_rounds = len(data[name])
        wins = abs(data[name].count(0) - total_rounds)
        print('{} played {} rounds. '.format(name, total_rounds))
        #displays each round and the score
        for score in data[name]:
            print('    Round {}: Score = {}    '.format(game_round, score))
            game_round +=1
        print('You won {} Rounds out of {}. '.format(wins, total_rounds))
        print(' -- Total Score : {} -- \n'.format(sum(data[name])))
    

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
                    user_input = int(string_to_numbers(input('Guess a number between 1 thru 10. ')))
                    break
                except ValueError:
                    print('Invalid input, try again.')
            if user_input > computer_guess:
                print('Nice try {}, but your guess is too high.'.format(username))
            elif user_input < computer_guess:
                print('Nice try {}, but your guess is too low.'.format(username))
            else:
                break
        if user_input == computer_guess:
            print('Congratulations {}! YOU WON!'.format(username.upper()))
            users[username].append(3-tries)
        else:
            print('Sorry {}. You lost.'.format(username))
            users[username].append(0)
        print('The number was {}'.format(computer_guess))

        if input("\nPlay again? ").lower()[0] == "n":
            print('\nGood-bye {}!'.format(username))
            #print(users)
            #print(end_game_results(users[username]))
            break

count = 0
loop = number_of_players()
while count < loop:
    play_game()
    count += 1
print(end_game_results(users))
