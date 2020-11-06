#-. QueryMaker class .-#
#.- Perform SPARQL queries and loads the data graph .-#

# Imports
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.plugins.sparql import prepareQuery
from SPARQLWrapper import SPARQLWrapper, JSON

# Namespaces
ns = Namespace("http://www.semanticweb.org/group16/ontologies/air-quality#")
sc = Namespace("https://schema.org/")
wiki = Namespace("https://www.wikidata.org/wiki/")

# Class
class QueryMaker:

    # Init function
    def __init__(self):
        self.query = ""
        self.order = ""
        self.paramsList = []
        if not(hasattr(self, "graph")):
            self.normalGraph = Graph()
            self.appGraph = Graph()
            self.sparql = SPARQLWrapper("http://localhost:9000/sparql")
            self.graph = self.normalGraph
        # END IF
    # END FUNCTION


    # addSelect(*string) -> ()
    #   Allows user to choose which parameters will be retrieved
    #   example: addSelect("?Measure", "?Station")
    def addSelect(self, *paramsToSelect : str):
        self.query = "SELECT DISTINCT\n\t"
        for param in paramsToSelect:
            self.query = self.query + param + " "
        # END FOR
        self.query = self.query[0:len(self.query)-1]
        self.query = self.query + "\nWHERE {\n\t"
    # END FUNCTION


    # addParam(string, string, string) -> ()
    #   Inserts into the query the triplet subject, predicate, object
    #   example: addParam("?Measure", "rdf:type", "ns:Measurement")
    def addParam(self, s : str, p : str, o : str):
        self.paramsList.append((s, p, o))
    # END FUNCTION


    # addFilter(string) -> ()
    #   Inserts into the query a filtering sentence
    #   example: addFilter("REGEX (?StLabel, \"Moratalaz\")")
    def addFilter(self, filter : str):
        filter = self.fixDate(filter)
        self.paramsList.append(("\tFILTER", filter))
    # END FUNCTION


    # addOrder(string) -> ()
    #   Orders the result of the query with the ordering sentence passed
    #   example: addOrder("xsd:integer(?Code)")
    def addOrder(self, order : str):
        self.order = self.order + "ORDER BY " + order
    # END FUNCTION


    # executeQuery () -> List<Dictionary>
    #   Queries the graph and returns a list with the dictionary for each row
    #   example: executeQuery() -> [{"Measure":"http:/...", "Station":"http:/..."},
    #                                "Measure":"http:/...", "Station":"http:/..."}
    #                              ]
    def executeQuery(self):
        for param in self.paramsList:
            for item in param:
                self.query = self.query + item + " "
            # END FOR
            if "\tFILTER" in param:
                self.query = self.query[0:len(self.query)-1]
            else:
                self.query = self.query + "."
            # END IF-ELSE
            self.query = self.query + "\n\t"
        # END FOR
        self.query = self.query[0:len(self.query)-1]
        self.query = self.query + "}"
        if not(self.order == ""):
            self.query = self.query + "\n" + self.order
        # END IF
        self.query = self.getNamespaces() + self.query

        self.sparql.setQuery(self.query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        listResult = []

        for row in results["results"]["bindings"]:
            rowDict = {}
            for key in row.keys():
                rowDict[key] = row[key]["value"]
                if(key == "Date"):
                    rowDict[key] = row[key]["value"][0:len(row[key]["value"])-10]
                # END IF
            # END FOR
            listResult.append(rowDict)
        # END FOR
        return listResult
    # END FUNCTION


    ## appQuery() -> List<Dictionary>
    #   Queries the measurements with given filters (or not)
    #   example: appQuery([False, False, False], []) -> List of all measurements
    #   example: appQuery([True, False, False], [{"Place":"District","ID":"#districtID"}]) -> List of measurements in given district
    #   example: appQuery([True, False, False], [{"Place":"Street","ID":"#streetID"}]) -> List of measurements in given street
    #   example: appQuery([True, False, False], [{"Place":"Station","ID":"#stationCode"}]) -> List of measurements in given station
    #   example: appQuery([False, True, False], ["2014"]) -> List of measurements in 2014
    #   example: appQuery([False, True, False], ["2014-04"]) -> List of measurements in April 2014
    #   example: appQuery([False, True, False], ["2014-04-26"]) -> List of measurements in 26th April 2014
    #   example: appQuery([False, False, True], ["#magnitudeID"]) -> List of measurements of given magnitude
    def appQuery(self, paramsUsed : list, paramsList : list):
        paramsList.reverse()
        self.addSelect("?Measure", "?StationLb", "?Date", "?MagnitudeLbEs", "?MagnitudeLbEn", "?MagnitudeCode", "?Value")
        self.addParam("?Measure", "rdf:type", "ns:Measurement")
        self.addParam("?Measure", "ns:measuredAt", "?Station")
        self.addParam("?Station", "rdfs:label", "?StationLb")
        self.addParam("?Measure", "ns:dateOfMeasure", "?Date")
        self.addParam("?Magnitude", "rdf:type", "ns:Magnitude")
        self.addParam("?Magnitude", "rdfs:label", "?MagnitudeLbEs , ?MagnitudeLbEn")
        self.addFilter("(LANG(?MagnitudeLbEn) = \'en\' && LANG(?MagnitudeLbEs) = \'es\')")
        self.addParam("?Measure", "ns:measuredMagnitude", "?Magnitude")
        self.addParam("?Measure", "ns:measureValue", "?Value")
        self.addParam("?Magnitude", "ns:measureCode", "?MagnitudeCode")
        if paramsUsed[0] == True:
            dictionary = paramsList.pop()
            placeType = dictionary["Place"]
            identifier = dictionary["ID"]
            if placeType == "District":
                self.addParam("?District", "rdf:type", "ns:District")
                self.addParam("?District", "ns:districtID", "\"{}\"^^<http://www.w3.org/2001/XMLSchema#integer>".format(identifier))
                self.addParam("?Station", "ns:inDistrict", "?District")
            elif placeType == "Street":
                self.addParam("?Street", "rdf:type", "ns:Street")
                self.addParam("?Street", "ns:streetID", "\"{}\"^^<http://www.w3.org/2001/XMLSchema#integer>".format(identifier))
                self.addParam("?Station", "ns:inStreet", "?Street")
            elif placeType == "Station":
                self.addParam("?Station", "rdf:type", "ns:Station")
                self.addParam("?Station", "ns:stationCode", "\"{}\"^^<http://www.w3.org/2001/XMLSchema#string>".format(identifier))
            else:
                print("Place " + placeType + " not identified")
                exit()
            # END IF
        # END IF
        if paramsUsed[1] == True:
            date = paramsList.pop()
            splitted = date.split("-")
            if len(splitted) == 1:
                self.addFilter("REGEX (STR(?Date), \"^{}\", \"i\")".format(splitted[0])) 
            elif len(splitted) == 2:
                self.addFilter("REGEX (STR(?Date), \"^{}-{}\", \"i\")".format(splitted[0], splitted[1])) 
            elif len(splitted) == 3:
                self.addFilter("REGEX (STR(?Date), \"^{}-{}-{}\", \"i\")".format(splitted[0], splitted[1], splitted[2])) 
            else:
                print("Date " + date + " wrong formatted (use YYYY-MM-DD)")
                exit()
            # END IF
        # END IF
        if paramsUsed[2] == True:
            magnitude = paramsList.pop()
            self.addParam("?Magnitude", "ns:measureCode", "\"{}\"^^<http://www.w3.org/2001/XMLSchema#string>".format(magnitude))
        # END IF
        self.addOrder("asc(?Date)")
        listResult = self.executeQuery()
        return listResult
    # END FUNCTION


    # cleanQuery () -> ()
    #   Flushes the current query and params in order to prepare a new one
    def cleanQuery(self):
        self.__init__()
    # END FUNCTION


    # [private function] getNamespaces() -> Dictionary
    #   Returns the dictionary with the namespaces used in the current query
    #   example: getNamespaces() -> {"ns":ns, "rdfs":RDFS, "rdf":RDF}
    def getNamespaces(self):
        initNs = ""
        if (self.query.find("ns:") > 0):
            initNs = initNs + "PREFIX ns: <http://www.semanticweb.org/group16/ontologies/air-quality#>\n"""
        if (self.query.find("wiki:") > 0):
            initNs = initNs + "PREFIX wiki: <http://www.wikidata.org/entity/>\n"""
        if (self.query.find("rdf:") > 0):
            initNs =  initNs + "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"""
        if (self.query.find("rdfs:") > 0):
            initNs =  initNs + "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"""
        if (self.query.find("owl:") > 0):
            initNs =  initNs + "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"""
        if (self.query.find("sc:") > 0):
            initNs =  initNs + "PREFIX sc: <https://schema.org/>\n"""
        return initNs
    # END FUNCTION

    # [private function] fixDate(string) -> string
    #   Returns a fixed fitler for date queries
    #   example: fixDate("REGEX (STR(?Date), "^2012-1-30", "i")" -> "REGEX (STR(?Date), "^2012-01-30", "i")"
    def fixDate(self, filter : str):
        idx = filter.find("^")
        if idx > 0:
            substr = filter[idx+1:]
            splitted = substr.split("\"")
            date = splitted[0]
            splitted = date.split("-")
            if len(splitted) > 1 and splitted[1].find("0") < 0 and len(splitted[1]) == 1:
                splitted[1] = "0" + splitted[1]
            if len(splitted) > 2 and splitted[2].find("0") < 0 and len(splitted[2]) == 1:
                splitted[2] = "0" + splitted[2]
            if len(splitted) == 1:
                date = splitted[0]
            elif len(splitted) == 2:
                date = splitted[0] + "-" + splitted[1]
            else:
                date = splitted[0] + "-" + splitted[1] + "-" + splitted[2]
            filter = "REGEX (STR(?Date), \"^{}\", \"i\")".format(date)
        return filter


# END CLASS

# Tests #

# Test method addSelect
def test_addSelect():
    qm = QueryMaker()
    qm.addSelect("?Measure", "?Station")
    expectedResult = "SELECT DISTINCT\n\t?Measure ?Station\nWHERE {\n\t"
    assert qm.query == expectedResult
# END FUNCTION

# Test method addParam
def test_addParam():
    qm = QueryMaker()
    qm.addParam("?Measure", "rdf:type", "ns:Measurement")
    qm.addParam("?Measure", "ns:measuredAt", "?Station")
    expectedResult = [("?Measure", "rdf:type", "ns:Measurement"),
                      ("?Measure", "ns:measuredAt", "?Station")
    ]
    assert qm.paramsList == expectedResult
# END FUNCTION

# Test method addFilter
def test_addFilter():
    qm = QueryMaker()
    qm.addParam("?Measure", "rdf:type", "ns:Measurement")
    qm.addParam("?Measure", "ns:measuredAt", "?Station")
    qm.addParam("?Station", "rdfs:label", "?StLabel")
    qm.addFilter("REGEX (?StLabel, \"Moratalaz\")")
    expectedResult = [("?Measure", "rdf:type", "ns:Measurement"),
                      ("?Measure", "ns:measuredAt", "?Station"),
                      ("?Station", "rdfs:label", "?StLabel"),
                      ("\tFILTER", "REGEX (?StLabel, \"Moratalaz\")")
    ]
    assert qm.paramsList == expectedResult
# END FUNCTION

# Test method addOrder
def test_addOrder():
    qm = QueryMaker()
    qm.addSelect("?Measure ?Station")
    qm.addParam("?Measure", "rdf:type", "ns:Measurement")
    qm.addParam("?Measure", "ns:measuredAt", "?Station")
    qm.addParam("?Station", "rdfs:label", "?StLabel")
    qm.addFilter("REGEX (?StLabel, \"Moratalaz\")")
    qm.addOrder("asc(?Measure)")
    listResult = qm.executeQuery()
    expectedResult = [{u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_12_28079036_2010_5_16'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_12_28079036_2012_2_23'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_1_28079036_2015_3_15'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_6_28079036_2016_9_11'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_7_28079036_2017_7_24'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_8_28079036_2018_12_26'}
    ]
    assert listResult == expectedResult
# END FUNCTION

# Test method executeQuery
def tests_executeQuery():
    qm = QueryMaker()
    qm.addSelect("?Measure", "?Station")
    qm.addParam("?Measure", "rdf:type", "ns:Measurement")
    qm.addParam("?Measure", "ns:measuredAt", "?Station")
    qm.addParam("?Station", "rdfs:label", "?StLabel")
    qm.addFilter("REGEX (?StLabel, \"Moratalaz\")")
    result = qm.executeQuery()
    expectedResult = [{u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_12_28079036_2012_2_23'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_8_28079036_2018_12_26'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_1_28079036_2015_3_15'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_6_28079036_2016_9_11'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_12_28079036_2010_5_16'},
                      {u'Station': u'http://www.semanticweb.org/group16/air-quality/resource/28079036', u'Measure': u'http://www.semanticweb.org/group16/air-quality/resource/36_7_28079036_2017_7_24'}
    ]
    for row in result:
        if not(row in expectedResult):
            assert False
        # END IF
    # END FOR
    assert True
# END FUNCTION

# Test method appQuery
def test_appQuery():
    qm = QueryMaker()
    listResult = qm.appQuery([True, True, True], [{"Place":"Station","ID":"28079057"}, "2020-06-23", "8"])
    expectedResult = [{'MagnitudeLbEs': 'Dióxido de Nitrógeno', 'Measure': 'http://www.semanticweb.org/group16/air-quality/resource/57_8_28079057_2020_6_23',
                       'StationLb': 'Sanchinarro', 'Value': '16',  'MagnitudeLbEn': 'Nitrogen dioxide', 'Date': "2020-06-23"}
    ]
    assert (expectedResult[0].items() == listResult[0].items()) == True
# END FUNCTION

# Test method cleanQuery
def test_cleanQuery():
    qm = QueryMaker()
    qm.addSelect("?Measure", "?Station")
    qm.addParam("?Measure", "rdf:type", "ns:Measurement")
    qm.addParam("?Measure", "ns:measuredAt", "?Station")
    qm.addParam("?Station", "rdfs:label", "?StLabel")
    qm.addFilter("REGEX (?StLabel, \"Moratalaz\")")
    qm.executeQuery()
    qm.cleanQuery()
    assert qm.paramsList == [] and qm.query == ""
# END FUNCTION


# Main entrypoint, used for tests
if __name__ == "__main__":
    test_addSelect()
    print("addSelect method test passed")
    test_addParam()
    print("addParam method test passed")
    test_addFilter()
    print("addFilter method test passed")
    test_addOrder()
    print("addOrder method test passed")
    tests_executeQuery()
    print("executeQuery method tests passed")
    test_appQuery()
    print("appQuery method test passed")
    test_cleanQuery()
    print("cleanQuery method test passed")
# END MAIN
