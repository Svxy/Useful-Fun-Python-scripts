print ("The Fucking Number Guessing Game")
print ("--------------------------------")

import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, so its yours bruh.")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Sup nigga! Welcome to the game of the guesses!")
    player_name = input("Whats your name yo? ")
    wanna_play = input("Gang shit {} wanna play mane? u fw number guessing? (Yee/Nahh) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yee":
        try:
            guess = input("ight now, pick a number between 1 and 15 ")
            if int(guess) < 1 or int(guess) > 15:
                raise ValueError("now guess yo shit")
            if int(guess) == random_number+1:
                print("DAAMNNN! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts so like shiii".format(attempts))
                play_again = input("wanna play again? (Yee/Nahh fuck this shit) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "nahh fuck this shit":
                    print("lol ight..")
                    break
                else:
                    print("you deadass gotta type fuck this shit")
            elif int(guess) > random_number:
                print("Lower nigga..")
                attempts += 1
            elif int(guess) < random_number:
                print("Higher buster")
                attempts += 1
        except ValueError as err:
            print("Numbers not valid dumbass")
            print("({})".format(err))
    else:
        print("Ight mane have a good one")
if __name__ == '__main__':
    start_game()