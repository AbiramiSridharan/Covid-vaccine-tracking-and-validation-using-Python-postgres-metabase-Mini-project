import re
import datetime
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  productionDetails(compID varchar,dateOfProduction date,unitOfProduction numeric,plantLocation varchar,plantID varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many company detail ur going to enter'))
for i in range(rows):

    def compidvalid():
        compId = input('enter company id')
        q1 = "select count(*) from phramacompmaster as pc where pc.compID = %s"
        data_tuple = [compId]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if(result[0][0] >= 1 ):
            print("compid is correct")
            return compId
        else:
            print("enter valid company code")
            return compidvalid()
    cid = compidvalid()

    def datevalid():
        dateofprod = input('enter Date of production')
        date_format = '%d-%m-%Y'

        try:
            date_obj = datetime.datetime.strptime(dateofprod, date_format)
            start = datetime.datetime.strptime("01-01-2019", "%d-%m-%Y")
            end = datetime.datetime.strptime("12-03-2021", "%d-%m-%Y")
            if start <=date_obj <= end:
                print(date_obj)
                return dateofprod
            else:
                print("date is not within the range")
                return datevalid()
        except ValueError:
            print("Incorrect data format, should be dd-mm-yyyy")
            return datevalid()

            #dateofprod = datetime.datetime.now()

    dateofprod=datevalid()

    unit = input('enter Unit Of production in Liters')

    location= input('enter production plant location')

    plantID=input("production plant ID ")


    var=(cid,dateofprod,unit,location,plantID)
    q1="""INSERT INTO productionDetails(compID,dateOfProduction,unitOfProduction,plantLocation,plantID) VALUES (%s,%s,%s,%s,%s)"""
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
