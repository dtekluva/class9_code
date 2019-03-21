import numpy as np
import random
import math
import pandas as df

mon = np.round(np.random.normal(500, 5, 104),0)
tue = np.round(np.random.normal(300, 4, 104),0)
wed = np.round(np.random.normal(400, 2, 104),0)
thur = np.round(np.random.normal(250, 10, 104),0)
fri = np.round(np.random.normal(400, 10, 104),0)
sat = np.round(np.random.normal(800, 5, 104),0)
sun = np.round(np.random.normal(50, 1, 104),0)

days = [mon, tue, wed, thur, fri, sat, sun]
print(days[1][1], days[2][1])
for day in days:
    for i in range(len(day)):
        change = (random.randint(-20, 20))
        day[i] = day[i] + change
        if  day[i] < 0 :
            day[i] = abs(day[i])

print("done")
print(days[1][1], days[2][1])

for day in days:
    for i in range(0, math.floor(len(day)/4)):
        change = (random.randint(0, 15))
        day[i] = day[i] + change + math.floor(i/2)
        if  day[i] < 0 :
            day[i] = abs(day[i])

print("done")
print(days[1][1], days[2][1])

for day in days:
    for i in range(math.floor(len(day)/4), math.floor(len(day)/2)):
        change = (random.randint(-10, 10))
        day[i] = day[i] - change + math.floor(i/2)
        if  day[i] < 0 :
            day[i] = abs(day[i]) 

print("done")
# print(days[1][160], days[2][160])

data = {'monday':days[0], 'tuesday':days[1], 'wednesday':days[2], 'thursday':days[3], 'friday':days[4], 'saturday':days[5], 'sunday':days[6]}

dataframe = df.DataFrame(data)
print(dataframe)

dataframe.to_csv('sales.csv')

# with open('sales.csv', 'w') as file:
#     file.write('helo')
#     file.close()