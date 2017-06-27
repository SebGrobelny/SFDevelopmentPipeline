#flask modules
from flask import Flask,  jsonify, make_response, abort, request, render_template
from flask_cors import CORS, cross_origin

from etl import dictFromTable, getFromTable, filtersFromTable, getFiltersFromTable

app = Flask(__name__)
CORS(app)


@app.route('/homepage')
def main():

	return render_template('main.html')

#GET requests
#obtain filters
@app.route('/loadFilters', methods=['GET'])
def loadFilters():
	listingDict = filtersFromTable()

	return jsonify(listingDict)

#obtain all listings
@app.route('/getAll', methods=['GET'])
def getAllDict():
	listingDict = dictFromTable()

	return jsonify(listingDict)

#obtain listings from a certain neighborhood--used with the map
@app.route('/getNeighborhood/neighborhood=<neighborhood>', methods=['GET'])
def getNeighborhoodDict(neighborhood):

	listingDict = getFromTable(neighborhood)

	return jsonify(listingDict)

#obtain listings based on filters
@app.route('/getFilters/neighborhood=<neighborhoods>/filing=<filings>/year=<years>/quarter=<quarters>', methods=['GET'])
def getFilters(neighborhoods,filings,years,quarters):

	neighborhoods = neighborhoods.split(',')
	filings = filings.split(',')
	years = years.split(',')
	quarters = quarters.split(',')


	listingDict = getFiltersFromTable(neighborhoods,filings,years,quarters)

	return jsonify(listingDict)







#always goes at the bottom of the page

#app doesn't cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

##has to do with the WSGI
if __name__ == '__main__':
    app.run(debug=True)