import mysql.connector as msc
import random
from datetime import date
#GAME
l = ["r","p", "s"]
d = date.today()
wcount = 0
lcount = 0
tcount = 0
won = 0
lost = 0
tie = 0
while True:
    g = random.choice(l)   
    player = input("Rock, Paper, Scissors (Enter to stop): ")
    if player == g:
        print(g)
        print("Tie")
        tcount+=1
    elif player == "r":
        if g == "s":
            print(g)
            print("You won")
            wcount +=1
        elif g == "p":
            print(g)
            print("You lost")
            lcount+=1
    elif player == "p":
        if g == "s":
            print(g)
            print("You lost")
            lcount +=1
        elif g == "r":
            print(g)
            print("You won")
            wcount+=1
    elif player == "s":
        if g == "r":
            print(g)
            print("You lost")
            lcount +=1
        elif g == "p":
            print(g)
            print("You won")
            wcount+=1
    elif player == "":
        print("Number of times you won:",wcount)
        print("Number of times computer won:",lcount)
        print("Tie count:",tcount)
        if (wcount == lcount and tcount<=wcount) or (tcount >=wcount and wcount == lcount):
            tie =1
            t = "tie"
            print("It is a tie")
        elif wcount>lcount:
            won = 1
            t = "won"
            print("You won the series")        
        elif lcount > wcount:
            lost = 1
            t = "lost"
            print("You lost the series")        
        break
    else:
        print("Invalid Try again")

#INPUT DATA
conn = msc.connect(host = "localhost", username = "root", password = "ahsirk", database = "rps")
c = conn.cursor()
q = "select won, lost, tie from plot where date  = %s"
val = (d,) 
c.execute(q,val)
data = c.fetchall()
if data == []:
    query = "insert into plot(date, won, lost, tie) values(%s, %s, %s, %s)"
    values = (d, won, lost, tie)
    c.execute(query, values)
    conn.commit()
else:
    if t == "won":
        query = "update plot set won = won +1  where date  = %s"
        values = (d,)
        c.execute(query, values)
        conn.commit()
    elif t == "lost":
        query = "update plot set lost = lost + 1  where date  = %s"
        values = (d,)
        c.execute(query, values)
        conn.commit()
    elif t == "tie":
        query = "update plot set tie = tie+1  where date  = %s"
        values = (d,)
        c.execute(query, values)
        conn.commit()

conn.close()
c.close()

