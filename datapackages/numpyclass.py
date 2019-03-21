import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

data = pd.read_csv('films.csv')
# print(data['title'])
# print(data.describe(include = 'all'))
# x = data.budget.apply(lambda x: np.where(x.isdigit(),x,0))
# x = x.astype(int)
# print(x)
# y = x[x != 0]
# print(y)
#GET MEAN OF DATA

# print('MEAN : ',y.mean())
# print(x.shape)
# a = np.linspace(-40, 200, 100)
# rand =  a - np.random.normal(-30,80,100)
# b = np.arange(0,100)
# print(a)
# print(b)
# print(rand)

# plt.plot(a,b)
# plt.scatter(rand,b)
# plt.show()


#PLOT SIN GRAPH

# points = np.linspace(-2*pi, 2*pi, 360)

# y = np.cos(points)
# print(y)

# plt.plot(points, y)
# plt.show()