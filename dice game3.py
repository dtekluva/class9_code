import random

scores = [0,0]
players = ['','']
high_score = 0

def get_players():
    global high_score
    high_score = int(input('PLEASE ENTER A HIGH SCORE LIMIT : '))
    player1 = input('Player 1 enter nick : ')
    players[0]= player1
    player2 = input('Player 2 enter nick : ')
    players[1]= player2

def getrand():
    return random.randint(1,6) 

def throw():
    die_one = getrand()
    die_two = getrand()

    return die_one,die_two

def score(val):
    scores[0] += val[0]
    scores[1] += val[1]
    print('SCORES=====>',players)
    print('SCORES=====>',scores)

def show(result):
    
    for i in result: 
        if i == 6:
            print('+-----+' )
            print('| *** |' )
            print('| *** |' )
            print('+-----+' )
        elif i == 5:
            print('+-----+' )
            print('| **  |' )
            print('| *** |' )
            print('+-----+' )
        elif i == 4:
            print('+-----+' )
            print('| *   |' )
            print('| *** |' )
            print('+-----+' )
        elif i == 3:
            print('+-----+' )
            print('|     |' )
            print('| *** |' )
            print('+-----+' )
        elif i == 2:
            print('+-----+' )
            print('|     |' )
            print('| **  |' )
            print('+-----+' )
        elif i == 1:
            print('+-----+' )
            print('|     |' )
            print('| *   |' )
            print('+-----+' )

def begin():
    get_players()
    _score = [0,0]
    global high_score
    print(high_score)
    while scores[0] < high_score and scores[1] < high_score:
        for i in range(2):
            input(players[i]+' : Press enter to throw ==>')
            value = throw()
            show(value)
            _score[i] = value[0]+value[1]
        score(_score)

begin()