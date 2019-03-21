                                                #Assignment on list methods, let's play!!!!!!!!!!!!!
Wallmart_Shopping_cart = ["Headsets", "Earbuds", "Projector", "WiFi", "Airpods", "Flashdrive", "Iphone X Max", "Macbook", "iwatch"]
print(Wallmart_Shopping_cart[::2])
List = ["Apple", "Chicken", "Fish", "Orange", "Beef", "Pork", "Soursop", ["House", "Car", "Food"]]
print(List[-1][0])
Hobbies = ["sleeping", "writting", "Gaming"]
print("Before append:", Wallmart_Shopping_cart)
Wallmart_Shopping_cart.append("Ipad")
print("After append:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart.remove("Earbuds") #or Wallmart_Shopping_cart.remove(Wallmart_Shopping_cart[2])
print("After removing Earbuds:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart.extend(Hobbies)
print("After extending:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart.insert(0, "Mouse")
print("After inserting Mouse:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart.pop()
print("After popping Gaming:", Wallmart_Shopping_cart)

print("Checking if Airpods is on the list and it's index:", Wallmart_Shopping_cart.index("Airpods"))

Wallmart_Shopping_cart.sort()
print("After sorting:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart.reverse()
print("After reveresing the elements:", Wallmart_Shopping_cart)

Wallmart_Shopping_cart2 = Wallmart_Shopping_cart.copy()
print("After copying:", Wallmart_Shopping_cart2)

Wallmart_Shopping_cart2.clear()
print("After clearing:",  "Empty")

print("Checking how many times 'Airpods' Appeared:", Wallmart_Shopping_cart.count("Airpods"))