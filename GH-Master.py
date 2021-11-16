#GH-Master:-
#GH-ID,GH-Name, chiefDocName,DocID,GH-Address, district/city, state,country ,pinCode,phone,email
import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  GHMaster(GHID varchar,GHName varchar,DocName varchar,DocID varchar,GHAddress varchar, ' \
  'districtorcity varchar, state varchar ,pinCode varchar,phone varchar,email varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many company detail ur going to enter'))
for i in range(rows):
    ghid = input('enter GH-ID')
    ghname = input('enter name of GH')
    doc=input("enter doc incharge name")
    docid=("input doc id ")
    addr = input('enter GH Address')
    city = input('enter  dist/City')
    state = input('enter  State')
    pin= input('enter pincode')
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
    def checkemail():

        email = input('enter GH emailid')
        regex = '^[a-z0-9|A-Z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if (re.search(regex, email)):
            print("Valid Email")
            return email
        else:
            print("Invalid Email")
            return checkemail()


    email = checkemail()

    reg = '^((\+91){0,1}[\s|-]\d{10})$|^(\d{3,5}[\s|-]\d{8})$|^(\d{10})$|^(\+91){0,1}(\d{10})$'

    def checkphone():
        phone = input("enter phone number")
        if (re.search(reg, phone)):
            print("Valid phone num")
            return phone
        else:
            print("Invalid phone num")
            return checkphone()


    phone = checkphone()
    var = (ghid,ghname,doc,docid,addr,city,state,pin,phone,email)

    q1 = """INSERT INTO GHMaster(GHID,GHName,DocName,DocID,GHAddress,districtorcity,state,pinCode,phone,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rs.execute(q1,var)
print("inserted successfully")

c.commit()
rs.close()
c.close()