#primary library for etl in python
import petl as etl


#GLOBALS
table1 = etl.fromcsv("2015_Q1.csv")

#parses csv for columns/attributes that we are primarily concerned with
#locationTable--table with coordinates,zoning symbols,addresses and 
#0-BESTSTAT 1-BESTDATE 2-NAMEADDR 5-PROPUSE 7-PROJECT_TYPE 31-ZONING_SIM 33-NEIGHBORHOOD 42-LOCATION 
locationTable = etl.cut(table1, *[0,1,2,5,7,33,42])
#adding the quarter and year to identify the table
locationTable = etl.addfield(locationTable,'Quarter', 'Q1')
locationTable = etl.addfield(locationTable,'Year','2015')



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

# for key in uniqueNeighborhoods.keys():
# 	print key

# for key in uniqueFilings.keys():
# 	print key


def openFileTable(years,quarters):
	#print "In openFileTable"
	table = []
	#traverse through the list of years provided via filters
	for year in years:
		#traverse through the list of quarters provided via filters
		for quarter in quarters:
			#print quarter
			#TODO--migrate transformations accordingly
			if quarter == 'Q1':
				attrList = [0,1,2,5,7,33,42]

			if quarter == 'Q4':
				attrList = [0,2,4,5,13,35,43]

			if quarter == 'Q3':
				attrList = [0,2,4,5,11,38,43]

			if quarter == 'Q2':
				attrList = [0,2,4,5,9,39,43]

			fileString = year+'_'+quarter+'.csv'
			table1 = etl.fromcsv(fileString)
			#0-BESTSTAT 1-BESTDATE 2-NAMEADDR 5-PROPUSE 7-PROJECT_TYPE 31-ZONING_SIM 33-NEIGHBORHOOD 42-LOCATION 
			tempTable = etl.cut(table1, *attrList)
			if quarter == 'Q3':
				tempTable = etl.convert(tempTable, 'Location', lambda v:v[5:])
			#adding the quarter and year to identify the table
			tempTable = etl.addfield(tempTable,'Quarter', quarter)
			tempTable = etl.addfield(tempTable,'Year', year)

			#print tempTable
			
			table.append(tempTable)

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


	years = ['2015']
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

	filters['Select a Year'] = ['2015','2016']
	filters['Select a Quarter'] = ['Q1','Q2','Q3','Q4']

	filters['Select a Neighborhood'] = uniqueNeighborhoods.keys()

	filters['Select a Filing'] = uniqueFilings.keys()

	print(type(filters))

	return filters

#TODO incoprotate select filters into neighborhood stuff 
def getFromTable(neighborhood):

	neighbors = []

	insights = {}
	#number of applications filed
	insights['Building Permits Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0

	for i in range(0,len(d)):
		#print d[i]
		if neighborhood in d[i]['NEIGHBORHOOD']:
			neighbors.append(d[i])

			

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
		years = ['2015','2016']

	if quarters[0] == 'null':
		quarters = ['Q1','Q2','Q3','Q4']

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
		b = list(d)


		for i in range(0,len(b)):

			if b[i]['BESTSTAT'] in filings:

				if b[i]['NEIGHBORHOOD'] in neighborhoods:

					if 'BP FILED' == b[i]['BESTSTAT']:
						insights['Building Permits Filed'] = insights['Building Permits Filed']+1

					if 'Resident' == b[i]['PROJECT_TYPE']:
						insights['Residential Project Count'] = insights['Residential Project Count']+1

					if 'Mixed' == b[i]['PROJECT_TYPE']:
						insights['Commercial Project Count'] = insights['Commercial Project Count']+1

					filteredListing.append(d[i])

	filteredListing.insert(0,insights)

	return filteredListing







