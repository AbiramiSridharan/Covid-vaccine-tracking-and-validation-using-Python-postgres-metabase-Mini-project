import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  phramacompMaster(compName varchar,CompID varchar,address varchar,city varchar,state ' \
  'varchar,pincode varchar,country varchar ,emailid varchar, phone varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many company detail ur going to enter'))
for i in range(rows):
    def nullvalid():
        compname = input('enter company name')
        if (compname == ''):
            print("pls enter company name , its Mandatory ")
            nullvalid()
        else:
            return compname
    compname = nullvalid()

    def nullvalid1():
        compid = input('enter company ID')
        if (compid == ''):
            print("pls enter company ID , its Mandatory ")
            nullvalid1()
        else:
            return compid
    compid= nullvalid1()


    def nullvalid2():
        addr = input('enter company Address')

        if (addr == ''):
            print("pls enter company address , its Mandatory ")
            nullvalid2()
        else:
            return addr
    addr= nullvalid2()

    def nullvalid3():
        city = input('enter company City')
        if (city == ''):
            print("pls enter city , its Mandatory ")
            nullvalid3()
        else:
            return city
    city= nullvalid3()


    def nullvalid4():
        state = input('enter company State')
        if (state == ''):
            print("pls enter state , its Mandatory ")
            nullvalid4()
        else:
            return state


    state = nullvalid4()

    def pincode():
        pin= input('enter pincode')
        reg='^\d{6}$|^\d{2}$'
        if(re.search(reg,pin)):
            print("valid pincode")
            return pin
        else:
            print("invalid pin")
            return pincode()
    pin=pincode()

    country = input('enter company Country')
    def checkemail():

            email = input('enter company emailid')
            regex = '^[a-z0-9A-Z]+[\._]?[a-z0-9A-Z]+[@]\w+[.]\w{2,3}$'

            if(re.search(regex,email)):
                print("Valid Email")
                return email
            else:
                print("Invalid Email")
                return checkemail()
    email=checkemail()

    reg = '^((\+91){0,1}[\s|-]\d{10})$|^(\d{3,5}[\s|-]\d{8})$|^(\d{10})$|^(\+91){0,1}(\d{10})$'
    def checkphone():
            phone= input("enter phone number")

            if (re.search(reg,phone)):
                print("Valid phone num")
                return phone
            else:
                print("Invalid phone num")
                return checkphone()
    phone=checkphone()
    var=(compname,compid,addr,city,state,pin,country,email,phone)
    q1="""INSERT INTO phramacompmaster(compname,compID,address,city,state,pincode,country,emailid,phone) VALUES (%s,%s,%s,%s,%s,
        %s,%s,%s,%s)"""
    rs.execute(q1,var)
print("inserted successfully")

c.commit()
rs.close()
c.close()
