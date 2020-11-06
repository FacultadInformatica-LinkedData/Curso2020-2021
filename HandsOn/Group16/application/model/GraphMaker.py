#-. GraphMaker class .-#
#.- Retrieves data associated with a Magnitude and a Station/District and graphs it .-#

# Imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.insert(1, './application/model/')
from QueryMaker import QueryMaker

# Class
class GraphMaker:

    # Init function
    def __init__(self):
        self.magnitude = ""
        self.place = ""
        self.isDistrict = None
        self.qm = QueryMaker()
    # END FUNCTION


    # selectMagnitude(string) -> ()
    #   Allows user to choose which magnitude (with its ID) will be retrieved
    #   example: selectMagnitude("1")
    def selectMagnitude(self, magnitude : str):
        self.magnitude = magnitude
    # END FUNCTION


    # selectPlace(boolean, string) -> ()
    #   Allows user to choose which place (whether station or district) will be retrieved
    #   example: selectMagnitude(False, "Pza. de España")
    #   example: selectMagnitude(True, "Carabanchel")
    def selectPlace(self, isDistrict : bool, place : str):
        self.isDistrict = isDistrict
        self.place = place
    # END FUNCTION


    # graphData() -> pd.DataFrame
    #   According to the parameters given in previous functions, graphs the query
    #   returns the dataframe of the queried data
    def graphData(self):
        listResult = self.getQueried()
        for item in listResult:
            item["Value"] = float(item["Value"])
        indexes = self.getIndexes(listResult)
        unit = self.getUnitOfMeasure()
        df = pd.DataFrame(listResult, index=indexes)
        df = df.rename(columns={"MeasureDate":"Date of measure", "Value":unit})
        return df
    # END FUNCTION


    # [private function] getQueried () -> List<Dictionary>
    #   Executes the query described by the parameters passed earlier and returns the
    #   list of dictionaries with its date column normalized to "YYYY-MM-DD"
    #   example: getQueried() -> [{"MeasureDate":"2011-07-26","Value":"11.0"},
    #                             {"MeasureDate":"2012-01-03","Value":"74.0"}
    #                            ]
    def getQueried(self):
        xsd_str = "http://www.w3.org/2001/XMLSchema#string"
        self.qm.addSelect("?MeasureDate ?Value")
        self.qm.addParam("?Measure", "rdf:type", "ns:Measurement")
        self.qm.addParam("?Magnitude", "rdf:type", "ns:Magnitude")
        self.qm.addParam("?Station", "rdf:type", "ns:Station")
        self.qm.addParam("?Magnitude", "ns:measureCode", "\"{}\"^^<{}>".format(self.magnitude, xsd_str))
        self.qm.addParam("?Measure", "ns:measuredMagnitude", "?Magnitude")
        self.qm.addParam("?Measure", "ns:measureValue", "?Value")
        self.qm.addParam("?Measure", "ns:dateOfMeasure", "?MeasureDate")
        if self.isDistrict:
            self.qm.addParam("?District", "rdf:type", "ns:District")
            self.qm.addParam("?District", "rdfs:label", "\"{}\"^^<{}>".format(self.place, xsd_str))
            self.qm.addParam("?Station", "ns:inDistrict", "?District")
        else:
            self.qm.addParam("?Station", "rdfs:label", "\"{}\"^^<{}>".format(self.place, xsd_str))
        # END IF
        self.qm.addParam("?Measure", "ns:measuredAt", "?Station")
        self.qm.addOrder("asc(?MeasureDate)")
        listResult = self.qm.executeQuery()
        self.qm.cleanQuery()
        for item in listResult:
            item["MeasureDate"] = item["MeasureDate"][0:len(item["MeasureDate"])-10]
        return listResult
    # END FUNCTION


    # [private function] getUnitOfMeasure() -> string
    #   Returns the unit of the measurement given the magnitude
    #   example: getUnitOfMeasure() [magnitude="1"] -> "μg/m3"
    #   example: getUnitOfMeasure() [magnitude="2"] -> "mg/m3"
    def getUnitOfMeasure(self):
        magnitudeID = int(self.magnitude)
        if magnitudeID == 1 or (magnitudeID >= 7 and magnitudeID <= 39):
            return "μg/m3"
        else:
            return "mg/m3"
        # END IF
    # END FUNCTION


    # [private function] getIndexes(List<Dictionary>) -> List
    #   Returns the list with all the keys of the dictionaries, normalized to strings
    #   example: getIndexes([{"MD":"2011-07-26",...},{"MD":"2012-01-03",...}]) -> ["2011-07-26", "2012-01-03"]
    def getIndexes(self, listDict):
        listResult = []
        for item in listDict:
            listResult.append(str(item["MeasureDate"]))
        # END FOR
        return listResult
    # END FUNCTION


    # [private function] getLabel() -> string
    #   Returns the label for the graph corresponding to the magnitude and place given
    #   example: getLabel() -> "Fuencarral-El Pardo .·. Sulfur dioxide"
    def getLabel(self):
        magnitudeDictionary = {"1":"Sulfur dioxide", "6":"Carbon monoxide",
        "7":"Nitric oxide", "8":"Nitrogen dioxide", "9":"Particulates <2.5 μm",
        "10":"Particulates <10 μm", "12":"Nitrogen oxide", "14":"Ozone",
        "20":"Toluene", "30":"Benzene", "35":"Ethylbenzene", "42":"Hexane",
        "43":"Methane", "44":"Non-Mehane volatile organic compunds"}
        label = self.place + " .·. " + magnitudeDictionary[self.magnitude] + " measurements"
        return label
    # END FUNCTION


# END CLASS

# Tests #

# Test method selectMagnitude
def test_selectMagnitude():
    gm = GraphMaker()
    gm.selectMagnitude("5")
    assert gm.magnitude == "5"
# END FUNCTION

# Test method selectPlace
def test_selectPlace():
    gm = GraphMaker()
    gm.selectPlace(False, "Arturo Soria")
    assert gm.place == "Arturo Soria" and gm.isDistrict == False
    gm.selectPlace(True, "Barajas")
    assert gm.place == "Barajas" and gm.isDistrict == True
# END FUNCTION

# Test method graphData
def test_graphData():
    gm = GraphMaker()
    gm.selectMagnitude("1")
    gm.selectPlace(True, "Centro")
    df = gm.graphData()
    assert type(df) == type(pd.DataFrame())
# END FUNCTION


# Main entrypoint, used for tests
if __name__ == "__main__":
    test_selectMagnitude()
    print("selectMagnitude method test passed")
    test_selectPlace()
    print("selectPlace method test passed")
    test_graphData()
    print("graphData method test passed")
# END MAIN
