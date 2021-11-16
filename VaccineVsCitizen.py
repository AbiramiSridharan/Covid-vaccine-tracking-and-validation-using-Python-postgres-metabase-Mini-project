from random import randrange
from datetime import timedelta, datetime
import re
import psycopg2 as pg
c = pg.connect(host="localhost", database="covidtrack",user="postgres",password="abi_postgres")
rs=c.cursor()
q='create table if not exists  VaccineVsCitizen(citizenID varchar, datetime varchar,GHID varchar, DocID varchar, coldstorageid varchar)'
rs.execute(q)
print("table created")
rows=int(input('how many  detail ur going to enter'))
for i in range(rows):
    def citizenIDvalid():
        citizenID = input('enter citizenID')
        q1 = "select count(*) from citizenmaster as cm where cm.id = %s"
        data_tuple = [citizenID]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
            print("citizenID is correct")
            return citizenID
        else:
            print("enter valid citizenID")
            return citizenIDvalid()

    def IDrepeatevalid():
        citizenID = citizenIDvalid()
        q1 = "select count(*) from VaccineVsCitizen as cm where cm.citizenid = %s"
        data_tuple = [citizenID]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
            print("citizenID already exist for vaccine appoinment pls enter again")
            return citizenIDvalid()

        else:
            print(" new citizenID inserted")
            return citizenID
    citizenID = IDrepeatevalid()

    date_format = '%d-%m-%Y %H-%M-%S'
    q1 = "select count(*) from citizenmaster"
    v = rs.execute(q1)
    result = rs.fetchall()
    r = result[0][0]
    print("number of rows", r)

    def dateofapponiment(start, end):
        date_format = '%d-%m-%Y %H-%M-%S'
        q1 = "select count(*) from citizenmaster"
        v = rs.execute(q1)
        result = rs.fetchall()
        r = result[0][0]
        print("number of rows", r)

        for i in range(r):
         delta = end - start
         int_delta = (delta.days * i * 60*60) + 60
         random_minute = randrange(int_delta)
         date=start + timedelta(seconds=random_minute)
        return date

    d1 = datetime.strptime('1/1/2021   9:00 AM', '%d/%m/%Y %I:%M %p')
    d2 = datetime.strptime('1/5/2021  9:00 AM', '%d/%m/%Y %I:%M %p')

    dateofapp=dateofapponiment(d1,d2)
    q="update VaccineVsCitizen set datetime=%s"
    data_tuple = [dateofapp]
    v = rs.execute(q1, data_tuple)
    print(dateofapp)


    def GHIDValid():
        GHID = input('enter GH ID')
        q1 = "select count(*) from ghmaster as gh where gh.ghid = %s"
        data_tuple = [GHID]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
            print("GHID is correct")
            return citizenID
        else:
            print("enter valid GHID")
            return citizenIDvalid()

    GHID = GHIDValid()


    def nullvalid2():
        DocID = input('enter DocID')

        if (DocID == ''):
            print("pls enter DocID , its Mandatory ")
            nullvalid2()
        else:
            return DocID
    DocID= nullvalid2()


    def coldstoreidvalid():
        cid = input('enter cold storage unit ID ')
        q1 = "select count(*) from ColdStoreUnitMaster as pc where pc.coldstorageID = %s"
        data_tuple = [cid]
        v = rs.execute(q1, data_tuple)
        result = rs.fetchall()
        if (result[0][0] >= 1):
            print("coldstore ID is correct")
            return cid
        else:
            print("enter valid cold storage id")
            return coldstoreidvalid()
    cid = coldstoreidvalid()


    var=(citizenID ,dateofapp,GHID,DocID,cid)
    q1="""INSERT INTO VaccineVsCitizen(citizenID , datetime ,GHID , DocID , coldstorageid) VALUES (%s,%s,%s,%s,%s)"""
    rs.execute(q1,var)
print("inserted successfully")

c.commit()
rs.close()
c.close()
