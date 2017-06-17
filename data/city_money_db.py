# -*- coding:utf-8 -*-
import sys
import MySQLdb

db=MySQLdb.connect(host='localhost',
                   user='root',
                   passwd='200201',
                   db='testdb',
                   charset='utf8')
cur=db.cursor()

def extract_data():
    with open('city_money.csv', 'r') as f:
        content = f.read()
    data_f = content.split('\n')
    n = 0
    for data in data_f:
        if data == '':
            continue
        data_s = data.split(',')
        if n == 8:
            break
        n += 1
        datadb(data_s[0], data_s[1])

def datadb(city, money):
    #city = city.decode('utf-8')
    cur.execute('INSERT INTO city_money(city, money) VALUES(%s, %s)',(city,money))
    db.commit()

if __name__ == '__main__':
    extract_data()
    cur.close()
