import random

class Player():

    def __init__(self, uname):
        self.score = 0
        self.uname = uname
        self.last_throw = []

    @staticmethod
    def say_hello():
        print('hello')

    def __getrand(self):#encapsulated method
        return random.randint(1,6)

    
    def throw(self):
        die_one = self.__getrand()
        die_two = self.__getrand()
        self.last_throw = [die_one,die_two]
        self.__add_score(self.last_throw)
        self.__show_dice(self.last_throw)

        return die_one,die_two
    
    def __add_score(self, score):
        self.score += sum(score)

    @staticmethod
    def __show_dice(arg):
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
        print(arg)
        
    def __str__(self):
        return '{}: {}'.format(self.uname,self.score)


class Game():

    def __init__(self, scorelim = 100, plays = 10, player1 = 'user1', player2 = 'user2'):

        self.scorelim = scorelim
        self.plays = plays
        self.p1 = Player(player1)
        self.p2 = Player(player2)

    def begin(self):
        self.p1.score
        self.p2.score

        players = [self.p1,self.p2]
        while self.p1.score < self.scorelim and self.p2.score < self.scorelim:
            for i in range(2):
                input(str(players[i]) +' : Press enter to throw ==>')
                players[i].throw()
        print(self)
        self.declare()

    def reset(self):
        self.p1.score = 0
        self.p2.score = 0
    
    def declare(self):
        winner = self.p1 if self.p1.score > self.p2.score else self.p2
        points = abs(self.p1.score - self.p2.score) 
        print ('{} WON THIS GAME BY {} POINTS'.format(winner,points))
        return ('{} WON THIS GAME BY {} POINTS'.format(winner,points))
    
    def __str__(self):
        return '{}:\t:{}'.format(str(self.p1),str(self.p2))