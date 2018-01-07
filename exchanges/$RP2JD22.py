import matplotlib.pyplot as plt
import numpy as np
import ast
z = open("C:/Users/nickd/Desktop/bitcoinchange0",'r')
b = z.read()
l = ast.literal_eval(b)
print(len(l[list(l.keys())[0]]))


# Data for plotting
t = np.arange(0, 1440, 1)
x = [list(l.keys())[0]]
for i in l[list(l.keys())[0]]:
    x += [i]
v=[]
for i in range(1440):
    v += [list(l.keys())[0]]
d=v
s=x

print(len(d))
print(len(s))

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t, d)

ax.set(xlabel='time (min)', ylabel='Value of coin)',
       title='Bitcoin tracker January 5 - January 6; 5:00 (Collects data every 2 mins')
ax.grid()

fig.savefig("test.png")
plt.show()