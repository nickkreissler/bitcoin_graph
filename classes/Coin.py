import time
import smtplib
import os
def switch(file, coin):
    z = ""
    y = 0
    for i in file:
        if i == '~':
            if y == 0:
                z += '"' + "{}.txt".format(coin) + '"'
            else:
                z += '"' + "{}: ".format(coin) + '"'
            y+=1
        else:
            z += i
    return z

class Bitcoin_utils:
    def __init__(self, coin = None, coinprice = None, recipient = None, percent = None, time = None):
        self.coin = coin
        self.coinprice = coinprice
        self.recipient = recipient
        self.percent = percent
        self.time = time

    def __str__(self):
        return "Bitcoin UtileParent class for Graph_data and Notification_System\n" \
               "Graph Data: Make file Creates a text file which will collect data on the coin\n" \
               "Append File: Loop through and this will add data to self.coin.txt file, takes coin price as argument\n" \
               "Graphing data is done by running the self.coin.py file"

class Graph_data(Bitcoin_utils):
    def __init__(self, coin, count = 0):
        self.coin = coin
        self.count = count
        z = open('files/' + self.coin + ".py", 'w')
        z.write(switch(open('functions.py', 'r').read(),self.coin))

    def makefile(self):
        z = open('files/' + self.coin + '.txt', 'w')
        z.close()

    def appendfile(self, currentcoinprice):
        try:
            x,y = str(self.count), str(float(currentcoinprice))

            a = open('files/' + self.coin +'.txt', 'a')
            a.write(x + ',' + y + '\n')
            a.close()

        except:
            print("Error")
class Notification_system(Bitcoin_utils):
    def __init__(self, recipient, coin):
        self.recipient = recipient
        self.coin = coin
        self.values = []
        self.x = 0
    def sendmail(self, coinvalue, timevalue, percent):
        self.values += coinvalue
        time.sleep(10)
        self.x += 10
        if self.x / 60 == timevalue:
            for i in self.value:
                if i > self.values[0]*int('1' + str(percent)):
                    fromaddr = 'nick.d.kreissler@gmail.com'
                    toaddrs = self.recipient
                    msg = "\r\n".join([
                        "From: nick.d.kreissler@gmail.com",
                        "To:{}".format(self.recipient),
                        "Subject: {} has moved from {} to {} in {} minutes".format(self.coin, self.values[0], i,
                                                                           timevalue),
                        "",
                        ""
                    ])
                    username = 'nick.d.kreissler@gmail.com'
                    password = 'maggie1997'
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
            self.values = []
            self.x = 0