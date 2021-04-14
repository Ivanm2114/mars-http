import sqlite3

name = input()
size = int(input())
speed = int(input())

con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute(f"""SELECT * FROM streelers
            WHERE size >= {size} and rate <= {speed}""").fetchall()
data = []
for elem in result:
    color1 = cur.execute(f"""SELECT name FROM colors
                WHERE id = {elem[3]}""").fetchall()[0][0]
    color2 = cur.execute(f"""SELECT name FROM colors
                WHERE id = {elem[4]}""").fetchall()[0][0]
    data.append([color1, color2, elem[1]])
data.sort(key=lambda x: x[2])
con.close()
for el in data:
    print(f'{el[0]} {el[1]} {el[2]}')
