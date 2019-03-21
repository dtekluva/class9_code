# food = {'carb': 'yam', 'protein':'meat', 'vit':'veges'}

# print('\nOriginal dictionary ==>', food)

# print('\n',food['carb']) #accessing a key-value pair (carb)

# food['fat'] = 'oils'

# print('\nfood dict ==> after adding fats ===> ', food)

# print('\nAccessing the fat value',food.get('fat'))

# print('keys in dict==> ',food.keys() )
# print('Values in dict==> ',food.values() )
# print('\n')

# for key in food:
#     print(key,' : ',food[key])

# stud = {'ali':['math','english'],'kola':['history'],'atha':['math','history','chemistry']}
# x = {'ali': ['math', 'english', 'chemistry'], 'kola': ['history', 'chemistry', 'math'], 'atha': ['math', 'history', 'chemistry']}
# for key in stud:
#     print(key, ' : ', x[key])
# for key in stud:
#     print('\n',key, ' : ')
#     for subject in x[key]:
#         print('\t',subject)
#         for letter in subject:
#             print('\t\t',letter)


# name = input('Please enter your name : ')
# hobbies = input('Please enter your hobbies seperated by commas: ')

# py_pips[name] = hobbies.split(',')

# for key in py_pips:
#     print('\n',key, ' : ')
#     print('\t HOBBIES')
#     for hobbies in py_pips[key]:
#         print('\t',hobbies)

py_pips = {}
py_pips.fromkeys('hello')
def manually_input():
    '''This function asks for input'''
    name = input('Please enter your name : ')
    hobbies = input('Please enter your hobbies seperated by commas: ')
    py_pips[name] = hobbies.split(',')
    # print(py_pips)
    show()

def show():
    for key in py_pips:
        print('\n',key, ' : ')
        print('\t HOBBIES')
        for hobbies in py_pips[key]:
            print('\t',hobbies)



data = [('ola','dancing,movies,food',),
        ('nelson','singing,maths,history',),
        ('Ubong','movies,football,cooking',),
        ('ada','reading,video games,travelling',)]

for person in data:
    py_pips[person[0]] = person[1].split(',')

for key in py_pips:
    print('\n',key, ' : ')
    print('\t HOBBIES')
    for hobbies in py_pips[key]:
        print('\t',hobbies)

manually_input()
# print(py_pips)