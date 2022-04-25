import psycopg2


conn = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="Mazayka2003",
  host="localhost")


sql = 'select * from players where score>=0'

cursor = conn.cursor()
cursor.execute(sql)

students = cursor.fetchall()

print(students)

cursor.close()
conn.close()