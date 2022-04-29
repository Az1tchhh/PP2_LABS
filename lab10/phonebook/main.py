import psycopg2
conn = psycopg2.connect(
    database="phonebook",
    user="postgres",
    password="Mazayka2003",
    host="localhost")
sql = 'select name, number from phonebookk'
cursor = conn.cursor()
cursor.execute(sql)
PhoneBook = cursor.fetchall()
print(PhoneBook)
##inputting the name and number
string = input("input the name: ")
### checking for identity
identity_finder = f'select name from phonebookk where name = \'{string}\''
pare = conn.cursor()
pare.execute(identity_finder)
names = pare.fetchall()
###
if len(names) == 0:
    number = input('Input the number: ')
    create = conn.cursor()
    create.execute("INSERT INTO phonebookk (name, number) VALUES ('{0}', {1});".format(string,number))
else:
    string1 = input('Input new name: ')
    number1 = input('Input new number: ')
    change = conn.cursor()
    change.execute(f'''
    UPDATE phonebookk
    set name = \'{string1}\'
    where name = \'{string}\';
    ''')
    change.execute(f'''
    UPDATE phonebookk
    set number = {number1}
    where name = \'{string1}\';
    ''')
###
string = input("Do you want to delete smth?(Y or N): ")
if string == 'Y':
    name2 = input("Choose the name to delete: ")
    identity_finder2 = f'select name from phonebookk where name = \'{name2}\''
    pare2 = conn.cursor()
    pare2.execute(identity_finder2)
    names2 = pare2.fetchall()
    if len(names2) != 0:
        delete = conn.cursor()
        delete.execute(f'''
        delete from phonebookk
        where name = \'{name2}\'
        ''')
    else:
        print("No such person exists!")
else:
    print("Good bye!")
conn.commit()  
conn.close()