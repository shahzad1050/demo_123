import random

def play():
    user = input("what is choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == (computer):
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'you won!'
    return' you lost!'

def is_win (player, oppnent):
    if player == ('r' and oppnent == 's') or (player == 's' and oppnent =='p') or player == ('p' and oppnent == 'r'):
        return True
    return False  
  
result = play()
print(result)

