# GLOBAL VARIABLES
player_one_name='PLAYER1'
player_two_name='PLAYER2'

keypad = { '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

allowed_keys=('1','2','3','4','5','6','7','8','9')
entered_keys=[]

player_one_entries= []
player_two_entries= []

player_one_completed = False
player_two_completed = False

player_one_won = False
player_two_won = False

win_outcomes= (
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,5,9],
    [3,5,7],
    [1,4,7],
    [3,6,9],
    [2,5,8]
)

def display_board(**keypad):
    '''
    Displays the tic-tac-toe board
    input: takes keypad input ranging from 1 to 9 in a sequence
    '''
    print(f"         |         |        ")
    print(f"    {keypad['1']}    |    {keypad['2']}    |    {keypad['3']}  ")
    print(f"         |         |        ")
    print(f"------------------------------")
    print(f"         |         |        ")
    print(f"    {keypad['4']}    |    {keypad['5']}    |    {keypad['6']}   ")
    print(f"         |         |        ")
    print(f"------------------------------")
    print(f"         |         |        ")
    print(f"    {keypad['7']}    |    {keypad['8']}    |    {keypad['9']}   ")
    print(f"         |         |        ")

def input_user_entry(player, keymap):
    if player.upper() == player_one_name:
        keypad[keymap]='X'
        display_board(**keypad)
    else:
        keypad[keymap]='O'
        display_board(**keypad)

def receive_user_input_and_validate(player,player_entries, message):
    if not player_one_won and not player_two_won:
        user_input = input(f"{player}, {message}")
        if not (user_input in allowed_keys):
            print('Please enter valid input. Only single digit numbers are alowed from 1 to 9')
            receive_user_input_and_validate(player,player_entries, "Please enter valid input.: ")
        elif user_input in entered_keys:
            print('Please enter valid input. This entry is already recorded.')
            receive_user_input_and_validate(player,player_entries, "Please enter new input in 1 to 9 which are not recorded: ")
        else:
            entered_keys.append(user_input)
            input_user_entry(player, user_input)
            player_entries.append(int(user_input))
            check_result(player, player_entries) 

def initialize_game():
    global player_one_name
    global player_two_name
    player_one_name = input('PLAYER1 please input your name: ').upper()
    player_two_name = input('PLAYER2 please input your name: ').upper()
    start_game_with_specified_player()

def start_game_with_specified_player():
    first_player = input(f'Type the player name who wants to start the game first? ({player_one_name}/{player_two_name}): ')
    if not (player_one_name == first_player.upper()) and not (player_two_name == first_player.upper()):
        print("Please enter correct name of the player who wants to start the game.")
        start_game_with_specified_player()
    else:
        start_game()


def start_game():
    reset_all_player_entries()
    display_board(**keypad)
    for x in range(1,7):
        if x%2==0:
            receive_user_input_and_validate(player_two_name, player_two_entries, 'please enter your input: ')
        else:
            receive_user_input_and_validate(player_one_name, player_one_entries, 'please enter your input: ')

def check_result(player, result):
    global player_one_completed
    global player_two_completed
    global player_one_won
    global player_two_won

    if len(result)==3:
        player_outcome=[]
        for outcome in win_outcomes:
            player_outcome=[]
            for x in result:
                player_outcome.append(x in outcome)
            if all(player_outcome):
                break

        if all(player_outcome) :
            if player == player_one_name:
                player_one_completed=True
                player_one_won=True
            elif player == player_two_name:
                player_two_completed=True
                player_two_won=True
        else:
            if player == player_one_name:
                player_one_completed=True
                player_one_won=False
            elif player == player_two_name:
                player_two_completed=True
                player_two_won=False

        if (player_one_completed and player_one_won) or (player_two_completed and player_two_won):
            print(f'Player {player} won the game.')
            play_again()
        elif player_one_completed and player_two_completed:
            print("It's a tie")
            play_again()

def play_again():
    play_again = input("Do you want to play again(Y/N): ")
    if (play_again.upper()=='Y'):
        print('Starting new game...')
        start_game_with_specified_player()
    else:
        print('Thank you for playing...')
                  
def reset_all_player_entries():
    global keypad
    global entered_keys
    global player_one_entries
    global player_two_entries
    global player_one_completed
    global player_two_completed
    global player_one_won
    global player_two_won

    keypad = { '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

    entered_keys=[]

    player_one_entries= []
    player_two_entries= []

    player_one_completed = False
    player_two_completed = False

    player_one_won = False
    player_two_won = False

print("###################################")
print("####---------------------------####")
print("####        TIC-TAC-TOE        ####")
print("####---------------------------####")
print("###################################")
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print('Welcome to TIC TAC TOE....')
print('Board takes input values from 1 to 9. Postion of each board block follows number postions in mobile phone keypad pad layout.')
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print('')
print('')
initialize_game()