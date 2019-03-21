def add_maggi(no):
    
    check = 1
    print('hello  Before return')
    if check == no:
        return ( str(no) +' Maggi')
    print('''hello  after return 
            because''', check, 'is not equal to',  no )

# no_cubes = add_maggi(1)
# print(no_cubes)

def adder(upperlim, increment,initial):
    print('Initial Before increment ===> ', initial)
    # print('upperLim Before increment ===> ', initial >= upperlim)
    initial = initial + increment

    if initial >= upperlim:
        return initial
    elif initial <= upperlim:
        adder(upperlim, increment,initial)

# print(adder(50,5,0))
# new_func = adder
# new_func(50,5,0)
# print(new_func)







import xyz

def show_fact(num):
    val = str(num)
    for i in reversed(range(1,num)):
        val +=  ' * '+ str(i)
    print(val)

# show_fact(3)

def fact(n):
    show_fact(n)
    """ Function to find factorial """
    if n == 1:

        return 1
    else:
        return (n * fact(n-1))

# print (fact(6))


def add(a,b,action):
    
    if action == "a":
        sum = a+b
        return sum
    else:
        print("input the right  code")

def sub(a,b,action):
    if action =="s":
        return a - b
    else:
        return "\nsorry. not my function"

def div(x, y, action):
    if action != 'd':
        return 'This action cannot be performed by this function'
    return x/y

def begin(a,b,action):
    funcs = [add,sub,div]

    for i in funcs:
        print(i(a,b,action))

begin(4,5,'d')