# importing useful libraries
import random
import datetime


class Dice:
    # Dice class that creates the roll feature we use to roll the dice
    def __init__(self, sides=20):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


def input1():
    # Simple greeting message
    print('Welcome to a made up dice game. ')
    name = input('What is your name?: ')
    print(f'Hello {name} welcome')
    return name


def process1(name):
    plays = []
    # Setting the dice to be a 20 sided one
    d20 = Dice(20)
    # Validation to endure we get a number and some instructions
    while True:
        try:
            guess = int(input("Please enter your guess. "
                              "\n The goal is to make sure the total of the rolls are higher than 100 and your guess is"
                              " in one of"
                              " the 10 rolls "
                              "\n Note this is a 20 sided dice! "))
            break
        except Exception as e:
            print('Please enter an number!')

    # Loop to roll the dice 10 times, add the numbers into a list and get the total 
    for r in range(1, 11):
        j = d20.roll()
        plays.append(j)
        sum_plays = sum(plays)
    #If statement to see if the guess more than 100 and if its in one of thee 10 rolls
    if guess in plays and sum_plays > 100:
        print(f'You were right {name}, {guess} was in the list of rolls and the total is above 100 \n Total is: {sum_plays}')
    else:
        print("Lady luck does not seem to be on your side today. Try again next time")


def time():
    # Function to get the time and greet the user
    if datetime.datetime.now().hour < 12:
        print('Good Morning!')
    elif datetime.datetime.now().hour >= 17:
        print('Good Evening!')
    else:
        print('Good Afternoon!')


def main():
    # simple time based greeting message
    time()
    # exception handling if anything goes wrong
    try:
        name = input1()
        process1(name)
        # prompting the user to start over
        restart = input('\nDo you want to restart? yes or no')
        if restart == 'yes':
            main()
        else:
            exit()
    # More exception handling
    except Exception as err:
        print(err)


main()
