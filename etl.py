#primary library for etl in python
import petl as etl

import sqlite3


#GLOBALSe
table1 = etl.fromcsv("2016_Q1.csv")
#    0           1    2           3          4         5             6            7        8           9           10    11        12     13          13          14          15            16   17     18         19    20   21     22   23     24   25     26       27         28           29          30     31           32              33           34             35               36            37          38            39    40
#PROJECT_TYPE	APN	NAMEADDR	Alias	BESTDATE	BESTSTAT	Entitlement	PLN_CASENO	PLN_DESC	BP_APPLNO	BP_DESC	COST	PROPUSE	UNITS	NET_UNITS	AFF_UNITS	NET_AFF_UNITS	RET	NET_RET	MIPS	NET_MIPS	PDR	NET_PDR	MED	NET_MED	CIE	NET_CIE	VISIT	NET_VISIT	FirstFiled	APPLICANT	CONTACT	CONTACTPH	NEIGHBORHOOD	PLAN_AREA	PLAN_DISTRICT	SUPE_DISTRICT	HEIGHT_DISTRICT	ZONING	ZONING_DISTRICT	PLANNER	LOCATION
#parses csv for columns/attributes that we are primarily concerned with
#locationTable--table with coordinates,zoning symbols,addresses and 
#0-BESTSTAT 1-BESTDATE 2-NAMEADDR 5-PROPUSE 7-PROJECT_TYPE 31-ZONING_SIM 33-NEIGHBORHOOD 42-LOCATION
#*[0,2,4,5,12,32,40] 
locationTable = etl.cut(table1,'PROJECT_TYPE','NAMEADDR','BESTDATE','BESTSTAT','PROPUSE','NEIGHBORHOOD','LOCATION' )
#adding the quarter and year to identify the table
locationTable = etl.addfield(locationTable,'Quarter', 'Q1')
locationTable = etl.addfield(locationTable,'Year','2016')



#30-ZONING DISTRICT 31-ZONING_SIM 
# zoningTable = 

#transforms into dictionary
d = etl.dicts(locationTable)

#list of dictionaries
d = list(d)

uniqueNeighborhoods = {}

uniqueFilings = {}

for i in range(0,len(d)):
	if d[i]['NEIGHBORHOOD'] not in uniqueNeighborhoods:
		uniqueNeighborhoods[d[i]['NEIGHBORHOOD']] = 0

	if d[i]['BESTSTAT'] not in uniqueFilings:
		uniqueFilings[d[i]['BESTSTAT']] = 0



def openFileTable(years,quarters):
	#print "In openFileTable"
	table = []
	#traverse through the list of years provided via filters
	for year in years:
		#traverse through the list of quarters provided via filters
		for quarter in quarters:
			fileString = year+'_'+quarter+'.csv'
			#print fileString
			table1 = etl.fromcsv(fileString)

			#TODO--migrate transformations accordingly
			#Q2
			#0        1             2          3           4          5         6         7           8            9        10         11              12         13         14       15       16         17     18   19     20   21     22        23       24   25      26   27    28         29          30         31           32     33      34         35          36           37              38           39               40             41            42             43           44
			#APN	Entitlement	BESTSTAT	BESTDATE	NAMEADDR	Alias	PLN_CASENO	BP_APPLNO	UNITS	NET_UNITS	AFF_UNITS	NET_AFF_UNITS	SECTION415	TENURE_TYPE	COST	PROPUSE	TOTAL_GSF	NET_GSF	CIE	NET_CIE	MED	NET_MED	MIPS	NET_MIPS	PDR	NET_PDR	RET	NET_RET	VISIT	NET_VISIT	FirstFiled	PLN_DESC	BP_DESC	PLANNER	SPONSOR	SP_CONTACT	SP_CONTACTPH	NEIGHBORHOOD	PLAN_AREA	PLAN_DISTRICT	HEIGHT_DISTRICT	ZONING_SIM	ZONING_DISTRICT	SUPE_DISTRICT	Location
			
			#Q3
			#     0             1          2       3            4           5         6           7            8        9         10      11      12            13         14              15           16           17       18     19    20    21  22       23       24        25   26     27   28      29       30          31          32       33       34       35            36   37    38           39             40             41           42              43           44               45              46
			#PROJECT_TYPE	NAMEADDR	Alias	BESTSTAT	BESTDATE	Entitlement	PLN_CASENO	PLN_DESC	PROPUSE	BP_APPLNO	BP_DESC	UNITS	NET_UNITS	AFF_UNITS	NET_AFF_UNITS	SECTION415	TENURE_TYPE	TOTAL_GSF	NET_GSF	CIE	NET_CIE	MED	NET_MED	MIPS	NET_MIPS	PDR	NET_PDR	RET	NET_RET	VISIT	NET_VISIT	APPLICANT	CONTACT	CONTACTPH	COST	FirstFiled	PLANNER	APN	PLAN_AREA	PLN_DISTRICT	SUPE_DISTRICT	ZONING_SIM	ZONING_DISTRICT	ZONING_GEN	NEIGHBORHOOD	HEIGHT_DISTRICT	Location

			#Q4
			# 0        1           2            3        4        5       6            7              8               9          10           11        12         13   14        15    16           17               18           19        20      21    22   23   24      25       26         27   28     29   30     31        32         33          34       35             36          37      38           39        40        41              42              43              44          45         46        47             48             49
			#APN	BESTSTAT	BESTDATE	NAMEADDR	Alias	UNITS	NET_UNITS	AFF_UNITS	NET_AFF_UNITS	SECTION415	TENURE_TYPE	PLN_CASENO	BP_APPLNO	PROPUSE	COST	BP_DESC	PLN_DESC	PROJECT_TYPE	ENTITLEMENT	TOTAL_GSF	NET_GSF	CIE	NET_CIE	MED	NET_MED	MIPS	NET_MIPS	PDR	NET_PDR	RET	NET_RET	VISIT	NET_VISIT	APPLICANT	CONTACT	CONTACTPHONE	FirstFiled	PLANNER	PLAN_AREA	PUBLICREALM	STATUS	PLAN_DISTRICT	SUPE_DISTRICT	ZONING_SIM	ZONING_DISTRICT	ZONING_GEN	ZONING	HEIGHT_DISTRICT	NEIGHBORHOOD	Location
			if quarter == 'Q1':
				#attrList = [0,2,4,5,12,32,40]
				table1 = etl.cut(table1,'PROJECT_TYPE','NAMEADDR','BESTDATE','BESTSTAT','PROPUSE','NEIGHBORHOOD','LOCATION' )

			if quarter == 'Q2':
				print quarter
				#attrList = [2,3,4,15,37,42,44]
				table1 = etl.cut(table1, 'BESTSTAT','BESTDATE','NAMEADDR','PROPUSE','NEIGHBORHOOD','ZONING_GEN','Location')

			if quarter == 'Q3':
				#attrList = [0,1,3,4,8,44,46]
				table1 = etl.cut(table1, 'PROJECT_TYPE','NAMEADDR','BESTSTAT','BESTDATE','PROPUSE','NEIGHBORHOOD','LOCATION')

			if quarter == 'Q4':
				#attrList = [1,2,3,13,17,48,49]
				table1 = etl.cut(table1, 'BESTSTAT','BESTDATE','NAMEADDR','PROPUSE','PROJECT_TYPE','NEIGHBORHOOD','Location')




			#adding the quarter and year to identify the table
			table1 = etl.addfield(table1,'Quarter', quarter)
			table1 = etl.addfield(table1,'Year', year)

			#print tempTable
			
			table.append(table1)

	return table



def dictFromTable():

	insights = {}
	#number of applications filed
	insights['Building Permits Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0



	listings = []

	print "in here "
	years = ['2016']
	quarters =['Q1','Q2','Q3','Q4']

	tableList = openFileTable(years,quarters)

	for table in tableList:
		#transforms into dictionary

		d = etl.dicts(table)
		# print etl.look(table)
		#list of dictionaries
		b = list(d)

		for i in range(0,len(b)):
				#print b[i]
				if 'BP FILED' == b[i]['BESTSTAT']:
					insights['Building Permits Filed'] = insights['Building Permits Filed']+1

				if 'Resident' == b[i]['PROJECT_TYPE']:
					insights['Residential Project Count'] = insights['Residential Project Count']+1

				if 'Mixed' == b[i]['PROJECT_TYPE']:
					insights['Commercial Project Count'] = insights['Commercial Project Count']+1

				listings.append(b[i])

	listings.insert(0,insights)



	return listings


def filtersFromTable():
	#print "In filtersFromTable"
	#filter dictionary used for storing all filters to be displayed 
	filterList = []
	filters = dict()

	filters['Select a Year'] = ['2016']
	filters['Select a Quarter'] = ['Q1','Q2','Q3','Q4']

	filters['Select a Neighborhood'] = uniqueNeighborhoods.keys()

	filters['Select a Filing'] = uniqueFilings.keys()

	print(type(filters))

	return filters

#TODO incoprotate select filters into neighborhood stuff 
def getFromTable(zipcode):

	print "in here "
	neighbors = []



	insights = {}
	#number of applications filed
	insights['Building Permits Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0

	conn = sqlite3.connect('dev2017Q1.db')


	cur = conn.cursor() 

	cur.execute("SELECT * FROM dev2017Q1 WHERE ZIPCODE = ?;", (str(zipcode),))
	all_rows = list(cur.fetchall())

	conn.commit()
	conn.close()

	for comp in all_rows:
		element = {}
		count = 0

		print comp
		print len(comp)
		element['BESTSTAT'] = comp[0]
		element['BESTDATE'] = comp[1]
		element['ADDRESS'] = comp[2]
		element['Zipcode'] = comp[3]
		element['PROJECT_TYPE'] = comp[4]
		element['PROPERTY_USE'] = comp[5]
		element['Neighborhood'] = comp[6]
		print comp[6]
		element['Location'] = comp[7]
		element['Quarter'] = comp[8]
		print comp[7]
		element['Year'] = comp[9]

		neighbors.append(element)

		if 'BP FILED' == d[i]['BESTSTAT']:
			insights['Building Permits Filed'] = insights['Building Permits Filed']+1

		if 'Resident' == d[i]['PROJECT_TYPE']:
			insights['Residential Project Count'] = insights['Residential Project Count']+1

		if 'Mixed' == d[i]['PROJECT_TYPE']:
			insights['Commercial Project Count'] = insights['Commercial Project Count']+1

	neighbors.insert(0,insights)

	return neighbors




def getFiltersFromTable(neighborhoods,filings,years,quarters):

	filteredListing = []

	#if no filters selected from filters assume all are desired
	if filings[0] == 'null':
		filings = uniqueFilings.keys()

	if years[0] == 'null':
		years = ['2016']

	if quarters[0] == 'null':
		quarters = ['Q1','Q3','Q4']

	if neighborhoods[0] == 'null':
		neighborhoods = uniqueNeighborhoods.keys()

	tableList = openFileTable(years,quarters)

	#TODO might generate different reports depending on what is filtered
	insights = {}
	#number of applications filed
	insights['Building Permits Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0

	for table in tableList:

		#transforms into dictionary

		d = etl.dicts(table)
		# print etl.look(table)
		#list of dictionaries
		#print d
		b = list(d)


		for i in range(0,len(b)):


			if b[i]['BESTSTAT'] in filings:

				if b[i]['NEIGHBORHOOD'] in neighborhoods:

					if 'BP FILED' == b[i]['BESTSTAT']:
						insights['Building Permits Filed'] = insights['Building Permits Filed']+1

					#print b[i]

					if b[i]['Quarter'] == 'Q2':
						continue
						# print "in here"
						# if 'Resident' == b[i]['ZONING_GEN']:
						# 	insights['Residential Project Count'] = insights['Residential Project Count']+1
						# if 'Mixed' == b[i]['ZONING_GEN']:
						# 	insights['Commercial Project Count'] = insights['Commercial Project Count']+1
					else:

						if 'Resident' == b[i]['PROJECT_TYPE']:
							insights['Residential Project Count'] = insights['Residential Project Count']+1

						if 'Mixed' == b[i]['PROJECT_TYPE']:
							insights['Commercial Project Count'] = insights['Commercial Project Count']+1

					filteredListing.append(d[i])

	filteredListing.insert(0,insights)

	return filteredListing







