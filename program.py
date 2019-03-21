
_list = []
structured_list = []
# users = "Ada, Ukbabi, ukpabi1, 3pm", "uche, ukanam, uchman, 3pm", "inyang, KPongette, inyanga50, 8am"


while True:
    action = (input('Do you want to add name(A) or search name(S)')).lower()

    if action == "a":

        x = input("enter details with comma spaces : ")

        _list.append(x)
        print(_list)

        for user in range(len(_list)):

                splitted = _list[user].split(",")
                print(_list[user].split(","))
                _dict = {"name":(splitted[0]).strip(),
                        "lname":(splitted[1]).strip(),
                        "uname":(splitted[2]).strip(),
                        "time":(splitted[3]).strip()}
                structured_list.append(_dict)

    # ##SEARCH THROUGH INPUTED VALUES
    elif action == "s":

        user_input = input("Please enter a userNAME to search : ")
        found = False
        for user in structured_list:
                # print(len(user["uname"]), len(user_input))
                if user_input in user["uname"]:
                        print("\n\t",user["uname"], user["name"], user["lname"], user["time"])
                        found = True
                        
        if not found :        
            print("User not found, Please try again..!!!" , found)