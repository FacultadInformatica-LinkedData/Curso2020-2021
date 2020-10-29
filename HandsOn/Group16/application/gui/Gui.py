#-. Gui class .-#
#.- Displays the user interface of the application .-#

# Imports
import os, sys
import qtmodern.styles
import qtmodern.windows

sys.path.insert(1, './application/model/')
from QueryMaker import QueryMaker

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QFile, QTextStream, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QDialog, QStyleFactory, QComboBox, QCheckBox, QSizePolicy, QGridLayout, QApplication, QMainWindow, QStackedWidget, QMessageBox, QWidget, QHBoxLayout, QPushButton, QLabel


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
        self.central_widget.addWidget(self.maps_widget)
        # Stations
        self.st_widget = StationsWidget(self)
        self.st_widget.back_button.clicked.connect(self.toMaps)
        self.st_widget.more_button.clicked.connect(self.toStInfo)
        self.central_widget.addWidget(self.st_widget)
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

    def toMG(self):
        self.central_widget.setCurrentWidget(self.mg_widget)
    # END FUNCTION

    def toDG(self):
        #self.central_widget.setCurrentWidget(self.dg_widget)

        self.dg_window = DGWindow()
        self.dg_window.show()
    # END FUNCTION

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

        ## LOCATION ##
        # Location check box
        self.location_check = QCheckBox("LOCATION", self)
        self.location_check.stateChanged.connect(self.checkLocation)
        self.location_check.setGeometry(30, 60, 200, 50)
        # Location combo box
        self.location_combo = QComboBox(self)
        self.location_combo.setGeometry(250, 80, 100, 30)
        self.location_combo.setEnabled(False)
        self.location_combo.addItems(["uno", "dos", "tres"])

        ## DATE/RANGE ##
        # Date check box
        self.date_check = QCheckBox("DATE", self)
        self.date_check.stateChanged.connect(self.checkDate)
        self.date_check.setGeometry(30, 120, 200, 50)
        # Date combo box
        self.date_combo = QComboBox(self)
        self.date_combo.setGeometry(250, 140, 100, 30)
        self.date_combo.setEnabled(False)
        self.date_combo.addItems(["uno", "dos", "tres"])

        self.date1_combo = QComboBox(self)
        self.date1_combo.setGeometry(350, 140, 100, 30)
        self.date1_combo.setEnabled(False)
        self.date1_combo.addItems(["uno", "dos", "tres"])

        self.date2_combo = QComboBox(self)
        self.date2_combo.setGeometry(450, 140, 100, 30)
        self.date2_combo.setEnabled(False)
        self.date2_combo.addItems(["uno", "dos", "tres"])

        ## MAGNITUDE ##
        # Magnitude check box
        self.mg_check = QCheckBox("MAGNITUDE", self)
        self.mg_check.stateChanged.connect(self.checkMagnitude)
        self.mg_check.setGeometry(30, 180, 200, 50)
        # Magnitude combo box
        self.mg_combo = QComboBox(self)
        self.mg_combo.setGeometry(250, 200, 100, 30)
        self.mg_combo.setEnabled(False)
        self.mg_combo.addItems(["uno", "dos", "tres"])

        # Query button
        self.query_button = QPushButton('QUERY', self)
        self.query_button.setGeometry(325, 400, 50, 30)
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    # END FUNCTION
    
    def checkLocation(self, state):
        if QtCore.Qt.Checked == state:
            self.location_combo.setEnabled(True)
        else:
            self.location_combo.setEnabled(False)
    # END FUNCTION

    def checkDate(self, state):
        if QtCore.Qt.Checked == state:
            self.date_combo.setEnabled(True)
        else:
            self.date_combo.setEnabled(False)
    # END FUNCTION

    def checkMagnitude(self, state):
        if QtCore.Qt.Checked == state:
            self.mg_combo.setEnabled(True)
        else:
            self.mg_combo.setEnabled(False)
    # END FUNCTION
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
        self.dist_button.setIcon(QIcon(os.path.join(ws_path, "../resources/districts.png")))
        self.dist_button.setIconSize(QSize(200, 200))
        # Districts label
        self.dist_label = QLabel('DISTRICTS', self)
        self.dist_label.setGeometry(480, 367, 100, 30)
        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
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
        self.sel_combo.addItems(["Empty",listStations[0]["StLabel"],listStations[1]["StLabel"],listStations[2]["StLabel"],
                listStations[3]["StLabel"],listStations[4]["StLabel"],listStations[5]["StLabel"],listStations[6]["StLabel"],
                listStations[7]["StLabel"],listStations[8]["StLabel"],listStations[9]["StLabel"],listStations[10]["StLabel"],
                listStations[11]["StLabel"],listStations[12]["StLabel"],listStations[13]["StLabel"],listStations[14]["StLabel"],
                listStations[15]["StLabel"],listStations[16]["StLabel"],listStations[17]["StLabel"],listStations[18]["StLabel"],
                listStations[19]["StLabel"],listStations[20]["StLabel"],listStations[21]["StLabel"],listStations[22]["StLabel"],
                listStations[23]["StLabel"]])
        
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
        self.st_label.setGeometry(60, 60, 700, 30)
        self.st_label.setFont(QFont('Arial', 15))
        # District info label
        self.ds_label = QLabel("DISTRICT:  " + parent.district_toShow, self)
        self.ds_label.setGeometry(60, 120, 500, 30)
        self.ds_label.setFont(QFont('.SF NS Text', 15))
        # URI label
        self.uri_label = QLabel("URI:  ", self)
        self.uri_label.setGeometry(170, 5, 500, 30)
        self.uri_label.setFont(QFont('Arial', 12))

        # Back button
        self.back_button = QPushButton('BACK', self)
        self.back_button.setGeometry(30, 5, 50, 30)
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

        self.mgwk_label = QLabel("WIKIDATA_ID:  " + self.mg_wiki, self)
        self.mgwk_label.setGeometry(250, 220, 400, 30)
        #self.mgwk_label.setFont(QFont('Arial', 13))

        self.mgdef_label = QLabel("SUMMARY:  " + self.mg_def, self)
        self.mgdef_label.setGeometry(250, 260, 400, 30)
        #self.mgdef_label.setFont(QFont('Arial', 13))

        # SUMMARY text
        self.mgdef_text = QTextEdit(self)
        self.mgdef_text.setGeometry(310, 264, 300, 100)
        self.mgdef_text.setReadOnly(True)

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
            self.mgwk_label.setText("WIKIDATA_ID:  " + self.mg_wiki)
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
            self.text_line.setPlainText("URI    http://www.semanticweb.org/group16/ontology/air-quality#dateOfMeasure\n:dateOfMeasure rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range xsd:dateTime ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#districtID\n:districtID rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :District ;\n                           rdfs:range xsd:integer ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureCode\n:measureCode rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Magnitude ,\n                           :Measurement ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureNotation\n:measureNotation rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Magnitude ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measureValue\n:measureValue rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range xsd:float ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#stationCode\n:stationCode rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Station ;\n                           rdfs:range xsd:string ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#streetID\n:streetID rdf:type owl:DatatypeProperty ;\n                           rdfs:domain :Street ;\n                           rdfs:range xsd:integer .")
        elif type == "obj" :
            self.text_line.setPlainText("URI    http://www.semanticweb.org/group16/ontology/air-quality#inDistrict\n:inDistrict rdf:type owl:ObjectProperty ;\n                           rdfs:domain :Station ,\n                                       :Street ;\n                           rdfs:range :District ."
                                    + "\n\n\nURI    http://www.semanticweb.org/group16/ontology/air-quality#measuredAt\n:measuredAt rdf:type owl:ObjectProperty ;\n                           rdfs:domain :Measurement ;\n                           rdfs:range :Station ."
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