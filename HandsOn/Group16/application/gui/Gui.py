#-. Gui class .-#
#.- Displays the user interface of the application .-#

# Imports
import os, sys
import qtmodern.styles
import qtmodern.windows
import collections
import urllib.request

sys.path.insert(1, './application/model/')
from QueryMaker import QueryMaker
from GraphMaker import GraphMaker

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QFile, QTextStream, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QVBoxLayout, QTextEdit, QLineEdit, QDialog, QStyleFactory, QComboBox, QCheckBox, QSizePolicy, QGridLayout, QApplication, QMainWindow, QStackedWidget, QMessageBox, QWidget, QHBoxLayout, QPushButton, QLabel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import random

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(1000, 200, 700, 500)
        self.setFixedSize(700, 500)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Station/district to show
        self.station_toShow = ""
        self.stName_toShow = ""
        self.district_toShow = ""

        # Query params
        self.check_list = []
        self.query_list = []

        # Main
        self.main_widget = MainWidget(self)
        self.main_widget.ds_button.clicked.connect(self.toDS)
        self.main_widget.mg_button.clicked.connect(self.toMG)
        self.main_widget.map_button.clicked.connect(self.toMaps)
        self.central_widget.addWidget(self.main_widget)
        # Data properties, object properties, class
        self.mt_widget = MTextWidget(self)
        self.mt_widget.back_button.clicked.connect(self.toModel)
        self.central_widget.addWidget(self.mt_widget)
        # Data searching
        self.ds_widget = DSWidget(self)
        self.ds_widget.back_button.clicked.connect(self.toMain)
        self.ds_widget.ms_button.clicked.connect(self.toMS)
        self.ds_widget.model_button.clicked.connect(self.toModel)
        self.central_widget.addWidget(self.ds_widget)
        # Measurements
        self.ms_widget = MSWidget(self)
        self.ms_widget.query_button.clicked.connect(self.toQuery)
        self.ms_widget.back_button.clicked.connect(self.toDS)
        self.central_widget.addWidget(self.ms_widget)
        # Model
        self.model_widget = ModelWidget(self)
        self.model_widget.dp_button.clicked.connect(lambda: self.toMT("dp"))
        self.model_widget.obj_button.clicked.connect(lambda: self.toMT("obj"))
        self.model_widget.cls_button.clicked.connect(lambda: self.toMT("cls"))
        self.model_widget.dg_button.clicked.connect(self.toDG)
        self.model_widget.back_button.clicked.connect(self.toDS)
        self.central_widget.addWidget(self.model_widget)
        # Maps
        self.maps_widget = MapsWidget(self)
        self.maps_widget.back_button.clicked.connect(self.toMain)
        self.maps_widget.st_button.clicked.connect(self.toStations)
        self.maps_widget.dist_button.clicked.connect(self.toDistricts)
        self.central_widget.addWidget(self.maps_widget)
        # Stations
        self.st_widget = StationsWidget(self)
        self.st_widget.back_button.clicked.connect(self.toMaps)
        self.st_widget.more_button.clicked.connect(self.toStInfo)
        self.central_widget.addWidget(self.st_widget)
        # Districts
        self.dts_widget = DistrictsWidget(self)
        self.dts_widget.back_button.clicked.connect(self.toMaps)
        self.dts_widget.more_button.clicked.connect(self.toDtInfo)
        self.central_widget.addWidget(self.dts_widget)
        # Magnitudes
        self.mg_widget = MGWidget(self)
        self.mg_widget.back_button.clicked.connect(self.toMain)
        self.central_widget.addWidget(self.mg_widget)
        

        # Diagram
        #self.dg_widget = DGWidget(self)
        #self.dg_widget.back_button.clicked.connect(self.toModel)
        #self.central_widget.addWidget(self.dg_widget)
    # END FUNCTION
        

    def toDS(self):
        self.central_widget.setCurrentWidget(self.ds_widget)
    # END FUNCTION

    def toMain(self):
        self.central_widget.setCurrentWidget(self.main_widget)
    # END FUNCTION

    def toMS(self):
        self.central_widget.setCurrentWidget(self.ms_widget)
    # END FUNCTION
    
    def toModel(self):
        self.central_widget.setCurrentWidget(self.model_widget)
    # END FUNCTION

    def toMaps(self):
        self.central_widget.setCurrentWidget(self.maps_widget)
    # END FUNCTION

    def toStations(self):
        self.central_widget.setCurrentWidget(self.st_widget)
    # END FUNCTION

    def toDistricts(self):
        self.central_widget.setCurrentWidget(self.dts_widget)
    # END FUNCTION

    def toMG(self):
        self.central_widget.setCurrentWidget(self.mg_widget)
    # END FUNCTION

    def toDG(self):
        #self.central_widget.setCurrentWidget(self.dg_widget)

        self.dg_window = DGWindow()
        self.dg_window.show()
    # END FUNCTION

    def toQuery(self):
        self.check_list = self.ms_widget.changeMode()
        self.query_list = self.ms_widget.retrieveCombo()
        # Query info
        self.query_widget = QueryInfo(self)
        self.query_widget.back_button.clicked.connect(self.toMS)
        self.central_widget.addWidget(self.query_widget)
        self.central_widget.setCurrentWidget(self.query_widget)

    def toMT(self, type):
        self.mt_widget.changeText(type)
        self.central_widget.setCurrentWidget(self.mt_widget)
    # END FUNCTION

    def toStInfo(self):
        self.station_toShow = self.st_widget.station_tsAux
        self.district_toShow = self.st_widget.district_tsAux
        self.stName_toShow = self.st_widget.stName_tsAux
        # Station info
        self.stinfo_widget = StationInfoWidget(self)
        self.stinfo_widget.back_button.clicked.connect(self.toStations)
        self.central_widget.addWidget(self.stinfo_widget)
        ## NOT NECESSARY ##
        if self.station_toShow != "Empty" :
            self.central_widget.setCurrentWidget(self.stinfo_widget)
    # END FUNCTION

    def toDtInfo(self):
        self.district_toShow = self.dts_widget.district_tsAux
        # District info
        self.dtinfo_widget = DistrictInfoWidget(self)
        self.dtinfo_widget.back_button.clicked.connect(self.toDistricts)
        self.central_widget.addWidget(self.dtinfo_widget)
        self.central_widget.setCurrentWidget(self.dtinfo_widget)

# END CLASS


class MainWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Map button
        self.map_button = QPushButton(self)
        self.map_button.setGeometry(85, 45, 250, 250)
        self.map_button.setIcon(QIcon(os.path.join(ws_path, "../resources/maps.png")))
        self.map_button.setIconSize(QSize(200, 200))
        # Map label
        self.map_label = QLabel('MAPS', self)
        self.map_label.setGeometry(196, 290, 100, 30)
        # Data searching label
        self.ds_label = QLabel('DATA SEARCHING', self)
        self.ds_label.setGeometry(446, 290, 100, 30)
        # Data searching button
        self.ds_button = QPushButton(self)
        self.ds_button.setGeometry(365, 45, 250, 250)
        self.ds_button.setIcon(QIcon(os.path.join(ws_path, "../resources/lupa.png")))
        self.ds_button.setIconSize(QSize(200, 200))
        # Magnitudes button
        self.mg_button = QPushButton(self)
        self.mg_button.setGeometry(85, 320, 530, 90)
        self.mg_button.setIcon(QIcon(os.path.join(ws_path, "../resources/pollution.png")))
        self.mg_button.setIconSize(QSize(70, 70))
        # Magnitudes label
        self.mg_label = QLabel('MAGNITUDES', self)
        self.mg_label.setGeometry(320, 405, 100, 30)
    # END FUNCTION
# END CLASS


class DSWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Measurement button
        self.ms_button = QPushButton(self)
        self.ms_button.setGeometry(50, 90, 280, 280)
        self.ms_button.setIcon(QIcon(os.path.join(ws_path, "../resources/measure.png")))
        self.ms_button.setIconSize(QSize(300, 300))
        # Measurement label
        self.ms_label = QLabel('MEASUREMENTS', self)
        self.ms_label.setGeometry(150, 367, 100, 30)
        # Model button
        self.model_button = QPushButton(self)
        self.model_button.setGeometry(365, 90, 280, 280)
        self.model_button.setIcon(QIcon(os.path.join(ws_path, "../resources/model.png")))
        self.model_button.setIconSize(QSize(200, 200))
        # Model label
        self.ms_label = QLabel('MODEL', self)
        self.ms_label.setGeometry(490, 367, 100, 30)
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
# END CLASS


class MSWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        self.setGeometry(0, 0, 120, 120)

        self.dist_dict = {}
        self.stat_dict = {}
        self.str_dict = {}

        self.check_list = [False, False, False]
        self.params_list = []

        self.generateDicts()

        ## LOCATION ##
        # Location check box
        self.location_check = QCheckBox("LOCATION", self)
        self.location_check.stateChanged.connect(self.checkLocation)
        self.location_check.setGeometry(30, 60, 200, 50)
        # Place combo box
        self.location_combo1 = QComboBox(self)
        self.location_combo1.setGeometry(250, 80, 100, 30)
        self.location_combo1.setEnabled(False)
        self.location_combo1.addItems(["Select Place"] + self.getPlaces())
        # Update location_combo2 when a new item is selected
        self.location_combo1.currentIndexChanged.connect(self.selectionchange1)

        # Station/Street/District combo box
        self.location_combo2 = QComboBox(self)
        self.location_combo2.setGeometry(350, 80, 100, 30)
        self.location_combo2.setEnabled(False)
        self.location_combo2.addItems([])

        ## DATE/RANGE ##
        # Date check box
        self.date_check = QCheckBox("DATE", self)
        self.date_check.stateChanged.connect(self.checkDate)
        self.date_check.setGeometry(30, 120, 200, 50)
        # Date combo box
        self.date_combo = QComboBox(self)
        self.date_combo.setGeometry(250, 140, 100, 30)
        self.date_combo.setEnabled(False)
        years = list(range(2010,2021))
        years_text = []
        for i in range(len(years)):
            years_text.append(str(years[i]))
        # END
        self.date_combo.addItems(years_text)

        self.date1_combo = QComboBox(self)
        self.date1_combo.setGeometry(350, 140, 100, 30)
        self.date1_combo.setEnabled(False)
        months = list(range(1,13))
        months_text = ["Empty"]
        for i in range(len(months)):
            months_text.append(str(months[i]))
        # END
        self.date1_combo.addItems(months_text)

        self.date2_combo = QComboBox(self)
        self.date2_combo.setGeometry(450, 140, 100, 30)
        self.date2_combo.setEnabled(False)
        days = list(range(1,32))
        days_text = ["Empty"]
        for i in range(len(days)):
            days_text.append(str(days[i]))
        # END
        self.date2_combo.addItems(days_text)

        ## MAGNITUDE ##
        # Magnitude check box
        self.mg_check = QCheckBox("MAGNITUDE", self)
        self.mg_check.stateChanged.connect(self.checkMagnitude)
        self.mg_check.setGeometry(30, 180, 200, 50)
        # Magnitude combo box
        self.mg_combo = QComboBox(self)
        self.mg_combo.setGeometry(250, 200, 100, 30)
        self.mg_combo.setEnabled(False)
        self.mg_combo.addItems(["1- SO2", "6- CO", "7- NO", "8- NO2", 
                                   "9- PM2.5", "10- PM10", "12- NOx", "14- O3", 
                                   "20- TOL", "30- BEN", "35- EBE", "42- TCH", 
                                   "43- CH4", "44- NMHC"])
            

        # Query button
        self.query_button = QPushButton('QUERY', self)
        self.query_button.setGeometry(325, 400, 50, 30)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION

    def locationDropdown(self):
        stationsDicts = StationsWidget().getStations()
        statList=[]
        for d in stationsDicts:
            statList.append(d.get('StLabel'))
        return statList
    # END FUNCTION

    def getPlaces(self):
        qm = QueryMaker()
        qm.addSelect("?cl")
        qm.addParam("?s", "rdfs:subClassOf", "sc:Place")
        qm.addParam("?s", "rdf:type", "?cl")
        queryResult = qm.executeQuery()
        placeList=[]
        for d in queryResult:
            placeList.append(d.get('cl').split("#",1)[1])
        return placeList
    # END FUNCTION

    def getLocations(self, selected):
        if selected == "Select Place":
            return
        qm = QueryMaker()
        qm.addSelect("?Label")
        qm.addParam("?s", "rdf:type", "ns:"+selected)
        qm.addParam("?s", "rdfs:label", "?Label")
        qm.addOrder("asc(?Label)")
        queryResult = qm.executeQuery()
        locationList = []
        for d in queryResult:
            locationList.append(d.get('Label'))
        return locationList
    # END FUNCTION
    
    # Update location_combo2 when a new item is selected
    def selectionchange1(self,i):
        self.location_combo2.clear()
        ls = self.getLocations(self.location_combo1.currentText())
        if ls is not None:
            self.location_combo2.addItems(ls)
    # END FUNCTION

    def checkLocation(self,state):
        if QtCore.Qt.Checked == state:
            self.location_combo1.setEnabled(True)
            self.location_combo2.setEnabled(True)
        else:
            self.location_combo1.setEnabled(False)
            self.location_combo2.setEnabled(False)
    # END FUNCTION

    def checkDate(self, state):
        if QtCore.Qt.Checked == state:
            self.date_combo.setEnabled(True)
            self.date1_combo.setEnabled(True)
            self.date2_combo.setEnabled(True)
        else:
            self.date_combo.setEnabled(False)
            self.date1_combo.setEnabled(False)
            self.date2_combo.setEnabled(False)
    # END FUNCTION

    def checkMagnitude(self, state):
        if QtCore.Qt.Checked == state:
            self.mg_combo.setEnabled(True)
        else:
            self.mg_combo.setEnabled(False)
    # END FUNCTION

    def generateDicts(self):
        qm = QueryMaker()

        # Stations
        qm.addSelect("?StLabel ?StCode")
        qm.addParam("?St", "rdf:type", "ns:Station")
        qm.addParam("?St", "rdfs:label", "?StLabel")
        qm.addParam("?St", "ns:stationCode", "?StCode")
        listResult = qm.executeQuery()
        qm.cleanQuery()
        for stationCode in listResult:
            self.stat_dict[stationCode["StLabel"]] = stationCode["StCode"]
        # END FOR

        # Streets
        qm.addSelect("?StLabel ?StCode")
        qm.addParam("?St", "rdf:type", "ns:Street")
        qm.addParam("?St", "rdfs:label", "?StLabel")
        qm.addParam("?St", "ns:streetID", "?StCode")
        listResult = qm.executeQuery()
        qm.cleanQuery()
        for streetCode in listResult:
            self.str_dict[streetCode["StLabel"]] = streetCode["StCode"]
        # END FOR
        
        # Districts
        qm.addSelect("?StLabel ?StCode")
        qm.addParam("?St", "rdf:type", "ns:District")
        qm.addParam("?St", "rdfs:label", "?StLabel")
        qm.addParam("?St", "ns:districtID", "?StCode")
        listResult = qm.executeQuery()
        qm.cleanQuery()
        for streetCode in listResult:
            self.dist_dict[streetCode["StLabel"]] = streetCode["StCode"]
        # END FOR
    # END FUNCTION

    def changeMode(self):
        self.check_list[0] = self.location_check.isChecked()
        self.check_list[1] = self.date_check.isChecked()
        self.check_list[2] = self.mg_check.isChecked()
        return self.check_list

    def retrieveCombo(self):
        result = []
        if self.check_list[0]:
            dictt = {}
            place = self.location_combo1.currentText()
            sitio = self.location_combo2.currentText()
            if place == "District":
                id = self.dist_dict[sitio]
            elif place == "Street":
                id = self.str_dict[sitio]
            else:
                id = self.stat_dict[sitio]
            dictt["Place"] = place
            dictt["ID"] = id
            result.append(dictt)
        if self.check_list[1]:
            ls = self.date_combo.currentText()
            if self.date1_combo.currentText() != "Empty":
                ls = ls + "-" + self.date1_combo.currentText()
                if self.date2_combo.currentText() != "Empty":
                    ls = ls + "-" + self.date2_combo.currentText()
            result.append(ls)
        if self.check_list[2]:
            mg = self.mg_combo.currentText()
            result.append(mg.split("-")[0])
        return result

            

# END CLASS
    

class ModelWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Data properties button
        self.dp_button = QPushButton(self)
        self.dp_button.setGeometry(120, 40, 190, 190)
        self.dp_button.setIcon(QIcon(os.path.join(ws_path, "../resources/dataprop.png")))
        self.dp_button.setIconSize(QSize(150, 150))
        # Data properties label
        self.dp_label = QLabel('DATA PROPERTIES', self)
        self.dp_label.setGeometry(185, 225, 100, 30)
        # Object properties properties button
        self.obj_button = QPushButton(self)
        self.obj_button.setGeometry(370, 40, 190, 190)
        self.obj_button.setIcon(QIcon(os.path.join(ws_path, "../resources/objectprop.png")))
        self.obj_button.setIconSize(QSize(150, 150))
        # Object properties label
        self.obj_label = QLabel('OBJECT PROPERTIES', self)
        self.obj_label.setGeometry(435, 225, 100, 30)
        # Classes button
        self.cls_button = QPushButton(self)
        self.cls_button.setGeometry(120, 260, 190, 190)
        self.cls_button.setIcon(QIcon(os.path.join(ws_path, "../resources/class.png")))
        self.cls_button.setIconSize(QSize(150, 150))
        # Classes label
        self.cls_label = QLabel('CLASSES', self)
        self.cls_label.setGeometry(194, 445, 100, 30)
        # Diagram button
        self.dg_button = QPushButton(self)
        self.dg_button.setGeometry(370, 260, 190, 190)
        self.dg_button.setIcon(QIcon(os.path.join(ws_path, "../resources/diagram.svg")))
        self.dg_button.setIconSize(QSize(150, 150))
        # Diagram label
        self.dg_label = QLabel('DIAGRAM', self)
        self.dg_label.setGeometry(440, 445, 100, 30)
        
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
# END CLASS


class MapsWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Stations button
        self.st_button = QPushButton(self)
        self.st_button.setGeometry(50, 90, 280, 280)
        self.st_button.setIcon(QIcon(os.path.join(ws_path, "../resources/stations.png")))
        self.st_button.setIconSize(QSize(200, 200))
        # Stations label
        self.st_label = QLabel('STATIONS', self)
        self.st_label.setGeometry(160, 367, 100, 30)
        # Districts button
        self.dist_button = QPushButton(self)
        self.dist_button.setGeometry(365, 90, 280, 280)
        self.dist_button.setIcon(QIcon(os.path.join(ws_path, "../resources/madrid.png")))
        self.dist_button.setIconSize(QSize(200, 200))
        # Districts label
        self.dist_label = QLabel('DISTRICTS', self)
        self.dist_label.setGeometry(480, 367, 100, 30)
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
# END CLASS

"""
class DistrictsInfoWidget(QWidget):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        #ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)       
        # Station info label
        self.st_label = QLabel("DISTRICT:  " + parent.district_toShow + ", " + parent.stName_toShow, self)
        self.st_label.setGeometry(60, 60, 700, 30)

        # URI label
        self.uri_label = QLabel("URI:  ", self)
        self.uri_label.setGeometry(170, 5, 500, 30)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
# END CLASS
"""

class DistrictsWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.district_tsAux = "Empty"
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.img_label = QLabel(self)
        img = QPixmap(os.path.join(ws_path, "../resources/districts/distritos.png"))       
        self.img_label.setPixmap(img)

        listDt = self.getDistricts()

        self.sel_combo = QComboBox(self)
        self.sel_combo.setGeometry(500, 230, 100, 30)

        districts = self.getDistricts()
        # Select district combo box
        self.sel_combo = QComboBox(self)
        self.sel_combo.setGeometry(500, 230, 100, 30)

        items = ["Empty"]
        for i in range(len(districts)):
            items.append(districts[i]["DtLabel"])
        # END
        self.sel_combo.addItems(items)

        # Select station label
        self.sel_label = QLabel('SELECT DISTRICT\n   ON BOX', self)
        self.sel_label.setGeometry(510, 200, 100, 30)
        # Select station button
        self.sel_button = QPushButton('SELECT', self)
        self.sel_button.setGeometry(610, 230, 50, 30)
        self.sel_button.pressed.connect(self.selCombo)

        # More info button
        self.more_button = QPushButton('MORE INFO', self)
        self.more_button.setGeometry(500, 270, 100, 30)
        self.more_button.setEnabled(False)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)

    # Recuperar los datos de los distritos por medio de los datos rdf
    def getDistricts(self):
        qm = QueryMaker()
        qm.addSelect("?DtLabel ?dtID")
        qm.addParam("?District", "rdf:type", "ns:District")
        qm.addParam("?District", "rdfs:label", "?DtLabel")
        qm.addOrder("asc(?DtLabel)")
        listStations = qm.executeQuery()
        return listStations
    # END FUNCTION

    def selCombo(self):
        ws_path = os.path.dirname(os.path.abspath(__file__))
        district = self.sel_combo.currentText()
        if district == "Empty":
            self.more_button.setEnabled(False)
            self.img_label.setPixmap(QPixmap(os.path.join(ws_path, "../resources/districts/distritos.png")))
        else:
            self.district_tsAux = district
            path = "../resources/districts/" + district + ".png"
            self.img_label.setPixmap(QPixmap(os.path.join(ws_path, path)))
            self.more_button.setEnabled(True)
    # END FUNCTION
# END CLASS

class StationsWidget(QWidget):
    def __init__(self, parent=None):
        self.station_tsAux = "Empty"
        self.district_tsAux = "Empty"
        self.stName_tsAux = "Empty"

        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        img_label = QLabel(self)
        img = QPixmap(os.path.join(ws_path, "../resources/madrid.png"))
        #img = img.scaledToHeight(480)        
        img_label.setPixmap(img)

        # Button 28079004
        self.b_9004 = QPushButton(self)
        self.b_9004.setStyleSheet("background-color:red")
        self.b_9004.setGeometry(172, 297, 10, 10)
        # Button 28079008
        self.b_9008 = QPushButton(self)
        self.b_9008.setStyleSheet("background-color:red")
        self.b_9008.setGeometry(208, 305, 10, 10)
        # Button 28079011
        self.b_9011 = QPushButton(self)
        self.b_9011.setStyleSheet("background-color:red")
        self.b_9011.setGeometry(216, 260, 10, 10)
        # Button 28079016
        self.b_9016 = QPushButton(self)
        self.b_9016.setStyleSheet("background-color:red")
        self.b_9016.setGeometry(253, 283, 10, 10)
        # Button 28079017
        self.b_9017 = QPushButton(self)
        self.b_9017.setStyleSheet("background-color:red")
        self.b_9017.setGeometry(178, 400, 10, 10)
        # Button 28079018
        self.b_9018 = QPushButton(self)
        self.b_9018.setStyleSheet("background-color:red")
        self.b_9018.setGeometry(167, 345, 10, 10)
        # Button 28079024
        self.b_9024 = QPushButton(self)
        self.b_9024.setStyleSheet("background-color:red")
        self.b_9024.setGeometry(140, 302, 10, 10)
        # Button 28079027
        self.b_9027 = QPushButton(self)
        self.b_9027.setStyleSheet("background-color:red")
        self.b_9027.setGeometry(332, 220, 10, 10)
        # Button 28079035
        self.b_9035 = QPushButton(self)
        self.b_9035.setStyleSheet("background-color:red")
        self.b_9035.setGeometry(185, 298, 10, 10)
        # Button 28079036
        self.b_9036 = QPushButton(self)
        self.b_9036.setStyleSheet("background-color:red")
        self.b_9036.setGeometry(250, 330, 10, 10)
        # Button 28079038
        self.b_9038 = QPushButton(self)
        self.b_9038.setStyleSheet("background-color:red")
        self.b_9038.setGeometry(180, 278, 10, 10)
        # Button 28079039
        self.b_9039 = QPushButton(self)
        self.b_9039.setStyleSheet("background-color:red")
        self.b_9039.setGeometry(210, 222, 10, 10)
        # Button 28079040
        self.b_9040 = QPushButton(self)
        self.b_9040.setStyleSheet("background-color:red")
        self.b_9040.setGeometry(245, 360, 10, 10)
        # Button 28079047
        self.b_9047 = QPushButton(self)
        self.b_9047.setStyleSheet("background-color:red")
        self.b_9047.setGeometry(201, 330, 10, 10)
        # Button 28079048
        self.b_9048 = QPushButton(self)
        self.b_9048.setStyleSheet("background-color:red")
        self.b_9048.setGeometry(210, 280, 10, 10)
        # Button 28079049
        self.b_9049 = QPushButton(self)
        self.b_9049.setStyleSheet("background-color:red")
        self.b_9049.setGeometry(218, 305, 10, 10)
        # Button 28079050
        self.b_9050 = QPushButton(self)
        self.b_9050.setStyleSheet("background-color:red")
        self.b_9050.setGeometry(215, 238, 10, 10)
        # Button 28079054
        self.b_9054 = QPushButton(self)
        self.b_9054.setStyleSheet("background-color:red")
        self.b_9054.setGeometry(270, 390, 10, 10)
        # Button 28079055
        self.b_9055 = QPushButton(self)
        self.b_9055.setStyleSheet("background-color:red")
        self.b_9055.setGeometry(325, 220, 10, 10)
        # Button 28079056
        self.b_9056 = QPushButton(self)
        self.b_9056.setStyleSheet("background-color:red")
        self.b_9056.setGeometry(174, 363, 10, 10)
        # Button 28079057
        self.b_9057 = QPushButton(self)
        self.b_9057.setStyleSheet("background-color:red")
        self.b_9057.setGeometry(246, 222, 10, 10)
        # Button 28079058
        self.b_9058 = QPushButton(self)
        self.b_9058.setStyleSheet("background-color:red")
        self.b_9058.setGeometry(145, 192, 10, 10)
        # Button 28079059
        self.b_9059 = QPushButton(self)
        self.b_9059.setStyleSheet("background-color:red")
        self.b_9059.setGeometry(305, 260, 10, 10)
        # Button 28079060
        self.b_9060 = QPushButton(self)
        self.b_9060.setStyleSheet("background-color:red")
        self.b_9060.setGeometry(200, 222, 10, 10)

        # Hashmap relating stations id with his name
        listStations = self.getStations()
        self.stations = {self.b_9004:[listStations[0]["StLabel"], listStations[0]["StationCode"], listStations[0]["DtLabel"]], 
                         self.b_9008:[listStations[1]["StLabel"], listStations[1]["StationCode"], listStations[1]["DtLabel"]], 
                         self.b_9011:[listStations[2]["StLabel"], listStations[2]["StationCode"], listStations[2]["DtLabel"]],
                         self.b_9016:[listStations[3]["StLabel"], listStations[3]["StationCode"], listStations[3]["DtLabel"]],
                         self.b_9017:[listStations[4]["StLabel"], listStations[4]["StationCode"], listStations[4]["DtLabel"]],
                         self.b_9018:[listStations[5]["StLabel"], listStations[5]["StationCode"], listStations[5]["DtLabel"]],
                         self.b_9024:[listStations[6]["StLabel"], listStations[6]["StationCode"], listStations[6]["DtLabel"]],
                         self.b_9027:[listStations[7]["StLabel"], listStations[7]["StationCode"], listStations[7]["DtLabel"]],
                         self.b_9035:[listStations[8]["StLabel"], listStations[8]["StationCode"], listStations[8]["DtLabel"]],
                         self.b_9036:[listStations[9]["StLabel"], listStations[9]["StationCode"], listStations[9]["DtLabel"]],
                         self.b_9038:[listStations[10]["StLabel"], listStations[10]["StationCode"], listStations[10]["DtLabel"]],
                         self.b_9039:[listStations[11]["StLabel"], listStations[11]["StationCode"], listStations[11]["DtLabel"]],
                         self.b_9040:[listStations[12]["StLabel"], listStations[12]["StationCode"], listStations[12]["DtLabel"]],
                         self.b_9047:[listStations[13]["StLabel"], listStations[13]["StationCode"], listStations[13]["DtLabel"]],
                         self.b_9048:[listStations[14]["StLabel"], listStations[14]["StationCode"], listStations[14]["DtLabel"]],
                         self.b_9049:[listStations[15]["StLabel"], listStations[15]["StationCode"], listStations[15]["DtLabel"]],
                         self.b_9050:[listStations[16]["StLabel"], listStations[16]["StationCode"], listStations[16]["DtLabel"]],
                         self.b_9054:[listStations[17]["StLabel"], listStations[17]["StationCode"], listStations[17]["DtLabel"]],
                         self.b_9055:[listStations[18]["StLabel"], listStations[18]["StationCode"], listStations[18]["DtLabel"]],
                         self.b_9056:[listStations[19]["StLabel"], listStations[19]["StationCode"], listStations[19]["DtLabel"]],
                         self.b_9057:[listStations[20]["StLabel"], listStations[20]["StationCode"], listStations[20]["DtLabel"]],
                         self.b_9058:[listStations[21]["StLabel"], listStations[21]["StationCode"], listStations[21]["DtLabel"]],
                         self.b_9059:[listStations[22]["StLabel"], listStations[22]["StationCode"], listStations[22]["DtLabel"]],
                         self.b_9060:[listStations[23]["StLabel"], listStations[23]["StationCode"], listStations[23]["DtLabel"]]
                        }

        # Select station combo box
        self.sel_combo = QComboBox(self)
        self.sel_combo.setGeometry(500, 230, 100, 30)
        items = ["Empty"]
        for i in range(len(listStations)):
            items.append(listStations[i]["StLabel"])
        # END
        self.sel_combo.addItems(items)

        
        # arreglar !!! TODO
        self.b_9004.pressed.connect(lambda: self.selMap(listStations[0]["StationCode"]))
        self.b_9008.pressed.connect(lambda: self.selMap(listStations[1]["StationCode"]))
        self.b_9011.pressed.connect(lambda: self.selMap(listStations[2]["StationCode"]))
        self.b_9016.pressed.connect(lambda: self.selMap(listStations[3]["StationCode"]))
        self.b_9017.pressed.connect(lambda: self.selMap(listStations[4]["StationCode"]))
        self.b_9018.pressed.connect(lambda: self.selMap(listStations[5]["StationCode"]))
        self.b_9024.pressed.connect(lambda: self.selMap(listStations[6]["StationCode"]))
        self.b_9027.pressed.connect(lambda: self.selMap(listStations[7]["StationCode"]))
        self.b_9035.pressed.connect(lambda: self.selMap(listStations[8]["StationCode"]))
        self.b_9036.pressed.connect(lambda: self.selMap(listStations[9]["StationCode"]))
        self.b_9038.pressed.connect(lambda: self.selMap(listStations[10]["StationCode"]))
        self.b_9039.pressed.connect(lambda: self.selMap(listStations[11]["StationCode"]))
        self.b_9040.pressed.connect(lambda: self.selMap(listStations[12]["StationCode"]))
        self.b_9047.pressed.connect(lambda: self.selMap(listStations[13]["StationCode"]))
        self.b_9048.pressed.connect(lambda: self.selMap(listStations[14]["StationCode"]))
        self.b_9049.pressed.connect(lambda: self.selMap(listStations[15]["StationCode"]))
        self.b_9050.pressed.connect(lambda: self.selMap(listStations[16]["StationCode"]))
        self.b_9054.pressed.connect(lambda: self.selMap(listStations[17]["StationCode"]))
        self.b_9055.pressed.connect(lambda: self.selMap(listStations[18]["StationCode"]))
        self.b_9056.pressed.connect(lambda: self.selMap(listStations[19]["StationCode"]))
        self.b_9057.pressed.connect(lambda: self.selMap(listStations[20]["StationCode"]))
        self.b_9058.pressed.connect(lambda: self.selMap(listStations[21]["StationCode"]))
        self.b_9059.pressed.connect(lambda: self.selMap(listStations[22]["StationCode"]))
        self.b_9060.pressed.connect(lambda: self.selMap(listStations[23]["StationCode"]))

        # Select station label
        self.sel_label = QLabel('SELECT STATION\n   ON MAP/BOX', self)
        self.sel_label.setGeometry(510, 200, 100, 30)
        # Select station button
        self.sel_button = QPushButton('SELECT', self)
        self.sel_button.setGeometry(610, 230, 50, 30)
        self.sel_button.pressed.connect(self.selCombo)

        # More info button
        self.more_button = QPushButton('MORE INFO', self)
        self.more_button.setGeometry(500, 270, 100, 30)
        self.more_button.setEnabled(False)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION


    # Change color of a point in the map when selected in combo box
    def selCombo(self):
        station = self.sel_combo.currentText()
        for id, st in self.stations.items():
            id.setStyleSheet("background-color:red")
            if st[0] == station :
                self.station_tsAux = st[1]
                self.district_tsAux = st[2]
                self.stName_tsAux = st[0]
                self.more_button.setEnabled(True)
                id.setStyleSheet("background-color:green")
            elif station == "Empty" :
                self.more_button.setEnabled(False)
    # END FUNCTION

    
    # Change color of a point in the map when selected in map
    def selMap(self, station):
        for id, st in self.stations.items():
            id.setStyleSheet("background-color:red")
            if st[1] == station :
                id.setStyleSheet("background-color:green")
                self.sel_combo.setCurrentText(st[0])
                self.sel_button.click()
    # END FUNCTION


    # Recuperar los datos de las estaciones por medio de los datos rdf
    def getStations(self):
        qm = QueryMaker()
        qm.addSelect("?StLabel ?StationCode ?DtLabel")
        qm.addParam("?St", "rdf:type", "ns:Station")
        qm.addParam("?St", "rdfs:label", "?StLabel")
        qm.addParam("?St", "ns:stationCode", "?StationCode")
        qm.addParam("?District", "rdf:type", "ns:District")
        qm.addParam("?St", "ns:inDistrict", "?District")
        qm.addParam("?District", "rdfs:label", "?DtLabel")
        qm.addOrder("asc(?StationCode)")
        listStations = qm.executeQuery()
        return listStations
    # END FUNCTION
# END CLASS

        
class StationInfoWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        #ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)       
        # Station info label
        self.st_label = QLabel("STATION:  " + parent.station_toShow + ", " + parent.stName_toShow, self)
        self.st_label.setGeometry(60, 140, 700, 30)

        # District info label
        self.ds_label = QLabel("DISTRICT:  " + parent.district_toShow, self)
        self.ds_label.setGeometry(60, 200, 500, 30)

        # URI label
        self.uri_label = QLabel("URI:  ", self)
        self.uri_label.setGeometry(60, 80, 500, 30)

        # URI text
        self.uri_text = QLabel(self)
        self.uri_text.setGeometry(90, 80, 500, 30)
        self.uri_text.setOpenExternalLinks(True)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)

        # Graph button
        self.graph_button = QPushButton('GRAPH', self)
        self.graph_button.setGeometry(135, 320, 50, 30)
        self.graph_button.pressed.connect(self.graphButton)

        # Mg combo
        self.mg_combo = QComboBox(self)
        self.mg_combo.setGeometry(60, 280, 70, 30)
        self.mg_combo.addItems(["1- SO2", "6- CO", "7- NO", "8- NO2", 
                                   "9- PM2.5", "10- PM10", "12- NOx", "14- O3", 
                                   "20- TOL", "30- BEN", "35- EBE", "42- TCH", 
                                   "43- CH4", "44- NMHC"])

        # Select combo button
        self.sel_combo = QPushButton("SELECT", self)
        self.sel_combo.setGeometry(135, 280, 50, 30)
        self.sel_combo.pressed.connect(self.changeMg)

        ## TODO
        # si cambia
        self.id_magnitude = "0"
        #no cambia
        self.nombre_estacion = parent.stName_toShow

        self.listStations = self.getStations()
        
        stationX = self.getStation(parent.station_toShow)

        self.uri_text.setText("<a href=" + stationX["St"] + ">" + stationX["St"] + "</a>")

    ##

    def changeMg(self):
        self.id_magnitude = self.mg_combo.currentText().split('-')[0]

    def getStation(self, nombre):
        result = None
        for item in self.listStations:
            if item["StationCode"] == nombre:
                result = item
                break
        return result

    def getStations(self):
        qm = QueryMaker()
        qm.addSelect("?St ?StLabel ?StationCode ?DtLabel")
        qm.addParam("?St", "rdf:type", "ns:Station")
        qm.addParam("?St", "rdfs:label", "?StLabel")
        qm.addParam("?St", "ns:stationCode", "?StationCode")
        qm.addParam("?District", "rdf:type", "ns:District")
        qm.addParam("?St", "ns:inDistrict", "?District")
        qm.addParam("?District", "rdfs:label", "?DtLabel")
        qm.addOrder("asc(?StationCode)")
        listStations = qm.executeQuery()
        return listStations
    # END FUNCTION

    def graphButton(self):
        gm = GraphMaker()
        gm.selectMagnitude(self.id_magnitude)
        gm.selectPlace(False, self.nombre_estacion)
        df = gm.graphData()

        df.plot()
        plt.show()

    # END FUNCTION
# END CLASS



## TODO cambiar copypaste
class DistrictInfoWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        #ws_path = os.path.dirname(os.path.abspath(__file__))

        # District info label
        self.ds_label = QLabel("DISTRICT:  " + parent.district_toShow, self)
        self.ds_label.setGeometry(60, 120, 500, 30)

        # URI label
        self.uri_label = QLabel("URI:  ", self)
        self.uri_label.setGeometry(60, 40, 500, 30)

        # URI text
        self.uri_text = QLabel(self)
        self.uri_text.setGeometry(90, 40, 500, 30)
        self.uri_text.setOpenExternalLinks(True)

        # URI wiki label
        self.uriwk_label = QLabel("URI(wiki):  ", self)
        self.uriwk_label.setGeometry(60, 80, 500, 30)

        # URI wiki text
        self.uriwk_text = QLabel(self)
        self.uriwk_text.setGeometry(120, 80, 500, 30)
        self.uriwk_text.setOpenExternalLinks(True)

        # Population label
        self.pop_label = QLabel("POPULATION:  ", self)
        self.pop_label.setGeometry(60, 160, 500, 30)

        # Area label
        self.area_label = QLabel("AREA:  ", self)
        self.area_label.setGeometry(60, 200, 500, 30)

        # Density label
        self.den_label = QLabel("DENSITY:  ", self)
        self.den_label.setGeometry(60, 240, 500, 30)

        # Stations list label
        self.stlist_label = QLabel("STATIONS IN THIS DISTRICT:  ", self)
        self.stlist_label.setGeometry(60, 280, 500, 30)

        # Stations list text
        self.stlist_text = QTextEdit(self)
        self.stlist_text.setGeometry(60, 310, 300, 120)
        self.stlist_text.setReadOnly(True)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)

        # Graph button
        self.graph_button = QPushButton('GRAPH', self)
        self.graph_button.setGeometry(550, 360, 50, 30)
        self.graph_button.pressed.connect(self.graphButton)

        # Mg combo
        self.mg_combo = QComboBox(self)
        self.mg_combo.setGeometry(420, 360, 70, 30)
        self.mg_combo.addItems(["1- SO2", "6- CO", "7- NO", "8- NO2", 
                                   "9- PM2.5", "10- PM10", "12- NOx", "14- O3", 
                                   "20- TOL", "30- BEN", "35- EBE", "42- TCH", 
                                   "43- CH4", "44- NMHC"])

        # Select mg button
        self.selmg_button = QPushButton("SELECT", self)
        self.selmg_button.setGeometry(495, 360, 50, 30)
        self.selmg_button.pressed.connect(self.changeMg)

        """
        self.graph_button = QPushButton('GRAPH', self)
        self.graph_button.setGeometry(500, 300, 50, 30)
        self.graph_button.pressed.connect(self.graphButton)
        """

        ## TODO
        # si cambia
        self.id_magnitude = "1" # COMBO
        #no cambia
        self.nombre_distrito = parent.district_toShow


        url = 'https://query.wikidata.org/sparql'
        q = """
            SELECT DISTINCT
                ?item ?itemLabel ?population ?area ?image
            WHERE {
                ?item wdt:P31 wd:Q3032114 .
                ?item wdt:P1082 ?population .
                ?item wdt:P2046 ?area .
                OPTIONAL{?item wdt:P18 ?image . }
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            """
        r = requests.get(url, params = {'format': 'json', 'query': q})
        data = r.json()

        districts_aux = []
        for item in data['results']['bindings']:
            if "image" in item :
                districts_aux.append(collections.OrderedDict({'districtURI': item['item']['value'],
                                            'districtName': item['itemLabel']['value'],
                                            'population': item['population']['value'],
                                            'area': item['area']['value'],
                                            'image': item['image']['value'],
                }))
            else: 
                districts_aux.append(collections.OrderedDict({'districtURI': item['item']['value'],
                                            'districtName': item['itemLabel']['value'],
                                            'population': item['population']['value'],
                                            'area': item['area']['value'],
                }))

        self.s = None
        for item in districts_aux : 
            if item["districtName"] == self.nombre_distrito :
                self.urlwk_text_aux = item["districtURI"]
                self.population = item["population"]
                basura0 = float(item["area"])
                self.area = f'{basura0:.2f}'
                basura = float(self.population)/float(basura0)
                self.density = f'{basura:.2f}'
                
                self.image = ""
                if "image" in item :
                    self.image = item["image"]
                    with urllib.request.urlopen(self.image) as url:
                        self.s = url.read()

        
        
        pixmap = QPixmap()
        pixmap.loadFromData(self.s)
        icon = QIcon(pixmap)

        self.districts = None

        self.setGeometry(0, 0, 120, 120)  

        if self.image != "" :
            self.false_button_img_url_wiki_district_semantic_web_2020_mark_pablo_beñat_diana_jax_no_copyright = QPushButton(self)
            self.false_button_img_url_wiki_district_semantic_web_2020_mark_pablo_beñat_diana_jax_no_copyright.setGeometry(370, 120, 300, 200)
            self.false_button_img_url_wiki_district_semantic_web_2020_mark_pablo_beñat_diana_jax_no_copyright.setIcon(icon)
            self.false_button_img_url_wiki_district_semantic_web_2020_mark_pablo_beñat_diana_jax_no_copyright.setIconSize(QSize(250, 250))
            self.false_button_img_url_wiki_district_semantic_web_2020_mark_pablo_beñat_diana_jax_no_copyright.setStyleSheet("border : outset")

        df = pd.DataFrame(districts_aux)
        df.set_index("districtURI")
        self.districts = df.astype({'population': int, 'area': float})
        self.listDistricts = self.getDistricts()

        districtX = self.getDistrict(self.nombre_distrito)
        self.st_in_dt = districtX["Stations"]

        self.uri_text.setText("<a href=" + districtX["Dt"] + ">" + districtX["Dt"] + "</a>")
        self.uriwk_text.setText("<a href=" + self.urlwk_text_aux + ">" + self.urlwk_text_aux + "</a>")
        self.pop_label.setText("POPULATION:  " + self.population + " inhabitants")
        self.area_label.setText("AREA:  " + self.area + " km2")
        self.den_label.setText("DENSITY:  " + self.density + " in/km2")
        
        district_aux = ""

        for stations in self.st_in_dt :

            district_aux += (stations + "\n")
        
        self.stlist_text.setPlainText(district_aux)
        
    ## 

    def changeMg(self):
        self.id_magnitude = self.mg_combo.currentText().split('-')[0]

    def graphButton(self):
        gm = GraphMaker()
        gm.selectMagnitude(self.id_magnitude)
        gm.selectPlace(True, self.nombre_distrito)
        df = gm.graphData()
        df.plot()
        plt.show()

    def getDistrict(self, nombre):
        result = None
        for item in self.listDistricts:
            if item["DtLabel"] == nombre:
                result = item
                break
        return result

    def getDistricts(self):
        qm = QueryMaker()
        qm.addSelect("?Dt ?DtLabel ?DistrictCode ?St")
        qm.addParam("?Dt", "rdf:type", "ns:District")
        qm.addParam("?Dt", "rdfs:label", "?DtLabel")
        qm.addParam("?Dt", "ns:districtID", "?DistrictCode")
        qm.addOrder("asc(?DtLabel)")
        listDistricts = qm.executeQuery()
        qm.cleanQuery()
        for item in listDistricts:
            qm.addSelect("?StLabel")
            qm.addParam("?St", "rdf:type", "ns:Station")
            qm.addParam("?St", "rdfs:label", "?StLabel")
            qm.addParam("?St", "ns:inDistrict", "<" + item["Dt"] + ">")
            stationsInDistrict = qm.executeQuery()
            qm.cleanQuery()
            ls = []
            for station in stationsInDistrict:
                ls.append(station["StLabel"])
            item["Stations"] = ls
        return listDistricts
    # END FUNCTION
# END CLASS


class MGWidget(QWidget):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.ws_path = os.path.dirname(os.path.abspath(__file__))

        self.mg_id = ""
        self.mg_notation = ""
        self.mg_nombre = ""
        self.mg_name = ""
        self.mg_wiki = ""
        self.mg_def = ""

        self.setGeometry(0, 0, 120, 120)
        # Select magnitude label
        self.selmg_label = QLabel('SELECT MAGNITUDE', self)
        self.selmg_label.setGeometry(60, 170, 100, 30)
        # Select magnitude combo box
        self.selmg_combo = QComboBox(self)
        self.selmg_combo.setGeometry(59, 200, 100, 30)
        self.selmg_combo.addItems(["1- SO2", "6- CO", "7- NO", "8- NO2", 
                                   "9- PM2.5", "10- PM10", "12- NOx", "14- O3", 
                                   "20- TOL", "30- BEN", "35- EBE", "42- TCH", 
                                   "43- CH4", "44- NMHC"])

        # Search button
        self.search_button = QPushButton("SEARCH", self)
        self.search_button.setGeometry(59, 240, 100, 30)
        self.search_button.pressed.connect(self.magnitudesSearch)
        
        # Info labels
        self.mgid_label = QLabel("ID:  " + self.mg_id, self)
        self.mgid_label.setGeometry(250, 60, 400, 30)
        #self.mgid_label.setFont(QFont('Arial', 13))

        self.mgnt_label = QLabel("NOTATION:  " + self.mg_notation, self)
        self.mgnt_label.setGeometry(250, 100, 400, 30)
        #self.mgnt_label.setFont(QFont('Arial', 13))
        
        self.mgname_label = QLabel("NAME(en):  " + self.mg_name, self)
        self.mgname_label.setGeometry(250, 140, 400, 30)
        #self.mgname_label.setFont(QFont('Arial', 13))

        self.mgnom_label = QLabel("NAME(es):  " + self.mg_nombre, self)
        self.mgnom_label.setGeometry(250, 180, 400, 30)
        #self.mgnom_label.setFont(QFont('Arial', 13))
        self.mgwk_label = QLabel("WIKIDATA_ID:  ", self)
        self.mgwk_label.setGeometry(250, 220, 400, 30)
        #self.mgwk_label.setFont(QFont('Arial', 13))

        # self.mgwk_text = QLabel("<a href=self.mg_wiki</a>", self)
        self.mgwk_text = QLabel(self)
        self.mgwk_text.setGeometry(325, 220, 400, 30)
        #self.mgwk_label.setFont(QFont('Arial', 13))


        self.mgdef_label = QLabel("SUMMARY:  ", self)
        self.mgdef_label.setGeometry(250, 260, 400, 30)
        #self.mgdef_label.setFont(QFont('Arial', 13))

        # SUMMARY text
        self.mgdef_text = QTextEdit(self)
        self.mgdef_text.setGeometry(310, 264, 300, 100)
        self.mgdef_text.setReadOnly(True)

        # WIKIDATAID text
        # self.mgwk_text = QTextEdit(self)
        # self.mgwk_text.setGeometry(325, 224, 300, 30)
        # self.mgwk_text.setReadOnly(True)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
    
    def magnitudesSearch(self):

        # Obtención del valor de la magnitud seleccionada
        valor_id = self.selmg_combo.currentText().split('-')[0]

        # Creación de un objeto QueryMaker (puedes hacerlo global y reusarlo)
        qm = QueryMaker()

        # Selección de los atributos que se requieren
        qm.addSelect("?Magnitude ?Id ?Notation ?Nombre ?Name ?Wiki ?Description")
        
        # Construcción de la query
        qm.addParam("?Magnitude", "rdf:type", "ns:Magnitude")
        qm.addParam("?Magnitude", "rdfs:comment", "?Description")
        qm.addParam("?Magnitude", "ns:measureNotation", "?Notation")
        qm.addParam("?Magnitude", "ns:measureCode", "?Id")
        qm.addFilter("(?Id = \"{}\")".format(valor_id))
        qm.addParam("?Magnitude", "owl:sameAs", "?Wiki")
        qm.addParam("?Magnitude", "rdfs:label", "?Name , ?Nombre")
        qm.addFilter("(LANG(?Name) = 'en' && LANG(?Nombre) = 'es')")
        
        # Ejecución de la query
        listResult = qm.executeQuery()

        # (Aquí solo tiene 1 elemento la lista, por haber seleccionado una magnitud)
        for item in listResult:

            self.mg_id = item["Id"]
            self.mg_notation = item["Notation"]
            self.mg_nombre = item["Nombre"]
            self.mg_name = item["Name"]
            self.mg_wiki = item["Wiki"]
            self.mg_def = item["Description"]

            # No quitar esta parte comentada si al final decidimos que la 
            # descripcion deberia ser un label y no un textEdit
            """
            aux = self.mg_def.split()
            self.mg_def = ""
            i = 0
            for word in aux :
                if i < 10 :
                    self.mg_def += word + " "
                    i += 1
                else :
                    self.mg_def += "\n" + word + " "
                    i = 0
            """

            self.mgid_label.setText("ID:  " + self.mg_id)
            self.mgnt_label.setText("NOTATION:  " + self.mg_notation)
            self.mgnom_label.setText("NAME(es):  " + self.mg_nombre)
            self.mgname_label.setText("NAME(en):  " + self.mg_name)
            self.mgwk_text.setOpenExternalLinks(True)
            self.mgwk_text.setText("<a href=" + self.mg_wiki + ">" + self.mg_wiki + "</a>")
            #self.mgwk_text.setPlainText(self.mg_wiki)
            self.mgdef_text.setPlainText(self.mg_def)
    # END FUNCTION
# END CLASS


class DGWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(50, 50, 614, 800)

        img_label = QLabel(self)
        img = QPixmap(os.path.join(ws_path, "../resources/ontology_dg.png"))
        #img = img.scaledToHeight(495)
        img_label.setPixmap(img)
        #img_label.move(160, 0)
    # END FUNCTION
# END CLASS


class MTextWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        # Text label
        self.text_line = QTextEdit(self)
        self.text_line.setGeometry(100, 50, 500, 400)
        self.text_line.setReadOnly(True)

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION

    def changeText(self, type):
        if type == "dp" :
            self.text_line.setPlainText("URI    http://www.schema.org#address\n:schema:address rdf:type owl:DatatypeProperty ;\n                            rdfs:domain schema:Place ;\n                            rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.schema.org#latitude\nschema:latitude rdf:type owl:DatatypeProperty ;\n                           rdfs:domain schema:Place ;\n                           rdfs:range schema:Number ."
                                    + "\n\n\nURI    http://www.schema.org#longitude\nschema:longitude rdf:type owl:DatatypeProperty ;\n                             rdfs:domain schema:Place ;\n                             rdfs:range schema:Number ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#dateOfMeasure\n:dateOfMeasure rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range xsd:dateTime ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#districtID\n:districtID rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :District ;\n                           rdfs:range xsd:integer ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureCode\n:measureCode rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Magnitude ,\n                           :Measurement ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureNotation\n:measureNotation rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Magnitude ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureValue\n:measureValue rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range xsd:float ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#stationCode\n:stationCode rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Station ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#streetID\n:streetID rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Street ;\n                           rdfs:range xsd:integer .")
        elif type == "obj" :
            self.text_line.setPlainText("URI    http://www.semanticweb.org/group16/ontology/air-quality#inStreet\n:inStreet rdf:type owl:ObjectProperty ;\n               rdfs:domain :Station ;\n               rdfs:range :Street ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#inDistrict\n:inDistrict rdf:type owl:ObjectProperty ;\n                           rdfs:domain [\n                           rdf:type owl:Class ;\n                           owl:Class   :Station,\n                                             :Street\n                           ] ;\n                           rdfs:range :District ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measuredAt\n:measuredAt rdf:type owl:ObjectProperty ;\n                      rdfs:domain :Measurement ;\n                      rdfs:range :Station ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measuredMagnitude\n:measuredMagnitude rdf:type owl:ObjectProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range :Magnitude .")
        elif type == "cls" :
            self.text_line.setPlainText("URI    http://www.semanticweb.org/group16/ontology/air-quality#District\n:District rdf:type owl:Class ;\n          rdfs:subClassOf <https://schema.org/Place> ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#Magnitude\n:Magnitude rdf:type owl:Class ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#Measurement\n:Measurement rdf:type owl:Class ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#Station\n:Station rdf:type owl:Class ;\n         rdfs:subClassOf <https://schema.org/Place> ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#Street\n:Street rdf:type owl:Class ;\n        rdfs:subClassOf <https://schema.org/Place> ."
                                    + "\n\n\nURI    https://schema.org/Place\n<https://schema.org/Place> rdf:type owl:Class .")
    # END FUNCTION
# END CLASS


class QueryInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(50, 50, 614, 800)

        # Text label
        self.query_line = QTextEdit(self)
        self.query_line.setGeometry(100, 50, 500, 400)
        self.query_line.setReadOnly(True)
        
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)

        qm = QueryMaker()
        
        listResult = qm.appQuery(parent.check_list, parent.query_list)

        testo = ""

        for item in listResult:
            self.measure_id = item["Measure"]
            self.measure_station = item["StationLb"]
            self.measure_date = item["Date"]
            self.measure_magnitude_en = item["MagnitudeLbEn"]
            self.measure_magnitude_es = item["MagnitudeLbEs"]
            self.measure_value = item["Value"]
            unit = self.getUnitOfMeasure(item["MagnitudeCode"])
            testo += ("\n" + self.measure_id + "\n\t" +
                     self.measure_station + "\n\t" +
                     self.measure_date + "\n\t" +
                     self.measure_magnitude_en + "\n\t" +
                     self.measure_magnitude_es + "\n\t" +
                     str(self.measure_value) + " " + unit + "\n")

        self.query_line.setPlainText(testo)
        # END FUNCTION
        
    # [private function] getUnitOfMeasure() -> string
    #   Returns the unit of the measurement given the magnitude
    #   example: getUnitOfMeasure() [magnitude="1"] -> "μg/m3"
    #   example: getUnitOfMeasure() [magnitude="2"] -> "mg/m3"
    def getUnitOfMeasure(self, magnitudeCode):
        magnitudeID = int(magnitudeCode)
        if magnitudeID == 1 or (magnitudeID >= 7 and magnitudeID <= 39):
            return "μg/m3"
        else:
            return "mg/m3"
        # END IF
    # END FUNCTION

# END CLASS


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    #QApplication.setStyle(QStyleFactory.create('sgi'))
    #file = QFile(":/dark.qss")
    #file.open(QFile.ReadOnly | QFile.Text)
    #stream = QTextStream(file)
    #app.setStyleSheet(stream.readAll())

    qtmodern.styles.dark(app)
    wn = qtmodern.windows.ModernWindow(window)

    wn.show()
    #window.show()
    app.exec_()
# END MAIN