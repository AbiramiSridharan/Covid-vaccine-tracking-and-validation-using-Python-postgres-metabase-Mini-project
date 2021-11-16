import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists ColdStoreUnitMaster(compID varchar,coldstorageID varchar,address varchar, city varchar ,' \
  ' state varchar,country varchar, pincode varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many company detail ur going to enter'))
for i in range(rows):


    def compidvalid():
        compId = input('enter company id')
    #q1 = "select count(*) from phramacompmaster as pc where pc.compID = '"+compId+"'"
    #print(q1)
    #v = rs.execute(q1)

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
    coldstoreID=input('enter coldstorageID')

    address = input('enter coldstorage unit address')
    city = input("enter city name")
    state = input('enter company State')
    pin = input('enter pincode')
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
var=(cid,coldstoreID,address,city,state,country,pin)
q2="""INSERT INTO ColdStoreUnitMaster(compID,coldstorageID,address,city,state,country,pincode) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
rs.execute(q2,var)
print("inserted successfully")
c.commit()
rs.close()
c.close()














































































































