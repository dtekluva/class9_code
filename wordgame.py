import random

months = ['jan','feb','mar','apr']
print(random.randint(0,3))
word = months[random.randint(0,3)]

def check(user_input):
        
        if user_input == word:
                print('You were right')
        else:
                print('You were wrong')
    

user_input = input('Tell me what i picked  jan, mar, apr : ')
check(user_input)