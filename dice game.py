import random

def getrand():
    return random.randint(1,6) 

def throw():
    die_one = getrand()
    die_two = getrand()

    return die_one,die_two
 
def gen_dice(values):
    for val in values:
        _list = [val,0]
        if val > 3:
            _list = [3, val - 3] 

        def print_closure():
            print('+-----+ ' )
        
        def print_nos():
            print_closure()
            for i in sorted(_list):
                print('| '+('*'*i).center(3)+' |' )
            print_closure()
        print_nos()

gen_dice(throw())