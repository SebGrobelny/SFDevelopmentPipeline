#primary library for etl in python
import petl as etl


#GLOBALS
table1 = etl.fromcsv("Map_SF_Pipeline_2015_Q1.csv")

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

def dictFromTable():
	listings = []

	insights = {}
	#number of applications filed
	insights['Applications Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0

	for i in range(0,len(d)):
			if 'BP FILED' == d[i]['BESTSTAT']:
				insights['Applications Filed'] = insights['Applications Filed']+1

			if 'Resident' == d[i]['PROJECT_TYPE']:
				insights['Residential Project Count'] = insights['Residential Project Count']+1

			if 'Mixed' == d[i]['PROJECT_TYPE']:
				insights['Commercial Project Count'] = insights['Commercial Project Count']+1

			listings.append(d[i])

	listings.insert(0,insights)



	return listings


def filtersFromTable():
	print "In filtersFromTable"
	#filter dictionary used for storing all filters to be displayed 
	filterList = []
	filters = {}

	filters['Select a Year'] = ['2015','2016']
	filters['Select a Quarter'] = ['Q1','Q2','Q3','Q4']

	filters['Select a Neighborhood'] = uniqueNeighborhoods.keys()

	filters['Select a Filing'] = uniqueFilings.keys()

	

	return filters

def getFromTable(neighborhood):

	neighbors = []

	insights = {}
	#number of applications filed
	insights['Applications Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0

	for i in range(0,len(d)):
		#print d[i]
		if neighborhood in d[i]['NEIGHBORHOOD']:
			neighbors.append(d[i])

			if 'BP FILED' == d[i]['BESTSTAT']:
				insights['Applications Filed'] = insights['Applications Filed']+1

			if 'Resident' == d[i]['PROJECT_TYPE']:
				insights['Residential Project Count'] = insights['Residential Project Count']+1

			if 'Mixed' == d[i]['PROJECT_TYPE']:
				insights['Commercial Project Count'] = insights['Commercial Project Count']+1



	neighbors.insert(0,insights)



	return neighbors


def getFiltersFromTable(neighborhoods,filings,years,quarters):

	filteredListing = []

	#TODO might generate different reports depending on what is filtered
	insights = {}
	#number of applications filed
	insights['Applications Filed']=0
	#number of commercial in the works
	insights['Commercial Project Count']=0
	#number of residential in the works
	insights['Residential Project Count']=0


	for i in range(0,len(d)):

		if d[i]['BESTSTAT'] in filings:

			if d[i]['NEIGHBORHOOD'] in neighborhoods:

				if 'BP FILED' == d[i]['BESTSTAT']:
					insights['Applications Filed'] = insights['Applications Filed']+1

				if 'Resident' == d[i]['PROJECT_TYPE']:
					insights['Residential Project Count'] = insights['Residential Project Count']+1

				if 'Mixed' == d[i]['PROJECT_TYPE']:
					insights['Commercial Project Count'] = insights['Commercial Project Count']+1

				filteredListing.append(d[i])

	filteredListing.insert(0,insights)

	return filteredListing







