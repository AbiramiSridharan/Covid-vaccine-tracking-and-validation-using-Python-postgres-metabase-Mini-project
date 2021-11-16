import datetime
import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  toColdStorageUnit(transportAgencyName varchar,transportAgencyid varchar, trucknumber varchar ,noOfColdbox numeric, ' \
  'coldstorageid varchar, qty_in_liters numeric,loadingdate date,dateOfDelivery date)'
rs.execute(q)
print("table created")
rows=int(input('how many detail ur going to enter'))
for i in range(rows):

    def nullvalid():
            TAName = input('enter TransportAgencyName ')
            if(TAName==''):
                print("pls enter TransportAgencyName , its Mandatory ")
                nullvalid()
            else:
                return TAName
    TAName=nullvalid()


    def nullvalid1():
        TAid = input('enter transportAgencyid')
        if (TAid == ''):
            print("pls enter TransportAgency ID , its Mandatory ")
            nullvalid()
        else:
            return TAid
    TAid = nullvalid1()


    def trucknumvalid():
        trucknum = input('enter truck Registred plate number ')
        #TS 07 DTR 1234
        reg = ('^[a-zA-Z]{2}\\s[0-9]{2}\\s[a-zA-z]{3}\\s[0-9]{4}$')

        if (re.search(reg, trucknum)):
                print("valid truck number")

        else:
                print("invalid truck number")
                return trucknumvalid()
    trucknum = trucknumvalid()
    def noofcoldvalid():
         noofcold = input('enter number Of Coldbox loaded')
         if(noofcold.isdigit()==True):
            print("valid")
            return noofcold
         else:
             print("enter number not character")
             return noofcoldvalid()
    noofcold=noofcoldvalid()

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
    def Qty():
         qty = input('enter number Of Quantity loaded in Liters')
         if(qty.isdigit()==True):
            print("valid")
            return qty
         else:
             print("enter number- not character")
             return Qty()
    qty=Qty()

    def ldatevalid():
        loadingdate = input('enter loadingDate')
        date_format = '%d-%m-%Y'
        try:
            ldate_obj = datetime.datetime.strptime(loadingdate, date_format)
            print(ldate_obj)
            return ldate_obj
        except ValueError:
            print("Incorrect data format, should be dd-mm-yyyy")
            return ldatevalid()

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


    def datevalid():
            deldate=deldatevalid()
            ldate = ldatevalid()
            if ldate <= deldate:
                print(deldate,ldate)
                return [ldate,deldate];
            else:
                print("date is not within the range")
                return datevalid()

    list=datevalid()



    var=(TAName,TAid,trucknum,noofcold,cid,qty,list[0],list[1])
    q1="""INSERT INTO toColdStorageUnit(transportAgencyName ,transportAgencyid , trucknumber  ,noOfColdbox,coldstorageid, qty_in_liters,
    loadingdate,dateOfDelivery ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    rs.execute(q1,var)
print("inserted successfully")


c.commit()
rs.close()
c.close()