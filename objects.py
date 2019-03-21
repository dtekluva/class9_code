class Person():
    species = 'homosapien'
    stomach = []
    
    def __init__(self, name = 'noname', legs = 2, hands = 2, height = 2):
        self.name = name
        self.legs = legs
        self.hands = hands
        self.height = height
        self.is_short = True if height < 1.2 else False

    def eat(self, food):
        if food == 'beans':
            print('Yeeenhh!!!... I dont like beans joor.')
            return

        self.stomach.append(food)

    def walk(self, dist):
        steps = 2
        if self.is_short: steps = 1

        for i in range(1,dist,steps):
            print(self.name,' is Taking step {}'.format(i))

class Warrior(Person):
    def fight(self):
        print('i am fighting i can fight')

class Swimmer(Person):
    def swim(self):
        print('i am swimming')

class Agebero(Warrior):

    def __init__(self, name, height, bata = 'origo'):
        super(Agebero, self).__init__( name = name, height = height )
        self.bata = bata

    def gba_owo_union(self):
        print('moti gba shandy...')
    
    # def __str__(self):
    #     return self.name

person1 = Agebero(name = 'Ade',height = 3)
person2 = Person(name ='Paul', height =0.9)
person3 = Agebero(name ='Kiyoshi', height =0.9)
# person1.walk(10)
# print(person1.is_short)
# person2.walk(10)
# print(person2.is_short)
person1.fight()
person3.gba_owo_union()
# person3.name = 'olamide'
print(person3.name)
print(person3.legs)
print(person3.height)
print(person3.hands)













        

# class kid(Person):

    
#     def __init__(self, species = 'baby', name = 'noname', legs = 2, hands = 2):
#         Person.__init__(self, name = 'noname', legs = 2, hands = 2)
#         self.species = 'baby'

# omo = kid(name = 'winston')

# print(omo.species)
# print(omo.name)