import json
import requests
import sqlite3

def address_convert(x):
    key = "25411e0758eb9f7b742cfa331a2a75c6"
    url = f'https://restapi.amap.com/v3/geocode/geo?address={x}&output=JSON&key={key}'
    response = requests.get(url)
    data = response.json()
    location = data["geocodes"][0]["location"]
    return location

db = sqlite3.connect('/Users/wangzifang/Desktop/应用经济学中的大数据分析/assignment/Assignment5_sql/address.db')
cur = db.cursor()
cur.execute("CREATE TABLE address(address TEXT, location TEXT);")

with open('/Users/wangzifang/Desktop/应用经济学中的大数据分析/assignment/data/assignment_sql/address.txt', 'r') as f:
    for line in f.readlines():
        address = line.strip() #去除可能存在的空格和换行符
        location = address_convert(line)
        list = [address, location]
        cur.execute("INSERT INTO address VALUES (?,?);", list)

db.commit()
cur.close()
db.close()
