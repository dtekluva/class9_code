# products = [{'jeans':{'price':50}}, {'shoes':{'price':50}}, {'shirts':{'price':20}}, {'shades':{'price':10}},
#             {'hats':{'price':80}}, {'drinks':{'price':5}}, {'beverages':{'price':30}}]
# cart = []
# wallet = 1020

# def add(item):
#     cart.append((products[int(item)]))
#     list_cart()

# def remove(item):
#     cart.remove(cart[int(item)])
#     list_cart

# def _list():
#     i = 0
#     print('ITEMS YOU Can buy are :')
#     for item in products:
#         for key in item:
#             print(i,':\t ',key, '\t Price: ', item[key]['price'] )
#         i += 1

# def list_cart():
#     print('Items currently in cart')
#     i = 0
#     for item in cart:
#         for key in item:
#             print(i,':\t ',key, '\t Price: ', item[key]['price'] )
#         i += 1
#     print_cart_total()

# def print_cart_total():
#     total = 0
#     for item in cart:
#         for key in item:
#             total += item[key]['price']

#     print('You currently have {0}Naira products in your cart'.format(total))
#     return total

# def checkout(bill):
#     if wallet < bill:
#         print ('Sorry Bro Your Money Nor Reach \n REMOVE SOME ITEMS')
#         return 
#     elif wallet >= bill:
#         charge(bill)
#         print('Thank you for your purchase of {bill}, your balance is {balance}'.format(bill = bill, balance = wallet))
#         return

# def charge(bill):
#     global wallet 
#     wallet = wallet - bill
#     return wallet - bill

# def begin():

#     while True:

#         action  = input('Welcome Please what would you like to do \n a => ADD r => REMOVE l=> LIST c => CART ch=> CHECKOUT: ')

#         if action == 'a'.lower():
#             _list()
#             item = input('Pick an item to add : ')
#             add(item)
#         if action == 'r'.lower():
#             list_cart()
#             item = input('Pick an item to remove : ')
#             remove(item)
#         if action == 'l'.lower():
#             pass
#         if action == 'c'.lower():
#             pass
#         if action == 'ch'.lower():
#             checkout(print_cart_total())
#         elif action == 'x':
#             break


# begin()

# _list = [
#             'baller', 'toaster','baddest', 'gbefun','stewing',
#                     ['monday', 'tuesday','wed', 'thurs','fir']
#                 ]

# # print(_list[5][4][-1])
# # i = 0
# # while i < 6:
# #     print(_list[i])
# #     for letter in _list[i]:
# #         print(letter)
# #     i += 1

# resp = input('Welcome, Do you have runny nose : (y/n) : ')
# y = 'y'
# n = 'n'
# if resp == y: 
#     resp = input('Sorry, Do you have headache : (y/n)')
#     if resp == y:
#         print('Take Paracetamol Thats all')
#     elif resp == n:
#         resp = input('Hmmfff!!!, Do you have eye pain : (y/n)')
#         if resp == y:
#             print('You Probably have Sinusitis')
#         else: 
#             ('Please See a doctor')
# else:
#     print('Sorry This feature is coming  soon ==> consult your medical prac for now')
import recursion
from recursion import adder as bla
def do_summin():
    ''''''
    pass

recursion.adder(50,2,0)