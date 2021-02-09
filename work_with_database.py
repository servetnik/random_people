import sqlite3
from tkinter import *
from random import randint as rnd

window = Tk()
window.geometry('400x400')

def random_person():
    #id1 = rnd(1, 19)
    #id2 = (int(id1))
    cur.execute("""SELECT * FROM people ORDER BY RANDOM() LIMIT 1;""")
    result = cur.fetchmany(1)
    for row in result:
        Label(text="ID: " + str(row[0])).grid(row=1, column=0)
        Label(text="Пол: " + str(row[1])).grid(row=2, column=0)
        Label(text="Имя: " + str(row[2])).grid(row=3, column=0)
        Label(text="Фамилия: " + str(row[3])).grid(row=4, column=0)
        Label(text="Возраст: " + str(row[4])).grid(row=5, column=0)
        Label(text="Месяц рождения: " + str(row[5])).grid(row=6, column=0)
        Label(text="Дата рождения: " + str(row[6])).grid(row=7, column=0)
        Label(text="Год рождения: " + str(row[7])).grid(row=8, column=0)
        Label(text="Город рождения: " + str(row[8])).grid(row=9, column=0)
        Label(text="Город проживания: " + str(row[9])).grid(row=10, column=0)
        Label(text="Адрес: " + str(row[10])).grid(row=11, column=0)
        Label(text="Телефон: " + str(row[11])).grid(row=12, column=0)
        Label(text="E-mail: " + str(row[12])).grid(row=13, column=0)
        
def all_lastnames():
    cur.execute("""SELECT last_name FROM people;""")
    result = cur.fetchall()
    nr = 0
    nc = 1
    for row in result:
        text1 = str(row[0])
        Label(text = text1).grid(row = nr, column = nc)
        nr += 1
        if nr == 7:
            nr = 0
            nc += 1
        
def find_person():
    name = ent.get()
    user = (str(name))
    print(user)
    
    cur.execute("""SELECT *
    FROM people 
    WHERE last_name = ?;""", (user,))
    result = cur.fetchmany(1)
    for row in result:
        Label(text="ID: " + str(row[0])).grid(row=0, column=0)
        Label(text="Пол: " + str(row[1])).grid(row=1, column=0)
        Label(text="Имя: " + str(row[2])).grid(row=2, column=0)
        Label(text="Фамилия: " + str(row[3])).grid(row=3, column=0)
        Label(text="Возраст: " + str(row[4])).grid(row=4, column=0)
        Label(text="Месяц рождения: " + str(row[5])).grid(row=5, column=0)
        Label(text="Дата рождения: " + str(row[6])).grid(row=6, column=0)
        Label(text="Год рождения: " + str(row[7])).grid(row=7, column=0)
        Label(text="Город рождения: " + str(row[8])).grid(row=8, column=0)
        Label(text="Город проживания: " + str(row[9])).grid(row=9, column=0)
        Label(text="Адрес: " + str(row[10])).grid(row=10, column=0)
        Label(text="Телефон: " + str(row[11])).grid(row=11, column=0)
        Label(text="E-mail: " + str(row[12])).grid(row=12, column=0)
    
conn = sqlite3.connect('people_base.db')
cur = conn.cursor()

cur.execute("SELECT first_name FROM people WHERE last_name = 'Новоженкова';")
three_results = cur.fetchmany(1)
print(three_results)
conn.commit()

but1 = Button(window, text="Случайный человек", command = random_person)
but1.grid(row = 18, column = 0)

btn_pok = Button(window, text="Показать фамилии", command = all_lastnames)
btn_pok.grid(row = 19, column = 0)

ent = Entry()
ent.grid(row = 20, column = 0)

btn_pok = Button(window, text="Поиск", command = find_person)
btn_pok.grid(row = 20, column = 1)


window.mainloop()
