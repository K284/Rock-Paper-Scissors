import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import mysql.connector as msc

conn = msc.connect(host = "localhost", username = "root", password = "ahsirk", database = "rps")
c = conn.cursor()
c.execute("select date, won, lost, tie from plot")
data = c.fetchall()
x = []
y = []
z = []
w = []

for row in data:
    x.append(row[0].strftime("%y-%m-%d"))
    y.append(row[1])
    z.append(row[2])
    w.append(row[3])

A = np.arange(len(x))  
range = np.arange(1,51)
plt.xlabel("Date")
plt.ylabel("Count")
plt.yticks(range)
plt.xticks(A,x)
plt.bar(A, y, color = "violet", label = "Won", width = 0.25)
plt.bar(A+0.25, z, color = "orange", label = "Lost", width = 0.25)
plt.bar(A+0.5, w, color = "red", label ="Tie", width = 0.25)
plt.legend(loc = "upper left")
plt.show()

