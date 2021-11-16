import datetime
import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  TruckToGH(AgencyName varchar,agencyid varchar, truckNumber varchar,GHID varchar, destination varchar, datetime varchar,coldstorageid varchar, ' \
  'coldboxID varchar,qty varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many  detail ur going to enter'))
for i in range(rows):
    def nullvalid():
        AgencyName = input('enter AgencyName name')
        if (AgencyName == ''):
            print("pls enter AgencyName , its Mandatory ")
            nullvalid()
        else:
            return AgencyName
    AgencyName = nullvalid()

    def nullvalid1():
        agencyid = input('enter agencyid')
        if (agencyid == ''):
            print("pls enter  agencyid , its Mandatory ")
            nullvalid1()
        else:
            return agencyid
    agencyid= nullvalid1()


    def trucknumvalid():
        trucknum = input('enter truck Registred plate number ')
        # TS 07 DTR 1234
        reg = ('^[a-zA-Z]{2}\\s[0-9]{2}\\s[a-zA-z]{3}\\s[0-9]{4}$')

        if (re.search(reg, trucknum)):
            print("valid truck number")

        else:
            print("invalid truck number")
            return trucknumvalid()
    trucknum = trucknumvalid()

    def IDMatch():
        GHID1 = input('enter GHID to deliver')
        q1 = "select count(*) from ghmaster as ghm where ghm.ghid = %s"
        data_tuple=[GHID1]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
                    print("GHID1 matched")
                    return GHID1
        else:
                    print("GHID  with master Table")
                    return IDMatch()
    def IDwithDestValid():
        GHID=IDMatch()
        q2 = "select districtorcity from ghmaster as ghm where ghm.ghid = %s "
        data_tuple = [GHID]
        v = rs.execute(q2,data_tuple)
        destination = rs.fetchall()
        print(destination)
        return [GHID,destination]

    list= IDwithDestValid()


    def deldatevalid():
        dateOfDelivery = input('enter Date of Delivery')
        date_format = '%d-%m-%Y'
        try:
            deldate_obj = datetime.datetime.strptime(dateOfDelivery, date_format)
            print(deldate_obj)
            return deldate_obj
        except ValueError:
            print("Incorrect data format, should be dd-mm-yyyy")
            return deldatevalid()
    deldate_obj=deldatevalid()

    def coldstoreidvalid():
        cid = input('enter cold storage unit ID ')
        q1 = "select count(*) from ColdStoreUnitMaster as pc where pc.coldstorageID = %s"
        data_tuple = [cid]
        v = rs.execute(q1,data_tuple)
        result = rs.fetchall()
        if(result[0][0] >= 1 ):
            print("coldstore ID is correct")
            return cid
        else:
            print("enter valid cold storage id")
            return coldstoreidvalid()
    cid = coldstoreidvalid()
    def nullvalid2():
        coldboxID = input('enter coldboxID name')
        if (coldboxID == ''):
            print("pls enter coldboxID , its Mandatory ")
            nullvalid2()
        else:
            return coldboxID
    coldboxID = nullvalid2()

    def nullvalid3():
        qty = input('enter qty in liter')
        if(qty.isdigit()):
            print("valid digit")
        else:
            print("pls enter numbers not character")
        if (qty == ''):
            print("pls enter qty , its Mandatory ")
            nullvalid3()
        else:
            return qty
    qty = nullvalid3()


    var=(AgencyName,agencyid, trucknum, list[0],list[1], deldate_obj ,cid, coldboxID, qty )
    q1="""INSERT INTO TruckToGH(AgencyName,agencyid, truckNumber, GHID,destination, datetime,coldstorageid, coldboxID, qty ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rs.execute(q1,var)
print("inserted successfully")
#rs1=c.cursor()

#rc=rs.rowcount
'''for i in range(rc):
    r=rs.fetchone()
a=rs.fetchall()
print(a)
print(rc)'''

c.commit()
rs.close()
c.close()
