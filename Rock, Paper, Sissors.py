import random

def user_input ():
    choices = ('rock', 'paper', 'sissor')
    user_input = ''
    #loop until user input rock, paper or sissor
    while user_input not in choices:
        user_input = input('Enter a choice(rock, paper, scissors: )').capitalize()
        continue
    return user_input

def computer_generated_selection():
    choices = ['Rock', 'Paper', 'Scissors' ]
    # choice() method returns a randomly selected element from the specified sequence
    computer_selection = random.choice(choices)
    return computer_selection

#determine a winner for each round and keep track of score  
def determine_winner(player_choice, computer_choice):
    global player_score
    global computer_score

    if player_choice == computer_choice:
        print('Both player selected {}. Its a draw!'.format(player_choice))
    
    elif player_choice == 'Rock':
        if computer_choice == 'Sissors':
            print('Rock smashes scissor! you win!')
            player_score += 1
        else:
            print('Paper covers rock!, you lose.')
            computer_score += 1
   
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper Cover Rock! you Lose.")
            computer_score += 1
        else:
            print("Scissors cut paper! You lose.")
    
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cut paper!, You Win")
        else:
            print("Rock smashes scissor!. You lose")
            computer_choice +=1

def play_again():
    replay = input('Would You like to play again? (Y/N): ')
    if replay.lower() == 'y':
        return True
    else:
        return False

player_score = 0
computer_score = 0           

while True:
    print('Welcome to Rock Paper Game!')
    print('Current Score: ')
    print('Player {} | {}'.format(player_score, computer_score))

    player_choice = user_input()
    computer_choice = computer_generated_selection()

    print('You chose {}, Computer chose {}'.format(player_choice, computer_choice))

    determine_winner(player_choice, computer_choice)

    print('The current score is: ') 
    print('Player {} | {}'.format(player_score, computer_score))

    if not play_again():
        print('Hope to see you again!')
        break