x = 0
y = 5

# if x < y:                           
#     print('yes')
#     print("y is", bool(y), ", x is", bool(x), "and the if statement got", x < y)


# if y < x:                           
#     print('yes')
#     print("y is", bool(y), ", x is", bool(x), "and the if statement got", y < x)
# else:
#     print('Failed')
#     print("y is", bool(y), ", x is", bool(x), "and the if statement got", y < x)

# if x:                               
#     print('yes')
#     print("y is", bool(y), ", x is", bool(x), "and the if statement got", bool(x))
# else:
#     print('Failed')
#     print("y is", bool(y), ", x is", bool(x), "and the if statement got", bool(x))

# if y:                               
#     print('yes')



# if x or y:                          
#     print('yes')


# if x and y:                         
#     print('yes')
# else:
#     print("no")

# test = "shayo"
# name = 'Feyishayo'
# letter = "s"

# if test in name:               
#     print('yes', name, "contains ", test)
# elif letter in name:
#     print(name, "does not contain ", test, ". But contains", letter)
# else:
#     print('No', name, "does not contain ", test, "and does not contain the letter", letter)

# response =  int(input("Please enter a number to test : "))

# if response%2 == 0:
#     print(f"{response} is an even number ")
# else :
#     print(f"{response} is not an even number ")


# headache_response = input("Do you have a headache .? respond y/n : ")

# if headache_response == "y": #check for headache

#     fever_response = input("Do you have a fever .? respond y/n : ")

#     if fever_response == "y": #check for fever

#         vomit_response = input("Have you vomitted .? respond y/n : ")

#         if vomit_response == "y": #check for vomit

#             print("you have Typhoid, please see a doctor")
        
#         elif vomit_response == "n": #check for no vomit
#             print("you have Malaria, please see a doctor")

#     elif fever_response == "n": #check for no fever:
#         print("You are probably just stressed out try to rest. ")
        

# elif  headache_response == "n": #check for no headache
#     print("You are probably okay or maybe see a medical practitioner")

# if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
# x = 20
# if x == 20 : print(x), print("next statement"), print("happy syntax") #Probably unreadable syntax too many single line statements
# if x == 20 : break #Acceptable

#TENARY OPERATOR

"""<expr1> if <conditional_expr> else <expr2>"""

# user_input = input("please enter your name in caps")

# name = user_input if user_input.isupper() else "input was not upper case"

# print(name )

score = int(input("please enter your students score"))

status = "Qualified" if score >= 60 else "Not qualified"
print(status)

student_is_qualified = True if score >= 60 else False

if student_is_qualified :
    print("\nSending mail to student\n")
    print("Coontent: You have qualified for admission please visit our page to continue your registration")


# if 'quux' in ['foo', 'bar', 'baz']: 
#     print('yes')

# boys_age = 18
# boys_gratitude = "merci"
# list_of_gratitudes = ["ese", "thanks", "daalu", "nagode", "merci"]

# if boys_age >= 21:
#     winner = "pdp"
#     print("You are of the right age")
#     payment = boys_age *100
#     print("Take ", str(payment) + "USD")
#     print("Please spend the money wisely")

#     if boys_gratitude in list_of_gratitudes:
#         print("\nYou are a good shyd")
    
#     else:
#         print("Else on inner 'If'")
# else:
#     winner = "apc"
#     print("Else on outer 'If'")

# print(winner)

# name = 'Chidi'
# if name == 'Tolu':
#     print('Hello Tolu')
# elif name == 'Tayo':
#     print('Hello Tayo')
# elif name == 'Chidi':
#     print('Hello Chidi')
# elif name == 'Shade':
#     print('Hello Shade')
# else:
#     print("I don't know who you are!")

# name = input("Please enter your name")
# names = {
#      'Chidi': 'Hello Chidi',
#      'Tayo': 'Hello Tayo',
#      'Tolu': 'Hello Tolu',
#      'Femi': 'Hello Femi'
#  }

# print(names.get(name, "I don't know who you are!"))

# def foo():
#     print('hello i am a function')

# population = 100000
# votes = 225000
# election_was_violent = True

# if  votes <= population: print('This was a fair election') #;print("this is awesome")

# debugging = True  # Set to True to turn debugging on.

 

# if debugging: print('About to call function foo()'); foo()

# if population > votes :
#     print("Fair election")
# elif election_was_violent :
#     print("Bad election")

# age = 30

# print("you are an", "Adult " if age > 18 else "adolescent")

# it_is_raining = False

# print("We are going ", "to stay home " if it_is_raining else "to the beach")

# if True:
#     pass
# else:
#     pass
