import string
import random



print("                                                 ;;    ")
print("                                                | |   ")
print("          ______________________________________|_|___")
print("         /____________________________________________\ ")
print("        /______________________________________________\ ")
print("        |----------------------------------------------|")
print("        |----WELCOME PLEASE ENJOY THE HANG MAN GAME----|")
print("        |--*NOTE THAT THE GAME IS NOT CASE SENSITIVE*--|")
print("        |----------------------------------------------|")
print("        |______________________________________________|")
print()
    

available=[]

f = open("twist.txt","r") #opens file with name of "test.txt"
me=f.readline()
f.close()
word = str.split(me)
level=[2]
game_count=0
tries=[10]

def level_Chk(words,level):
    game_word=random.choice(words)

    while len(game_word)!=level[0]:
        game_word=random.choice(words)

    return game_word.upper()

def available_gen(game_count):
    
    i=0
    for item in string.ascii_uppercase:
        if game_count==1:
            available.append(string.ascii_uppercase[i])
        
        available[i]=string.ascii_uppercase[i]
        i+=1

def list_conv(arg1,arg2):

    print('  '.join(arg1))
    print(               )
    print('  '.join(arg2))
    

def input_checker():
    print()
    arg=input('please enter a letter  : ')
    print()
    
    while len(arg)!=1 :
        print()
        arg=input('Please enter not more or less than 1 letter  : ')
        print()
        
    return arg.upper()
        
     
def game_engine(word):
    score=0
    blank=[]
    blank2=[]
    print()
    print("|0_0|           THANK YOU, I HAVE PICKED A",len(word),"LETTER WORD            |0_0|  ")
    print()
    print("|0_0|   YOU HAVE TO GUESS LETTER BY LETTER AND HAVE JUST ",tries[0],"TRIES  |0_0|")
    ##print(word)
    print()
    list_conv(blank,available)    
    for item in word:
         blank.append("_")
         blank2.append("_")
    print ('  '.join(blank2))
         
    while tries[0]>0:
        print()
        print("tries: " ,tries[0]," <<<<<00000>>>>> Score " ,score," <<<<<00000>>>>> level ",level[0]-1 )
        print()
        
        in_put=input_checker()
        if in_put not in available:
            print()
            print("You have already picked this value!!!!!")
            tries[0]+=1
            print()
        if in_put not in word:
            print()
            print("Sorry ",in_put," is not in word!!!!!")
            print()
        if in_put in word and in_put in available:
            print()
            print("GOOD GUESS, WAY TO GO!")
            print()
        i=0

        for item in word:
            j=0
            if in_put==word[i]:
                for item in available:
                    if in_put==available[j] :
                        score+=10
                        tries[0]+=1
                        available[j]="_"
                    j+=1
                    
                blank[i]=word[i]
            i+=1
        tries[0]-=1
        
        list_conv(blank,available)
        
        
        if "".join(blank)==word:
            print()
            print("Congrats, you won with ",tries[0],"tries left")
            print()
            if level[0]<10:
                level[0]=level[0]+1
            break
        if "".join(blank)!=word and tries[0]==0:
            print()
            print("Sorry you have used up you tries!!!!")
            print()
            print("THE WORD WAS : ",word,"!!!")
            if level[0]>2:
                level[0]=level[0]-1
            break

    return score*len(word)

        
                
def play_game(game_count):
    tries[0]=10
    start=""
    score=0
    if game_count==0:
        start=input("|0_0|        Welcome, please press just the enter key to start      |0_0|")
        print()
       

    if len(start)==0:
        game_count+=1
        available_gen(game_count)
        
        score=game_engine(level_Chk(word,level))
        
        print("|0_0| Do you want to try again (y/n) |0_0|")
        retry=input_checker()
        
        if retry=="Y":
            score=score*game_count
            play_game(game_count)
            
        else:
            score=score*game_count
            print("You played " ,game_count,"Games."," Total score |>>> ",score)      
            input("GOODBYE, COME BACK SOON")
    else:
        score=score*game_count
        input("GOODBYE, COME BACK SOON."," Total score |>>> ",score)

play_game(game_count)
