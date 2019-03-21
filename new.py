# x = []
# y = ("ghol",)
# z = {'key': "value"}
# a = {}

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))


# x = [1,2,3,4,5]
# x = tuple(x)
# print(x)

# mass =  int(input('ENTER MASS IN KG : '))
# height = int(input('ENTER HEIGHT IN METRE : '))
# height = height ** 2
# BMI = mass/height
# print('YOUR BMI IS : ', BMI)

# time = 4
# rate =2/100

# principal = int(input('Enter the amount your want to borrow : '))
# interest = principal * rate * time
# print('You want ',principal,'loan , your interest is ', interest ,'at',rate*100,'% for ', time,'months' )

# thing = list(input('Enter anything '))
# ChangeToTuple= tuple(thing)
# print(thing)
# print(ChangeToTuple)

# word = 'people are bad'
# findWord = input('Find what?  ').lower()
# if findWord in word:
#     print('True')
# else:
#     print('false')


# uname='men2'
# _pass = 'pass'

# username = input('Please enter username:  ').lower()
# userpassword = input('Please enter password:  ').lower()

# x = (username == uname and _pass == userpassword)
# y = print('login' if x == True else 'Wrong password')

import re
# baby_names = open("html.html","r") # open and 'r' read  'w' write 'a' append
 

# name_str = baby_names.read()#assign csv data to variable
# baby_names.close()
# print(name_str)
text = 'Hello world i am 2018 testing and hello learining regular expressions 2018 testing and hello using cats and dog with tutorials point its quite interesting'

# exp = r'[0-9][0-9][0-9][0-9].'
exp = r'[0-9]+.'

x = re.search(exp,text)
if x:
    print(x.group())
else:
    print('no match')