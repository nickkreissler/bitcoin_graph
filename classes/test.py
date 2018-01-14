from Coin import Graph_data
from exchanges.poloniex import Poloniex
import main
import time

a = 0
z = main.scrape()
y = Poloniex()
for i in z:
    i = Graph_data(str(i))
    i.makefile()

while(True):
    for i in z:
        x = Graph_data(str(i), a)
        x.appendfile(y.get_current_price("{}".format(i)))

    y.refresh()
    time.sleep(10)
    a+=1