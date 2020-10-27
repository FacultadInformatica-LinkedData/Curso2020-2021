#-. QueryMaker class .-#
#.- Perform SPARQL queries and loads the data graph .-#

# Imports
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.plugins.sparql import prepareQuery

# Namespaces
ns = Namespace("http://www.semanticweb.org/group16/ontologies/air-quality#")
wiki = Namespace("https://www.wikidata.org/wiki/")

# Class
class QueryMaker:

    # Init function
    def __init__(self):
        self.query = ""
        self.paramsList = []
        if not(hasattr(self, "graph")):
            self.graph = Graph()
            self.graph.parse("/home/pablo/Descargas/a.ttl", format="nt")
        # END IF
    # END FUNCTION


    # addSelect(*string) -> ()
    #   Allows user to choose which parameters will be retrieved
    #   example: addSelect("?Measure", "?Station")
    def addSelect(self, *paramsToSelect):
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
    def addParam(self, s, p, o):
        self.paramsList.append((s, p, o))
    # END FUNCTION


    # addFilter(string) -> ()
    #   Inserts into the query a filtering sentence
    #   example: addFilter("REGEX (?StLabel, \"Moratalaz\")")
    def addFilter(self, filter):
        self.paramsList.append(("\tFILTER", filter))
    # END FUNCTION


    # [private function] getNamespaces() -> Dictionary
    #   Returns the dictionary with the namespaces used in the current query
    #   example: getNamespaces() -> {"ns":ns, "rdfs":RDFS, "rdf":RDF}
    def getNamespaces(self):
        initNs = {}
        if (self.query.find("ns:") > 0):
            initNs["ns"] = ns
        if (self.query.find("wiki:") > 0):
            initNs["wiki"] = wiki
        if (self.query.find("rdf:") > 0):
            initNs["rdf"] = RDF
        if (self.query.find("rdfs:") > 0):
            initNs["rdfs"] = RDFS
        if (self.query.find("owl:") > 0):
            initNs["owl"] = OWL
        return initNs
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
        initNs = self.getNamespaces()
        q = prepareQuery(self.query, initNs)
        result = self.graph.query(q)
        listResult = []
        for row in result:
            rowDict = row.asdict()
            for key in rowDict.keys():
                rowDict[key] = rowDict[key].toPython()
            # END FOR
            listResult.append(rowDict)
        # END FOR
        return listResult
    # END FUNCTION

    # cleanQuery () -> ()
    #   Flushes the current query and params in order to prepare a new one
    def cleanQuery(self):
        self.__init__()
    # END FUNCTION


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
    tests_executeQuery()
    print("executeQuery method tests passed")
    test_cleanQuery()
    print("cleanQuery method test passed")
# END MAIN
