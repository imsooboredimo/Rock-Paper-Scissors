import random

#options
x = ['Rock','Paper','Scissors']

#rounds
rounds = [1,2,3,4,5]

#score
scores = {
    'YOU': 0,
    'BOT': 0
}

#game
print('START GAME!')
for round in rounds:
    random.shuffle(x)
    for element in x:
        computer = element
        pass
    player = input('Choose: rock, paper or scissors? ')
    print(f'YOU: {player}')
    print(f'BOT: {computer}')
    if player == computer:
        print('TIE!')
        print()
        print('Score:')
        print(scores)
        print()
    elif player == 'Rock':
        if computer == 'Scissors':
            print('YOU WIN!')
            scores['YOU']+=1
            print()
            print('Score:')
            print(scores)
            print()
        elif computer == 'Paper':
            print('YOU LOSE!')
            scores['BOT']+=1
            print()
            print('Score:')
            print(scores)
            print()
    elif player == 'Paper':
        if computer == 'Rock':
            print('YOU WIN!')
            scores['YOU']+=1
            print()
            print('Score:')
            print(scores)
            print()
        elif computer == 'Scissors':
            print('YOU LOSE!')
            scores['BOT']+=1
            print()
            print('Score:')
            print(scores)
            print()
    elif player == 'Scissors':
        if computer == 'Rock':
            print('YOU LOSE!')
            scores['BOT']+=1
            print()
            print('Score:')
            print(scores)
            print()
        elif computer == 'Paper':
            print('YOU WIN!')
            scores['YOU']+=1
            print()
            print('Score:')
            print(scores)
            print()
    else: print('Try Again..')


you = scores['YOU'] 
bot = scores['BOT']

print('END!')
print()
print('Result:')
print(f'YOU: {you}')
print(f'BOT: {bot}')
print()
if you > bot:
    print("YOU'VE FUCKING WIN!")
elif you == bot:
    print('TIE!')
elif you < bot:
    print('YOU LOSE!')