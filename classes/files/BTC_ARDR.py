import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pullData = open("BTC_ARDR.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.set(xlabel='time (10 sec)', ylabel='Value of coin)',
           title="BTC_ARDR: " + str(y) )
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()