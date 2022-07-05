import psycopg2
import requests
import re
import csv
con = psycopg2.connect(database="data_ss", user="postgres", password="457621", host="localhost", port="5432")
cur = con.cursor()
sqlstr="select domain from table1"
cur.execute(sqlstr)
url_list=cur.fetchall()
url_1=[url[0] for url in url_list]

i=0
data=[]
start=i
for url in url_1[start:]:
    i+=1
#         a_data=[]

    try:
        try:
            res=requests.get("http://"+url,timeout=20)
        except:
            res=requests.get("https://"+url,timeout=20)
        pat = r"<title>(.*)</title>"
        res.encoding = res.apparent_encoding
        name=re.findall(pat, res.text)[0]
#             a_data.append(url)
        print(i,name)
#             a_data.append(name)
        a_data=(url,name)
        data.append(a_data)
    except:
        pass
    if i %500==0:
        with open(str(i)+'.csv', 'w', encoding='utf-8') as file_obj:
            writer = csv.writer(file_obj)
            writer.writerow(['domain', 'name'])
            writer.writerows(data)
            data=[]

