from coingraph import Graph_data
from exchanges.bitfinex import Bitfinex

x = Graph_data('Bitoin')
x.makefile()
print(x)
print(x.__repr__())
while(True):
    x.appendfile(Bitfinex().get_current_price())
