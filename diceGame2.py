# Dice Rolling Game

import random
def dice1():
    print(""" 
                -----
                | x |
                ----- 1 """)
def dice2():
    print(""" 
               -----
               |x  |
               |  x|
               -----  2 """)
def dice3():
    print(""" 
               ------
               | x  |
               |x  x|
               ------  3 """) 
def dice4():
    print(""" 
               ------
               |x  x|
               |x  x|
               ------  4 """)
def dice5():
    print(""" 
               ------
               | x  |
               |x  x|
               |x  x|
               ------  5 """)
def dice6():
    print(""" 
               ------
               |x  x|
               |x  x|
               |x  x|
               ------ 6 """)   

#rand = random.randint(1,6)
def player():
    score = 10
   
    


    rand = random.randint(1,6) 
    if rand == 1:
        print(dice1())
        score *= 1
        print('Your high Score is ',score)
        
    elif rand == 2:
        print(dice2())
        score *= 2
        print('Your high Score is ',score)
        
    elif rand == 3:
        print(dice3())
        score *= 3
        print('Your high Score is ',score)
        
    elif rand == 4:
        print(dice4())
        score *= 4
        print('Your high Score is ',score)
        
    elif rand == 5:
        print(dice5())
        score *= 5
        print('Your high Score is ',score)
        
    elif rand == 6:
        print(dice6())
        score *= 6
        print('Your high Score is ',score)
    return score        
        
def cpu():
    score2 = 10
   


    cpu = random.randint(1,6) 

    if cpu == 1:
        print(dice1())
        score2 *= 1
        print('Your high Score is ',score2)
        
    elif cpu == 2:
        print(dice2())
        score2 *= 2
        print('Your high Score is ',score2)
        
    elif cpu == 3:
        print(dice3())
        score2 *= 3
        print('Your high Score is ',score2)
        
    elif cpu == 4:
        print(dice4())
        score2 *= 4
        print('Your high Score is ',score2)
        
    elif cpu == 5:
        print(dice5())
        score2 *= 5
        print('Your high Score is ',score2)
        
    elif cpu == 6:
        print(dice6())
        score2 *= 6
        print('Your high Score is ',score2)
    
    return score2
        
# def begin():
#     while True:
#         print("player's turn")
#         rollDie = input('Do you want to roll a die  - ').lower()  

#         if rollDie == 'no':
#             print('GAMEOVER!')
#             break
#         elif rollDie == 'yes':
#             player()

#         print("computer's turn")
#         cpu()
#         # rand = random.randint(1,6) 
#         # cpu = random.randint(1,6) 
#         """"if player() < cpu():
#             print('I won')
#         elif player() > cpu():
#             print('You won\n Good job')
#         elif player() == cpu():
#             print("it\'s a tie")"""
        
#         continue
def begin():
    score = [0,0]
    for plays in range(6):
        i = 0
        for _player in [player, cpu]:
            input()
            score[i] += _player()
            i += 1
        print(score)
    player_score = score[0]
    cpu_score = score[1]
    if player_score > cpu_score:
        print('Player Won This game')
    else:
        print('CPU Won This game')

begin()



    



        
                    
