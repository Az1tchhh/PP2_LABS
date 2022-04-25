import psycopg2


conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="Mazayka2003",
  host="localhost")


name = input('Eneter your name...\n')

sql = f'select id, score from players where name = \'{name}\''

cursor = conn.cursor()
cursor.execute(sql)

players = cursor.fetchall()

if len(players) > 0:
  print(f'Welcome {players[0][0]}! You last score = {players[0][1]}')
  # print('you already registered in the system')
else:
  print('please register in the system')



cursor.close()
conn.close()