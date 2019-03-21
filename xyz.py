#fname = input("What is your Firstname\n")
#lname = input("What is your Lastname\n")
#age = input("tell me your sge\n")

##print(fname, lname, age )

# x1 = eval(input('Entry x1? '))
# print('x1 =', x1, ' type:', type(x1))


'''
THESE ARE PYHTON KEY WORDS AND SHOULD NOT BE USED FOR VARIABLE NAMING

and del from None try
as elif global nonlocal True
assert else if not while
break except import or with
class False in pass yield
continue finally is raise
def for lambda return'''

# my_print = print

# my_print("Boy")


#LISTS - THIS IS A COMMENT

##names = ["ada", "bola", "uche"]
##
###to reference "ada" in the list above
##
##print(names[0])

##v= 1 +2j
##type("")



"OPERATORS"
# x= 1
# y= 2

# print("X :",  x)

# x -= 1
# y= 2

# print("X :",  x)

# Simple programme to add two fractions and give answer as fraction 

# num1 = int(input ("Enter Numerator 1 :"))
# den1 = int(input ("Enter Denominator 1 :"))
# num2 = int(input ("Enter Numerator 2 : "))
# den2 = int(input ("Enter Denominator 2 :"))

# full_den = den1*den2

# up1 = (full_den/den1)*num1
# up2 = (full_den/den2)*num2

# full_num = up1 + up2
# print ("\nAnswer = ", full_num, "/", full_den)
# print("\n", num1, "/", den1, "+", num2, "/", den2, "is ---> ", full_num, "/", full_den)

#SAMPLE LOGICAL TEST TO CHECK IF USER INPUT IS A PRIME NUMBER

# user_input = int(input ("Enter a number to test if Odd number :"))

# response = ((user_input%2) is not 0)
# print("\n Is", user_input, "an Odd NUmber ?? ---> ",response )

# if not response :
#     print("\n ", user_input, "an Even NUmber!!!!!" )



#ASSIGNMENT WEEK 1
# WRITING A PROGRAM THAT ADDS FOUR FRACTIONS

#while loop 

# print("\t This program can add , minus, or times two values")
# print("\t Enter S- to subtract")
# print("\t Enter m- to multiply")
# print("\t Enter A- to add")

# while(True):
#     x = int(input("Enter a first value : "))
#     y = int(input("Enter a second value : "))
#     action = (input("Enter an action : "))

#     if action == "s" : print(x-y)
    # elif action == "a":
    #     print(x+y)
    # elif action == "m":
    #     print(x*y)
    # else:
    #     break
# while(True):
#     print("otisele")

#Guessing Game in python with score


# import random as ran



# while True:
#     score = 0
#     picked_number = ran.randint(0,5)
#     while True:
#         print(picked_number)
#         user_guess = int(input("Whats your guess : "))
#         if user_guess == picked_number:
#             print("Wow youre a genius")
#             score = score + 50
            
#         elif user_guess != picked_number:
#             print("Sorry Bro try again")
#             print(score)
#             break

# zodiac_signs = ["aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo", 
#                 "virgo", "libra","scorpio", "sagitarius", "carpricon"]

# months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

# user_input = input("Please enter your birth month : ")

# for index in range(12):
#     if months[index]== user_input:
#         print("Your Zodiac sign for ", user_input, "is", zodiac_signs[index])

# SLICE

# x= ["john","hi", "paul", "23"]
# y =(x[3:])

# print(x.split(","))
# print(x.upper())
# arr = x.replace("paul", "mary")
# print(x.replace("paul", "mary"))
# print("".join(x))

# _dict = {"key1":"val", "key2":"val", "key3":"val"}
# _list = ["john","hi", "paul", "23"]
# print(_list)
# for key in _dict:
#         _list.append(_dict[key])
#         print(_dict[key])
# print(_list)
 
# _list = []
# structured_list = []
# users = "Ada, Ukbabi, ukpabi1, 3pm", "uche, ukanam, uchman, 3pm", "inyang, KPongette, inyanga50, 8am"
# for i in range(len(users)):
#         # x = input("enter details with comma spaces : ")
#         x = users[i]
#         _list.append(x)
#         print(_list)

# for user in range(len(_list)):

#         splitted = _list[user].split(",")
#         print(_list[user].split(","))
#         _dict = {"name":(splitted[0]).strip(),
#                 "lname":(splitted[1]).strip(),
#                 "uname":(splitted[2]).strip(),
#                 "time":(splitted[3]).strip()}
#         structured_list.append(_dict)

# # ##SEARCH THROUGH INPUTED VALUES

# while True:
#         user_input = input("Please enter a userNAME to search : ")
#         found = False
#         for user in structured_list:
#                 # print(len(user["uname"]), len(user_input))
#                 if user_input in user["uname"]:
#                         print("\n\t",user["uname"], user["name"], user["lname"], user["time"])
#                         found = True
                        
#         if not found :        
#             print("User not found, Please try again..!!!" , found)








# import timeit
# word = "qwertyuiopasdfghjklzxcvbnm" * 10

# def rev1 (word):
#     return word[::-1]

# def rev2(word):
#     new_word = []
#     for i in range(len(word)):
#         new_word.append(word[len(word)-i-1])

#     return ("".join(new_word))


# def rev3 (word):
#     chars = list(word)
#     for i in range(len(word)//2):
#         tmp = chars[i]
#         chars[i] = chars[len(word)-i-1]
#         chars[len(word)-i-1] = tmp
#     return ("".join(chars))


# print("Running rev1 -----\|/")
# print(timeit.repeat(lambda:rev1(word)))
# print("Running rev2 -----\|/")
# print(timeit.repeat(lambda:rev2(word)))
# print("Running rev3 -----\|/")
# print(timeit.repeat(lambda:rev3(word)))

# divide fractions to their lowest

# num = 20
# den = 500

# for i in reversed(range(2,10)):
#     if num % i == 0 and den % i == 0 :
#         divisible = True
#         while divisible :
#             if num % i == 0 and den % i == 0 :
#                 num = num/i
#                 den = den/i
#                 print(num,den, i)
#             else:
#                 divisible = False


# print(int(num), int(den))


# file = open("babies.csv","r") 
 
# file.write("\nHello World") 

# for i in range(10):
#         x = file.readline()
#         print(x) 
# print(x.split().count("Adam"))
# print(x.count("Adam"))
# file.write("This is our new text file") 
# file.write("and this is another line.\n") 
# file.write("Why? Because we can.") 
 
# file.close() 
# import csv

# baby_names = open("babies.csv","r") # open and 'r' read  'w' write 'a' append
 

# name_str = baby_names.read()#assign csv data to variable
# name_list = []
# splitted_list = name_str.split()#split into individual babies (==> list of strings)

# list_length = len(splitted_list)#got list lenght to use in for loop

# for i in range(list_length):
#         target_val = splitted_list[i].split(",")#  (split babiy details into ==> list of lists)
#         name_list.append(target_val[2])

# baby_names.close() #close baby name file

# #REMOVE DUPLICATES SECTION
# non_duplicate_list = []# holds names without repeatition
# occurences = []#occurences of each name
# length_name_list = len(name_list)

# for i in range(length_name_list):#check if already added to non duplicates and add if so else pass  name
#         if name_list[i] in non_duplicate_list:
#                 pass
#         elif name_list[i] not in non_duplicate_list:
#                 occurence = name_list.count(name_list[i])
#                 non_duplicate_list.append(name_list[i])
#                 occurences.append(occurence)

# print(len(non_duplicate_list), len(name_list))

# for i in range(len(non_duplicate_list)):
#         print("name : ", non_duplicate_list[i], "\t\toccurence : ", occurences[i])


# import requests
# site = requests.get('http://localhost:8000')
# site.status_code
# site.headers['content-type']

# response = (site.text)

# list = (response.split('<'))
# found = False
# for line in list:
        
#         if 'class="form-check-label"' in line or found is True:
#                 print('<'+line)
#                 found = True
# height = 5
# for x in range(height):
#         for i in range(height):
#                 if i == height/2:
#                         print('*'*x*2, end = "")
#                 else:
#                         print(end = " ")
#         print("\n")

# for i in reversed(range(height)):
#         print('*'*i, end = "")

# print(end="")

baby_names = open("babies.csv","r") # open and 'r' read  'w' write 'a' append
 

name_str = baby_names.read()#assign csv data to variable
name_list = []
splitted_list = name_str.split()#split into individual babies (==> list of strings)

list_length = len(splitted_list)#got list lenght to use in for loop

for i in range(list_length):
        target_val = splitted_list[i].split(",")#  (split babiy details into ==> list of lists)
        name_list.append(target_val[2])

baby_names.close() #close baby name file

#REMOVE DUPLICATES SECTION
non_duplicate_list = []# holds names without repeatition
occurences = []#occurences of each name
length_name_list = len(name_list)

for i in range(length_name_list):#check if already added to non duplicates and add if so else pass  name
        if name_list[i] in non_duplicate_list:
                pass
        elif name_list[i] not in non_duplicate_list:
                occurence = name_list.count(name_list[i])
                non_duplicate_list.append(name_list[i])
                occurences.append(occurence)

print(len(non_duplicate_list), len(name_list))

# WRITE TO FILE SECTION

baby_names = open("bla.csv","w") #CREATE NEW FILE FOR ADDING DATA
baby_names.close()
baby_names = open("bla.csv","a") # OPEN AND 'a' append

for i in range(len(non_duplicate_list)):
        text = '{name},{occurence}\n'.format(name = non_duplicate_list[i], occurence = occurences[i])
        # text = non_duplicate_list[i]+','+str(occurences[i])+'\n'
        # print(text)
        # baby_names.write(text)
        # print("name : ", non_duplicate_list[i], "\t\toccurence : ", occurences[i])

baby_names.close()

#GET HIGHEST OCCURENCE SECTION

# most_frequent_occurrence = max(occurences)
# most_freq_value_index = occurences.index(most_frequent_occurrence)
# corresponding_name = non_duplicate_list[most_freq_value_index]

# print(corresponding_name, 'is the most occuring name with ', most_frequent_occurrence, 'occurences.')









# class frac:
#         def __init__(self, num, den):
#                 self.__nume = num 
#                 self.__deno = den 

#         def add(self):
                
#                 return  print(self.__nume + self.__deno)

# x = frac(22,3)
# (x.add())

