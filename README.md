**Postgres DB design**
**Aim of this mini project is to track, validate and Analyse the vaccine details from phrama companies to hospitals** 

**Covid vaccine tracking lookup**
- company name,company code
- cold storage id

**storage unit master:**
- city,state,country

**recivermaster:**
- GH-ID
- city/district,state
 
**Citizenmaster**
- voter id/aadhaarid/ ration card id
 
**GH-Master**
- GH-ID
 
**Master**
**PharmacompanyMaster**
- company name,companyID ,address,city ,state ,country,pinCode,phone
 
**Coldstorageunitmaster**
- companyID, coldstorageID,address, city , state, country, pinCode 

**GH-Master**
- GH-ID, chiefDocName,DocID,GH-Address, district/city, state,country ,pinCode,phone,email;

**citizen master**
- ID,ID-type[voter id/aadhaarid/ PANcard id],Name,address,age,gender, bloodgroup, address, district/city,state ,postalcode, nearby GH-ID

***Transaction***

**vaccine appointment**
- citizenid,date-time, Gh-ID,DOc-ID
- one person 1 appointment(Yet to do)

**vaccination details**
- citizenID, date-time,GH-ID, Doc-ID, coldboxID,package/bottle-id, coldstorageid

**Truck delivery to GH**
- agency id, truckNumber, destination, datetime,coldstorageid, coldboxID,qty, GH-ID

**Tocold storage unit**
- TransportagencyName,transportagencyid, trucknumber, date,noOFColdbox,coldstorageid, qty, destination,
	loadingdate ,dateOfDelivery

**productionDetails**
 - companycode,date of production,unit of production,plant location


**Python code Validation-Details** 
1) Citizen ID validation
   - PAN (or)
   - AADHAR(or)
   - VoterID(or) (any1 id mandatory field check)
2) Pincode
3) Phone number
4) EmailID
5) CitizenID matches with CitizenMaster
6) CompanyID matches with PhramacompanyMaster
7) Coldstorage 
   - StorageID matches with coldstorageunitMaster
   - ColdboxID match
   - Loading < Delivery date validation
8) GH-master
   - GH-ID matches with Gh-Master(Gh-ID)
   - GH delivery - Tocold storage unit:qty reduces
9) Vaccination appoinment
   - appoinment time-date 
   - Doc-ID matches 
10) Date of Production (date within 2years range)
11) Date format validation
12) Truck Registration's plate number validation
13) Null check for all mandatoryfields
14) Truck delivery-Query validation(GH-ID matches with Destination)with GHmaster
15) Citizen age <10 and >70 not eligible to get vaccination 


**After getting inputs and validated using python, load datas in postgres and connect with Metabase to Analyse**
![Screenshot (1438)](https://user-images.githubusercontent.com/94047237/142053853-e4e3ec18-c2bf-4ddd-8c3e-7d344affcba9.png)
![Screenshot (1439)](https://user-images.githubusercontent.com/94047237/142053862-318d3552-73a6-4d3d-8013-a297020023e7.png)
![Screenshot (1440)](https://user-images.githubusercontent.com/94047237/142053866-1413170d-548c-4888-996d-3489c9231d18.png)
![Screenshot (1443)](https://user-images.githubusercontent.com/94047237/142053867-e48ca90c-7a38-4456-8f1a-075c944245c0.png)
![Screenshot (1434)](https://user-images.githubusercontent.com/94047237/142053869-628c5a61-953e-4b36-9153-3ae602f1532e.png)
![Screenshot (1436)](https://user-images.githubusercontent.com/94047237/142053872-a43de0a7-6c11-4fe0-a894-66f82af61522.png)
![Screenshot (1437)](https://user-images.githubusercontent.com/94047237/142053874-1885e2fa-ce22-4488-a611-1dc58146e7c1.png)

