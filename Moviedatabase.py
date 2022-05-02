import sqlite3

conn = sqlite3.connect('Moviedatabase')
"""conn.execute('''CREATE TABLE MOVIE
         (ID INT PRIMARY KEY     NOT NULL,
         Movie_name           TEXT    NOT NULL,
         Lead_actor            TEXT     NOT NULL,
         Lead_actress        TEXT       NOT NULL,
         Year_of_release        INT     NOT NULL,
         Director_name      TEXT        NOT NULL);''')
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (1,'Alice in the Wonderland ', 'Johnny Depp','Anne Hathaway', 2010, 'Tim Burton')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (2, 'Journey to the centre of the Earth', 'Brendan Fraser', 'Anita Briem', 2008, 'Eric Brevig')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (3, 'The chronicles of Narnia', 'Aslan', '', 2005, 'Andrew Adamson')");
conn.commit()
conn.close()"""


print(" 1. Alice in the Wonderland \n 2. Journey to the centre of the Earth\n 3. The chronicles of Narnia")
choice = int(input("Enter your choice: "))

val = conn.execute("SELECT * from MOVIE WHERE ID is "+str(choice))
for v in val:
     A = v[0]
     B = v[1]
     C = v[2]
     D = v[3]
     E = v[4]
     F = v[5]
print("Movie ID      : ",A)
print("Movie Name    : ",B)
print("Lead Actor    : ",C)
print("Lead Actress  : ",D)
print("Released Year : ",E)
print("Director      : ",F)

