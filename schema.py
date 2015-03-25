import sqlite3 as lite

DATABASE="mqttbot.db"


con = lite.connect(DATABASE)
con.execute('''CREATE TABLE Subscriptions
       (ID INT PRIMARY KEY     NOT NULL,
       Name           TEXT    NOT NULL,
       Topic          TEXT     NOT NULL,
       Enable         BOOLEAN);''')
con.close()
