# value = int(input("Please enter a value to raise "))
# power = int(input("please enter the raising factor "))

# result = value ** power

# output = "The " + str(power) + " power of " + str(value) +" is " + str(result)

# print(output)

t = True
f = False

print(t and t)# Should print true
print(t and f)# Should print false
print(f and t)# Should print false
print(f and f)# Should print false
print("\nFOR OR OPERATIONS\n")

print(t or t)# Should print true
print(t or f)# Should print true
print(f or t)# Should print true
print(f or f)# Should print false

print("\nFOR IN OPERATIONS\n")
name = "adebayo"

print("x" in name, " ,before adding the NOT logical operator") #should print false charachter 'x' is not a member of adebayo
print("a" in name) #should print true 

print("x" not in name, " ,after adding the NOT logical operator") #should print true as not negates original answer

print("\nMIXING MEMBERSHIP OPERATORS WITH THE LOGICAL OPERATORS FOR MULTIPLE TESTS\n")

test_list = [1,4,5,6,7,8]

print(1 in test_list," , single test")
print(1 in test_list and 32 in test_list, " , mutiple tests with 'AND' logical operator")

print(1 in test_list and 32 not in test_list, " , mutiple tests with 'AND' logical operator and 'NOT' inverting factor")

print(1 in test_list and 32 not in test_list or 8 in test_list, " , mutiple tests with 'AND' $ 'NOT' logical operators and 'NOT' inverting factor")

print(1 in test_list and 32 in test_list or 8 not in test_list, " , mutiple tests with 'AND' $ 'NOT' logical operators and 'NOT' inverting factor\n")

print("\nIDENTITY OPERATORS\n")

x = 20
y = 30

print(x is y)

y = x
print(x is y)

print("\nCOMPARISON OPERATORS\n")

a = 23
b = 32
c = 23
boy = "adamu"
girl = "suliyat"
somebody = "adamu"

print(a == b, " >----> using the equal to(==) operator 1")
print(a != b, " >----> using the not equal to(!=) operator 2")
print(a == c, " >----> using the equal to(==) operator 3")
print(a != c, " >----> using the not equal to(!=) operator 4")

print(a > c, " >----> using the greater than to(>) operator 5")
print(a < c, " >----> using the less than to(<) operator 6")

print(a >= c, " >----> using the greater than equal to((>=) operator 7")
print(a <= c, " >----> using the less than equal to((<=) operator 8")


print(boy == girl, " >----> using the equal to(==) operator 9")
print(boy == somebody, " >----> using the equal to(==) operator 10")

print(len(boy), len(girl), len(somebody))

#MAP BUILTIN FUNC
unsorted = [1, 6, 0, 9, 32, 3, 4]
stringed_list = map(str, unsorted)
print("\n List string --->", list(stringed_list))


list_for_join = ['1', '6', '0', '9', '32', '3', '4']
joined = "; ".join(list_for_join)
print("\n Joined List string --->", joined)
