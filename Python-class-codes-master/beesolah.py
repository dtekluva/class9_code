file =  open('docword.txt','r') 

text = file.read()
text = (text.split('\n')) #convert each newline into a list (split by newline \n)

for line in text:
    splitted_line = line.split(' ') #convert each of the splited valeus into list of three  numbers (split by spaces)
    single_value = splitted_line[1]
    single_value #<===== i believe this is what you need the middle value
    print('\n',single_value) 