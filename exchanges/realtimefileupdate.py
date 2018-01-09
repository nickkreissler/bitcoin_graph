from time import gmtime, strftime
import time
from bitfinex import Bitfinex

c = 0

def getvar():
    x = strftime("%H", gmtime())
    y = int(Bitfinex().get_current_price())
    return str(x),str(y)


while(True):
    try:
        time.sleep(8)
        z = open("sampleText.txt",'a')
        a = getvar()
        z.write(str(c) + ',' + a[1] + '\n')
        z.close()
        c+=1
    except:
        print("Error")