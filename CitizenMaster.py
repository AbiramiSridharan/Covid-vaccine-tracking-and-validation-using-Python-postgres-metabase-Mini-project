#GH-Master:-
#GH-ID,GH-Name, chiefDocName,DocID,GH-Address, district/city, state,country ,pinCode,phone,email
import re
import psycopg2 as pg
import sys
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists CitizenMaster(ID varchar,IDtype varchar ,citizenName varchar,age varchar,gender varchar,' \
  ' bloodgroup varchar, address varchar, districtorcity varchar,state varchar,pincode varchar , phone varchar, GHID varchar)'
rs.execute(q)
print("table created")

id = input('enter 1- for voter-ID,2- for Aadhar-ID,3-for pancard')
def voteridvalid():

            voterid=input("enter voter ID")
            reg='^([a-zA-Z]){3}([0-9]){7}?$'
            if (re.search(reg,voterid)):
                print("valid voterid")
                return voterid
            else:
                print("invalid voterid")
                return idvalid()

def aadharvalid():

            aadharid=input("enter ur aadhar number")
            reg = ("^[2-9]{1}[0-9]{3}\\" +
                     "s[0-9]{4}\\s[0-9]{4}$")
            if(re.search(reg,aadharid)):
                print("valid aadhar ID")
                return aadharid
            else:
                print("invalid aadharid")
                return idvalid()


def panvalid():
        reg = ("^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
        panid = input("enter ur PAN number")
        if (re.search(reg,panid)):
                print("valid pan number")
                return panid
        else:
                print("invalid pan number")
                return idvalid()

#ACDEG2587E
def idvalid():
    # id = input('enter 1- for voter-ID,2- for Aadhar-ID,3-for pancard')
    if (id.isdigit() == True):
        if (id == '1'):
            str="voterID"
            voterid = voteridvalid()
            return [voterid,str];
        elif (id == '2'):
            str1="AadharID"
            aadharid = aadharvalid()
            return [aadharid,str1];
        elif (id == '3'):
            str2="PAN ID"
            panid = panvalid()
            return [panid,str2];
        elif (id == ''):
            print("any 1 id is mandatory,pls enter any one")
            return idvalid()
        else:
            print(" number not valid")
            return idvalid()

    else:
        print("enter any number,not characters")
        return idvalid()


list = idvalid()
print(list)
name = input('enter name of citizen')
def agevalid():
    age=input("enter age")
    if(age.isdigit()==True):
        age=int(age)
        if(age>70 or age<10):
            print("not eligible for vaccine")
            sys.exit(0)
        else:
            print("eligible")
            return age
    else:
        print("enter valid number not character ")
        return agevalid()
age=agevalid()

gender=("enter gender ")
bloodgroup = input('enter bloodgroup')
address= input('enter address')
city = input('enter District/City')
state = input('enter state')

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


reg = '^((\+91){0,1}[\s|-]\d{10})$|^(\d{3,5}[\s|-]\d{8})$|^(\d{10})$|^(\+91){0,1}(\d{10})$'
def checkphone():
        phone = input("enter phone number")
        # regex= '^((\+*)((0[-]+)|(91))(\d{12}+|\d{10}+))|\d{5}([-]*)\d{6}$'
        if (re.search(reg, phone)):
            print("Valid phone num")
            return phone
        else:
            print("Invalid phone num")
            return checkphone()
phone = checkphone()


def GHidvalid():
        GHID = input('enter nearby GH-ID')
        q1 = "select count(*) from GHMaster as gh where gh.GHID = %s"
        data_tuple = [GHID]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
            print("GHID is correct")
            return GHID
        else:
            print("enter valid GH-ID")
            return GHidvalid()
gid = GHidvalid()


var = (list[0], list[1],name,age,gender,bloodgroup,address,city,state,pin,phone,gid)

q1 = """INSERT INTO CitizenMaster(ID, IDtype, citizenName ,age ,gender,bloodgroup,address,districtorcity ,state,pincode , phone,  GHID ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
rs.execute(q1,var)
print("inserted successfully")

c.commit()
rs.close()
c.close()