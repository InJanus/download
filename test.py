import matplotlib.pyplot as plt
import pandas as pd
import re
import os

# this will make a graph based off ping and how many hours it takes to connect to the router

time = 5 # in minutes
ip = '192.168.30.1' #router ip
os.system('ping ' + ip + ' -n ' + str(time*60) + ' > ping.txt')

values = []
f = open("ping.txt", "r")
for x in f:
    m = re.search('time.(\\d{1,})', x)
    print(x)
    try:
        values.append(int(m.group(1)))
    except AttributeError:
        print('RegEx not found, skipping...')
print(values)

plt.plot(values)
plt.ylabel('Ping in ms')
plt.xlabel('Test #')
# # libraries
# import matplotlib.pyplot as plt
# import numpy as np
 
# # create data
# values=np.cumsum(np.random.randn(1000,1))
 
# # use the plot function
# plt.plot(values)
plt.show()