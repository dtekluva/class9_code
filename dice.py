import random

def getrand():
    return random.randint(1,6) 

def throw():
    die_one = getrand()
    die_two = getrand()

    return die_one,die_two

def gen_dice(arg):
    list1, list2 = [arg[0],0], [arg[1],0]
    
    if arg[0] > 3:
        list1 = [3, arg[0] - 3] 
    if arg[1] > 3:
        list2 = [3, arg[1] - 3] 
    _list = list1 + list2
    def print_closure():
        print('+-----+  +-----+' )
    
    def print_nos():
        print_closure()
        for i in range(2):
            print('| '+('*'*_list[i]).center(3)+' | ' +' | '+('*'*_list[i+2]).center(3)+' |' )
        print_closure()
    print_nos()

gen_dice(throw())