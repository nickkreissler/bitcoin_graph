import urllib.request
import ast
def scrape():
    x = urllib.request.urlopen("https://poloniex.com/public?command=returnTicker")
    x = x.read().decode('utf-8')
    x = ast.literal_eval(x)
    x = list(x.keys())
    return x