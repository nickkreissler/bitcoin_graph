import time
from bitfinex import Bitfinex
import smtplib

c = []
d = 1
v = 0
while(True):
    while(d % 4 != 0):

        x = Bitfinex().get_current_price()

        y = 0.62888179*int(x)

        a = .6288179*21000

        z = y - 9170

        b = a - 9170

        c += [z]

        print(z)
        print(b)
        print(c)
        d += 1
        fromaddr = 'nick.d.kreissler@gmail.com'
        toaddrs = 'nick.d.kreissler@gmail.com'
        msg = "\r\n".join([
            "From: nick.d.kreissler@gmail.com",
            "To: nick.d.kreissler@gmail.com",
            "Subject: Profit Every Hour",
            "",
            "Current Profit: $" + str(z) + "\n" +
            "Exit Point/Expected Profit at $21000: $" + str(b)
        ])
        username = 'nick.d.kreissler@gmail.com'
        password = 'maggie1997'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        if len(c) == 72:
            v+=1

        f = open("C:/Users/nickd/Desktop/datatxt" + str(v),'w+')
        f.write(str(c))
        f.close()
        time.sleep(1200)
    while(d % 4 == 0):
        d+=1
        fromaddr = 'nick.d.kreissler@gmail.com'
        toaddrs  = 'charlesnmisuraca@gmail.com'
        msg = "\r\n".join([
          "From: nick.d.kreissler@gmail.com",
          "To: charlesnmisuraca@gmail.com",
          "Subject: Profit Every Hour",
          "",
          "Current Profit: $" + str(z) + "\n" +
          "Exit Point/Expected Profit at $21000: $" + str(b)
          ])
        username = 'nick.d.kreissler@gmail.com'
        password = 'maggie1997'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()