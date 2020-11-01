#-. GraphMaker class .-#
#.- Retrieves data and graphs it? .-#

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

    #̣ --
    def selectMagnitude(self, magnitude : str):
        self.magnitude = magnitude
    # END FUNCTION

    # --
    def selectPlace(self, isDistrict : bool, place : str):
        self.isDistrict = isDistrict
        self.place = place
    # END FUNCTION

    # --
    def graphData(self):
        listResult = self.getQueried()
        unit = self.getUnitOfMeasure()
        df = pd.DataFrame(listResult)
        plt.show()
    # END FUNCTION

    # [private function]
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
            item["MeasureDate"] = item["MeasureDate"].date()
        return listResult
    # END FUNCTION

    # [private function]
    def getUnitOfMeasure(self):
        magnitudeID = int(self.magnitude)
        if magnitudeID == 1 or (magnitudeID >= 7 and magnitudeID <= 39):
            return "μg/m3"
        else:
            return "mg/m3"
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
    gm.selectMagnitude("7")
    gm.selectPlace(True, "Fuencarral-El Pardo")
    gm.graphData()
    # assert sth
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