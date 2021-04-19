import sqlite3

name = input()
temp = int(input())
rash = int(input())

con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute(f"""SELECT * FROM malaclaws
            WHERE temp >= {temp} and rash <= {rash}""").fetchall()
data = []
for elem in result:
    country = cur.execute(f"""SELECT name FROM places
                WHERE {elem[1]} == id""").fetchall()
    data.append([country[0][0], elem[2], elem[3]])
data.sort(key=lambda x: (x[1], x[0]), reverse=True)
con.close()
for el in data:
    print(f'{el[0]} {el[1]} {el[2]}')
