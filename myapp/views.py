from django.shortcuts import render
from .models import mydata
from .models import mydata, Customer
import json
#import pymysql
# Create your views here.

def json_record(request):
    json_data=open("C:\\Users\\singh\\PycharmProject\\pythonProject\\myjson\\media\\file_media\chandigarh.json").read()
    json_obj=json.loads(json_data)
    # print(json_obj)
    # con=pymysql.connect(host="localhost",user="root",password="",db="myjson")

    # cursor=con.cursor()

    for item in json_obj:
        Name=item.get("Name")
        Address=item.get("Address")
        Phone=item.get("Phone")
        Ratings=item.get("Ratings")
        Reviews=item.get("Reviews")
        Description=item.get("Description")
        try:

            check = Customer.objects.filter(Name=item['Name'])
            if not check:
                obj=Customer(Name=Name,Address=Address,Phone=Phone,Ratings=Ratings,Reviews=Reviews,Description=Description)
                obj.save()
        except:
            pass
    # con.commit()
    # # con.close()
    # return  render(request,'display.html')


    # for item in json_obj:
    #     Name=item["Name"]
    #     Address=item["Address"]
    #     Phone=item["Phone"]
    #     Ratings=item["Ratings"]
    #     Reviews=item["Reviews"]
    #     Description=item["Description"]
    #     obj=mydata(Name=Name,Address=Address,Phone=Phone,Ratings=Ratings,Reviews=Reviews,Description=Description)
    #     Obj_data=mydata.objects.filter(id=obj.id)
        # obj.save()
    # con.commit()
    # con.close()
    return  render(request,'home.html')

def display_data(request):
    obj1 = Customer.objects.all()

    return render(request,"display.html", {"addto":obj1})

def home(request):
    #load all the post from db(10)
    # customer=Customer.objects.all()[:11]
    # # print(customer)
    # data={
    #     'customer':customer
    # }
    return render(request, 'home.html')









































