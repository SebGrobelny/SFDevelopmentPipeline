#sql interfacing 
import sqlite3
import csv
import urllib, json, time


from geopy.geocoders import Nominatim




class csvrd(object):

	
	def GoogGeoAPI(self, latlang):
		api="AIzaSyC2AuRFA97c6zDlq87lXKl9HMUwHxQjbew"
		delay=5
		base = r"https://maps.googleapis.com/maps/api/geocode/json?"
		addP = "latlng=" + latlang
		GeoUrl = base + addP + "&key=" + api
		response = urllib.urlopen(GeoUrl)
		jsonRaw = response.read()
		jsonData = json.loads(jsonRaw)
		if jsonData['status'] == 'OK':
			resu = jsonData['results'][0]
			finList = resu['formatted_address']
		else:
			finList = [None,None,None]
		time.sleep(delay) #in seconds
		return finList


	def create2017Q1Table(self):


		#database stuff
		filename = "2017_Q1.csv"
		conn = sqlite3.connect('dev2017Q1.db')


		cur = conn.cursor() 
		cur.execute("""CREATE TABLE IF NOT EXISTS dev2017Q1(BESTSTAT varchar, BESTDATE varchar, NAMEADDR varchar, ZIPCODE int, PROPUSE varchar, PROJECT_TYPE varchar, NEIGHBORHOOD varchar, LOCATION varchar, QUARTER varchar, YEAR varchar)""")
		filename.encode('utf-8')
		geolocator = Nominatim()

		#0-BESTSTAT 1-BESTDATE 2-NAMEADDR ZIPCODE 5-PROPUSE 7-PROJECT_TYPE 31-ZONING_SIM 33-NEIGHBORHOOD 42-LOCATION 
		# if quarter == 'Q1':
		# 	attrList = [0,1,2,5,7,33,42]
		#		0    		 1 			2 		3 		4 			5 				6 			7   	8 			9   		10 			11 					12 			13  		14 			15 			16 			17 			18 			19 		20 			21 			22 		23 		24 			25 		26 		27 		28 			29 		30 			31 		32 			33 		34 			35 			36 			37 			38 			39 				40 				41 			42 					43 					44 				45 				46 				47 			48 			49 		
		# ['PROJECT_TYPE', 'APN', 'NAMEADDR', 'PHASE', 'ALIAS', 'ENTITLEMENT', 'BESTSTAT', 'BESTDATE', 'UNITS', 'NET_UNITS', 'AFF_UNITS', 'NET_AFF_UNITS', 'SECTION415', 'TENURE_TYPE', 'DA', 'PLN_CASENO', 'PLN_DESC', 'BP_APPLNO', 'BP_DESC', 'COST', 'PROPUSE', 'TOTAL_GSF', 'NET_GSF', 'CIE', 'NET_CIE', 'MED', 'NET_MED', 'MIPS', 'NET_MIPS', 'PDR', 'NET_PDR', 'RET', 'NET_RET', 'VISIT', 'NET_VISIT', 'PLANNER', 'APPLICANT', 'CONTACT', 'CONTACTPH', 'NEIGHBORHOOD', 'ZONING_SIM', 'ZONING_GEN', 'ZONING_DISTRICT', 'HEIGHT_DISTRICT', 'SUPE_DISTRICT', 'PLAN_DISTRICT', 'PLAN_AREA', 'PUBLICREALM', 'STATUS', 'Location']

		with open(filename,'rU') as f:
			count = 0
			reader = csv.reader(f)
			
			for field in reader:
				if count == 0:
					print field
					count = count+1
					continue
				else:
					entry = list()
					entry.append(field[6])
					entry.append(field[7])
					entry.append(field[2])

					format = field[49].strip("()")
					coordinates = format.split(",")
					coordinatesString = str(coordinates[0])+","+str(coordinates[1])
					#print coordinatesString
					address = self.GoogGeoAPI(coordinatesString)
					# location = geolocator.reverse(coordinatesString)
					# address = location.raw['address']
					if type(address) == list:
						entry.append(" ")
					else:
						address = address.split(",")

						print address[2][4:]

						entry.append(address[2][4:])


					entry.append(field[20])
					entry.append(field[0])
					entry.append(field[39])
					entry.append(field[49])
					entry.append('Q1')
					entry.append('2017')

					cur.execute("INSERT INTO dev2017Q1 VALUES (?,?,?,?,?,?,?,?,?,?);", entry)

				count = count+1
		conn.commit()
        #conn.close()



		# # if quarter == 'Q2':
		# # 	attrList = [0,2,4,5,9,39,43]
		# filename = "2015_Q2.csv"
		# filename.encode('utf-8')
		# with open(filename,'rU') as f:
		# 	count = 0
		# 	reader = csv.reader(f)
			
		# 	for field in reader:
		# 		if count == 0:
		# 			print "in"
		# 			count = count+1
		# 			continue
		# 		else:
		# 			entry = list()
		# 			entry.append(field[0])
		# 			entry.append(field[2])
		# 			entry.append(field[4])
		# 			format = field[43].strip("()")
		# 			coordinates = format.split(",")
		# 			coordinatesString = str(coordinates[0])+","+str(coordinates[1])
		# 			location = geolocator.reverse(coordinatesString)
		# 			address = location.raw['address']

		# 			if 'postcode' in address:
		# 				entry.append(address['postcode'])
		# 			else:
		# 				entry.append(" ")

		# 			entry.append(field[5])
		# 			entry.append(field[9])
		# 			entry.append(field[39])
		# 			entry.append(field[43])
		# 			entry.append('Q2')
		# 			entry.append('2015')

		# 			cur.execute("INSERT INTO dev2015 VALUES (?,?,?,?,?,?,?,?,?,?);", entry)

		# 		count = count+1

		# # if quarter == 'Q3':
		# # 	attrList = [0,2,4,5,11,38,43]
		# filename = "2015_Q3.csv"
		# filename.encode('utf-8')

		# with open(filename,'rU') as f:
		# 	count = 0
		# 	reader = csv.reader(f)
			
		# 	for field in reader:
		# 		if count == 0:
		# 			print "in"
		# 			count = count+1
		# 			continue
		# 		else:
		# 			entry = list()
		# 			entry.append(field[0])
		# 			entry.append(field[2])
		# 			entry.append(field[4])
		# 			format = field[43].strip("()")
		# 			coordinates = format.split(",")
		# 			coordinatesString = str(coordinates[0])+","+str(coordinates[1])
		# 			location = geolocator.reverse(coordinatesString)
		# 			address = location.raw['address']

		# 			if 'postcode' in address:
		# 				entry.append(address['postcode'])
		# 			else:
		# 				entry.append(" ")

		# 			entry.append(field[5])
		# 			entry.append(field[11])
		# 			entry.append(field[38])
		# 			entry.append(field[43])
		# 			entry.append('Q3')
		# 			entry.append('2015')

		# 			cur.execute("INSERT INTO dev2015 VALUES (?,?,?,?,?,?,?,?,?,?);", entry)

		# 		count = count+1

  # #       if quarter == 'Q4':
		# # 	attrList = [0,2,4,5,13,35,43]
		# filename = "2015_Q4.csv"
		# filename.encode('utf-8')

		# with open(filename,'rU') as f:
		# 	count = 0
		# 	reader = csv.reader(f)
			
		# 	for field in reader:
		# 		if count == 0:
		# 			print "in"
		# 			count = count+1
		# 			continue
		# 		else:
		# 			entry = list()
		# 			entry.append(field[0])
		# 			entry.append(field[2])
		# 			entry.append(field[4])
		# 			format = field[43].strip("()")
		# 			coordinates = format.split(",")
		# 			coordinatesString = str(coordinates[0])+","+str(coordinates[1])
		# 			location = geolocator.reverse(coordinatesString)
		# 			address = location.raw['address']

		# 			if 'postcode' in address:
		# 				entry.append(address['postcode'])
		# 			else:
		# 				entry.append(" ")

		# 			entry.append(field[5])
		# 			entry.append(field[11])
		# 			entry.append(field[38])
		# 			entry.append(field[43])
		# 			entry.append('Q4')
		# 			entry.append('2015')

		# 			cur.execute("INSERT INTO dev2015 VALUES (?,?,?,?,?,?,?,?,?,?);", entry)

		# 		count = count+1







c = csvrd().create2017Q1Table()