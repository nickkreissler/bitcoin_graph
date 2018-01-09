import time


from bitfinex import Bitfinex
var1 = True
var2 = True

i = 0

while(True):
    while(var1):
        try:
            y = int(Bitfinex().get_current_price())
            c = {}
            c[y] = []
            z=0
            var1 = False
            var2 = True
        except:
            print('error')

    while(var2):
        try:
            x = int(Bitfinex().get_current_price())
            time.sleep(60)
            c[y] += [x]
            z+=1
            print(z)
            if z==1439:
                n = open("C:/Users/nickd/Desktop/bitcoinchange"+str(i), 'w+')
                n.write(str(c))
                n.close()
                i+=1
                var2 = False
                var1= True
        except:
            print('error')