import sqlite3

from mimesis import Generic
from mimesis import Person
from mimesis import Datetime
from mimesis import Address
from mimesis.enums import Gender
from mimesis.builtins import RussiaSpecProvider

import random
g = Generic('ru')
p = Person('ru')
dt = Datetime('ru')
rus = RussiaSpecProvider('ru')
adr = Address('ru')

conn = sqlite3.connect('people_base.db')
cur = conn.cursor()

gen = ['Женский', 'Мужской']
n = 1

cur.execute("""CREATE TABLE IF NOT EXISTS people(
   id INT PRIMARY KEY,
   gender TEXT,
   first_name TEXT,
   last_name TEXT,
   age TEXT,
   month_ob TEXT,
   day_ob TEXT,
   year_ob TEXT,
   city_ob TEXT,
   city TEXT,
   address TEXT,
   phone TEXT,
   email TEXT);
""")
conn.commit()

for i in range(20):
    #idd =  g.code.imei()
    idd = n
    gender = random.choice(gen)
    if gender == 'Женский':
        first_name = p.first_name(gender = Gender.FEMALE)
        last_name = p.last_name(gender = Gender.FEMALE)
        #self.patron = rus.patronymic(gender = Gender.FEMALE)
    elif gender == 'Мужской':
        first_name = p.first_name(gender = Gender.MALE)
        last_name = p.last_name(gender = Gender.MALE)
        #self.patron = rus.patronymic(gender = Gender.MALE)
    age =  p.age(minimum=18, maximum=70)
    month_ob = dt.month()
    day_ob = dt.day_of_month()
    year_ob = 2020 - age
    city_ob = adr.city()
    city = adr.city()
    address = adr.address()
    phone = p.telephone(mask='+7(###)-###-####')
    email = p.email(domains=['mimesis.name'])
    
    user = (int(idd), str(gender), str(first_name), str(last_name), str(age),
             str(month_ob), str(day_ob), str(year_ob), str(city_ob),
             str(city), str(address), str(phone), str(email))
    
    cur.execute("INSERT INTO people VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
    conn.commit()
    n += 1

cur.execute("SELECT * FROM people;")
three_results = cur.fetchmany(-1)
conn.commit()