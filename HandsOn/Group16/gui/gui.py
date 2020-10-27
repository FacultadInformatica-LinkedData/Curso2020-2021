import os, sys, csv
import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QFile, QTextStream, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QStyleFactory, QComboBox, QCheckBox, QSizePolicy, QGridLayout, QApplication, QMainWindow, QStackedWidget, QMessageBox, QWidget, QHBoxLayout, QPushButton, QLabel


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
        

    def toDS(self):
        self.central_widget.setCurrentWidget(self.ds_widget)

    def toMain(self):
        self.central_widget.setCurrentWidget(self.main_widget)

    def toMS(self):
        self.central_widget.setCurrentWidget(self.ms_widget)
    
    def toModel(self):
        self.central_widget.setCurrentWidget(self.model_widget)

    def toMaps(self):
        self.central_widget.setCurrentWidget(self.maps_widget)

    def toStations(self):
        self.central_widget.setCurrentWidget(self.st_widget)

    def toMG(self):
        self.central_widget.setCurrentWidget(self.mg_widget)

    def toStInfo(self):
        self.station_toShow = self.st_widget.station_tsAux
        self.district_toShow = self.st_widget.district_tsAux
        self.stName_toShow = self.st_widget.stName_tsAux
        # Station info
        self.stinfo_widget = StationInfoWidget(self)
        self.stinfo_widget.back_button.clicked.connect(self.toStations)
        self.central_widget.addWidget(self.stinfo_widget)
        ## NOT NECESSARY ##
        if self.station_toShow != "Vacío" :
            self.central_widget.setCurrentWidget(self.stinfo_widget)


class MainWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Map button
        self.map_button = QPushButton(self)
        self.map_button.setGeometry(85, 45, 250, 250)
        self.map_button.setIcon(QIcon(os.path.join(ws_path, "maps5.png")))
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
        self.ds_button.setIcon(QIcon(os.path.join(ws_path, "lupa5.png")))
        self.ds_button.setIconSize(QSize(200, 200))
        # Magnitudes button
        self.mg_button = QPushButton(self)
        self.mg_button.setGeometry(85, 320, 530, 90)
        self.mg_button.setIcon(QIcon(os.path.join(ws_path, "pollution.png")))
        self.mg_button.setIconSize(QSize(70, 70))
        # Magnitudes label
        self.mg_label = QLabel('MAGNITUDES', self)
        self.mg_label.setGeometry(320, 405, 100, 30)


class DSWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Measurement button
        self.ms_button = QPushButton(self)
        self.ms_button.setGeometry(50, 90, 280, 280)
        self.ms_button.setIcon(QIcon(os.path.join(ws_path, "measure3.png")))
        self.ms_button.setIconSize(QSize(300, 300))
        # Measurement label
        self.ms_label = QLabel('MEASUREMENTS', self)
        self.ms_label.setGeometry(150, 367, 100, 30)
        # Model button
        self.model_button = QPushButton(self)
        self.model_button.setGeometry(365, 90, 280, 280)
        self.model_button.setIcon(QIcon(os.path.join(ws_path, "model3.png")))
        self.model_button.setIconSize(QSize(200, 200))
        # Model label
        self.ms_label = QLabel('MODEL', self)
        self.ms_label.setGeometry(490, 367, 100, 30)
        # Back button
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)


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
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    
    def checkLocation(self, state):
        if QtCore.Qt.Checked == state:
            self.location_combo.setEnabled(True)
        else:
            self.location_combo.setEnabled(False)

    def checkDate(self, state):
        if QtCore.Qt.Checked == state:
            self.date_combo.setEnabled(True)
        else:
            self.date_combo.setEnabled(False)

    def checkMagnitude(self, state):
        if QtCore.Qt.Checked == state:
            self.mg_combo.setEnabled(True)
        else:
            self.mg_combo.setEnabled(False)
            

class ModelWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Data properties button
        self.dp_button = QPushButton(self)
        self.dp_button.setGeometry(100, 40, 190, 190)
        self.dp_button.setIcon(QIcon(os.path.join(ws_path, "dataprop.png")))
        self.dp_button.setIconSize(QSize(150, 150))
        # Data properties label
        self.dp_label = QLabel('DATA PROP', self)
        self.dp_label.setGeometry(165, 225, 100, 30)
        # Object properties properties button
        self.obj_button = QPushButton(self)
        self.obj_button.setGeometry(390, 40, 190, 190)
        self.obj_button.setIcon(QIcon(os.path.join(ws_path, "dataprop.png")))
        self.obj_button.setIconSize(QSize(150, 150))
        # Object properties label
        self.obj_label = QLabel('OBJECT PROP', self)
        self.obj_label.setGeometry(455, 225, 100, 30)
        # Classes button
        self.cls_button = QPushButton(self)
        self.cls_button.setGeometry(248, 260, 190, 190)
        self.cls_button.setIcon(QIcon(os.path.join(ws_path, "dataprop.png")))
        self.cls_button.setIconSize(QSize(150, 150))
        # Classes label
        self.cls_label = QLabel('CLASSES', self)
        self.cls_label.setGeometry(322, 445, 100, 30)
        # Back button
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)


class MapsWidget(QWidget):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(0, 0, 120, 120)
        # Stations button
        self.st_button = QPushButton(self)
        self.st_button.setGeometry(50, 90, 280, 280)
        self.st_button.setIcon(QIcon(os.path.join(ws_path, "stations.png")))
        self.st_button.setIconSize(QSize(200, 200))
        # Stations label
        self.st_label = QLabel('STATIONS', self)
        self.st_label.setGeometry(160, 367, 100, 30)
        # Districts button
        self.dist_button = QPushButton(self)
        self.dist_button.setGeometry(365, 90, 280, 280)
        self.dist_button.setIcon(QIcon(os.path.join(ws_path, "districts.png")))
        self.dist_button.setIconSize(QSize(200, 200))
        # Districts label
        self.dist_label = QLabel('DISTRICTS', self)
        self.dist_label.setGeometry(480, 367, 100, 30)
        # Back button
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)


class StationsWidget(QWidget):
    def __init__(self, parent=None):
        self.station_tsAux = "Vacío"
        self.district_tsAux = "Vacío"
        self.stName_tsAux = "Vacío"

        QLabel.__init__(self, parent)
        ws_path = os.path.dirname(os.path.abspath(__file__))

        img_label = QLabel(self)
        img = QPixmap(os.path.join(ws_path, "madrid5.png"))
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
        ## ESTO VA A HABER QUE MODIFICARLO PARA QUE LOS DATOS LOS RECOJA DE LOS TTL
        self.stations = {self.b_9004:["Pza. de España", "28079004", "Moncloa-Aravaca"], 
                        self.b_9008:["Escuelas Aguirre", "28079008", "Salamanca"], 
                        self.b_9011:["Avda. Ramón y Kajal", "28079011", "Chamartín"],
                        self.b_9016:["Arturo Soria", "28079016", "Ciudad Lineal"],
                        self.b_9017:["Villaverde", "28079017", "Villaverde"],
                        self.b_9018:["Farolillo", "28079018", "Carabanchel"],
                        self.b_9024:["Casa de campo", "28079024", "Moncloa-Aravaca"],
                        self.b_9027:["Barajas Pueblo", "28079027", "Barajas"],
                        self.b_9035:["Pza. del Carmen", "28079035", "Centro"],
                        self.b_9036:["Moratalaz", "28079036", "Moratalaz"],
                        self.b_9038:["Cuatro Caminos", "28079038", "Tetuán"],
                        self.b_9039:["Barrio del Pilar", "28079039", "Fuencarral-El Pardo"],
                        self.b_9040:["Vallecas", "28079040", "Puente de Vallecas"],
                        self.b_9047:["Méndez Álvaro", "28079047", "Arganzuela"],
                        self.b_9048:["Castellana", "28079048", "Chamartín"],
                        self.b_9049:["Parque del Retiro", "28079049", "Retiro"],
                        self.b_9050:["Plaza Castilla", "28079050", "Chamartín"],
                        self.b_9054:["Ensanche de Vallecas", "28079054", "Villa de Vallecas"],
                        self.b_9055:["Urb. Embajada", "28079055", "Barajas"],
                        self.b_9056:["Pza. Elíptica", "28079056", "Usera"],
                        self.b_9057:["Sanchinarro", "28079057", "Hortaleza"],
                        self.b_9058:["El Pardo", "28079058", "Fuencarral-El Pardo"],
                        self.b_9059:["Juan Carlos I", "28079059", "Barajas"],
                        self.b_9060:["Tres Olivos", "28079060", "Fuencarral-El Pardo"]}

        # Select station combo box
        self.sel_combo = QComboBox(self)
        self.sel_combo.setGeometry(500, 230, 100, 30)
        self.sel_combo.addItems(["Vacío","Pza. de España","Escuelas Aguirre",
                                "Avda. Ramón y Kajal","Arturo Soria",
                                "Villaverde","Farolillo",
                                "Casa de campo","Barajas Pueblo",
                                "Pza. del Carmen","Moratalaz",
                                "Cuatro Caminos","Barrio del Pilar",
                                "Vallecas","Méndez Álvaro",
                                "Castellana","Parque del Retiro",
                                "Plaza Castilla","Ensanche de Vallecas",
                                "Urb. Embajada","Pza. Elíptica",
                                "Sanchinarro","El Pardo",
                                "Juan Carlos I","Tres Olivos"])
        
        self.b_9004.pressed.connect(lambda: self.selMap("28079004"))
        self.b_9008.pressed.connect(lambda: self.selMap("28079008"))
        self.b_9011.pressed.connect(lambda: self.selMap("28079011"))
        self.b_9016.pressed.connect(lambda: self.selMap("28079016"))
        self.b_9017.pressed.connect(lambda: self.selMap("28079017"))
        self.b_9018.pressed.connect(lambda: self.selMap("28079018"))
        self.b_9024.pressed.connect(lambda: self.selMap("28079024"))
        self.b_9027.pressed.connect(lambda: self.selMap("28079027"))
        self.b_9035.pressed.connect(lambda: self.selMap("28079035"))
        self.b_9036.pressed.connect(lambda: self.selMap("28079036"))
        self.b_9038.pressed.connect(lambda: self.selMap("28079038"))
        self.b_9039.pressed.connect(lambda: self.selMap("28079039"))
        self.b_9040.pressed.connect(lambda: self.selMap("28079040"))
        self.b_9047.pressed.connect(lambda: self.selMap("28079047"))
        self.b_9048.pressed.connect(lambda: self.selMap("28079048"))
        self.b_9049.pressed.connect(lambda: self.selMap("28079049"))
        self.b_9050.pressed.connect(lambda: self.selMap("28079050"))
        self.b_9054.pressed.connect(lambda: self.selMap("28079054"))
        self.b_9055.pressed.connect(lambda: self.selMap("28079055"))
        self.b_9056.pressed.connect(lambda: self.selMap("28079056"))
        self.b_9057.pressed.connect(lambda: self.selMap("28079057"))
        self.b_9058.pressed.connect(lambda: self.selMap("28079058"))
        self.b_9059.pressed.connect(lambda: self.selMap("28079059"))
        self.b_9060.pressed.connect(lambda: self.selMap("28079060"))

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
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)


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
            elif station == "Vacío" :
                self.more_button.setEnabled(False)

    
    # Change color of a point in the map when selected in map
    def selMap(self, station):
        for id, st in self.stations.items():
            id.setStyleSheet("background-color:red")
            if st[1] == station :
                id.setStyleSheet("background-color:green")
                self.sel_combo.setCurrentText(st[0])
                self.sel_button.click()

        
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
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)


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
        self.selmg_combo.addItems(["SO2", "CO", "NO", "NO2", 
                                   "PM2.5", "PM10", "NOx", "O3", 
                                   "TOL", "BEN", "EBE", "TCH", 
                                   "CH4", "NMHC"])

        # Search button
        self.search_button = QPushButton("SEARCH", self)
        self.search_button.setGeometry(59, 240, 100, 30)
        self.search_button.pressed.connect(self.csvSearch)
        
        # Info labels
        self.mgid_label = QLabel("ID:  " + self.mg_id, self)
        self.mgid_label.setGeometry(250, 60, 400, 30)
        #self.mgid_label.setFont(QFont('Arial', 13))

        self.mgnt_label = QLabel("NOTATION:  " + self.mg_notation, self)
        self.mgnt_label.setGeometry(250, 100, 400, 30)
        #self.mgnt_label.setFont(QFont('Arial', 13))
        
        self.mgnom_label = QLabel("NOMBRE:  " + self.mg_nombre, self)
        self.mgnom_label.setGeometry(250, 140, 400, 30)
        #self.mgnom_label.setFont(QFont('Arial', 13))

        self.mgname_label = QLabel("NAME:  " + self.mg_name, self)
        self.mgname_label.setGeometry(250, 180, 400, 30)
        #self.mgname_label.setFont(QFont('Arial', 13))

        self.mgwk_label = QLabel("WIKIDATA_ID:  " + self.mg_wiki, self)
        self.mgwk_label.setGeometry(250, 220, 400, 30)
        #self.mgwk_label.setFont(QFont('Arial', 13))

        self.mgdef_label = QLabel("DEFINITION:  " + self.mg_def, self)
        self.mgdef_label.setGeometry(250, 260, 400, 30)
        #self.mgdef_label.setFont(QFont('Arial', 13))

                
        # Csv search
        ## ESTO VA A HABER QUE MODIFICARLO PARA QUE LOS DATOS LOS RECOJA DE LOS TTL
        self.csvSearch()

        # Back button
        self.back_button = QPushButton('ATRÁS', self)
        self.back_button.setGeometry(30, 5, 50, 30)
    
    ## ESTO VA A HABER QUE MODIFICARLO PARA QUE LOS DATOS LOS RECOJA DE LOS TTL
    def csvSearch(self):
        with open(os.path.join(self.ws_path, "magnitudes.csv")) as csv_mg:
            csv_reader = csv.reader(csv_mg, delimiter = ',')
            i = 0
            for row in csv_reader :
                if i > 0 :
                    if row[1] == self.selmg_combo.currentText() :
                        self.mg_id = row[0]
                        self.mg_notation = row[1]
                        self.mg_nombre = row[2]
                        self.mg_name = row[3]
                        self.mg_wiki = row[4]
                        self.mg_def = row[5]

                        self.mgid_label.setText("ID:  " + self.mg_id)
                        self.mgnt_label.setText("NOTATION:  " + self.mg_notation)
                        self.mgnom_label.setText("NOMBRE:  " + self.mg_nombre)
                        self.mgname_label.setText("NAME:  " + self.mg_name)
                        self.mgwk_label.setText("WIKIDATA_ID:  " + self.mg_wiki)
                        self.mgdef_label.setText("DEFINITION:  " + self.mg_def)
                        break
                i += 1



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