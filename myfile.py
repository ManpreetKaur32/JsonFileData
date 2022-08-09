import json
import pymysql

json_data=open("chandigarh.json").read()
json_obj=json.loads(json_data)
print(json_obj)
con=pymysql.connect(host="localhost",user="root",password="",db="myjson")

cursor=con.cursor()

for item in json_obj:
    Name=item.get("Name")
    Address=item.get("Address")
    Phone=item.get("Phone")
    Ratings=item.get("Ratings")
    Reviews=item.get("Reviews")
    Description=item.get("Description")
    cursor.execute("insert into json_file(Name,Address,Phone,Ratings,Reviews,Description) value(%s,%s,%s,%s,%s,%s)",(Name,Address,Phone,Ratings,Reviews,Description))
con.commit()
con.close()

