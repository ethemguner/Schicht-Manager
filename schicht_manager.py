from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pylab
from statistics import mean
from statistics import StatisticsError
from PyQt5.QtWidgets import QMessageBox
import shutil
import datetime
import xlsxwriter
import os


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schicht Manager")
        self.init_ui()
        self.setTheme()

    def setTheme(self):
        self.labelFont = QtGui.QFont("Trebuchet MS", 11, QtGui.QFont.Bold)
        self.labelFont2 = QtGui.QFont("Trebuchet MS", 12, QtGui.QFont.Bold)
        self.buttonFont = QtGui.QFont("Trebuchet MS", 12, QtGui.QFont.Light)
        self.cbFont = QtGui.QFont("Trebuchet MS", 9, QtGui.QFont.Light)
        self.dateFont = QtGui.QFont("Trebuchet MS", 11, QtGui.QFont.Bold)
        self.wellcomeFont = QtGui.QFont("Trebuchet MS", 20, QtGui.QFont.Light)


        self.shift_label.setFont(self.labelFont)
        self.info.setFont(self.labelFont)
        self.value_label.setFont(self.labelFont)
        self.dateLable.setFont(self.dateFont)
        self.months_lb.setFont(self.labelFont)
        self.ein_rb.setFont(self.labelFont2)
        self.drei_rb.setFont(self.labelFont2)
        self.edit_button.setFont(self.buttonFont)
        self.averages_b.setFont(self.buttonFont)
        self.saveRB.setFont(self.buttonFont)
        self.createExcel.setFont(self.buttonFont)
        self.shift_cb.setFont(self.cbFont)
        self.months.setFont(self.cbFont)
        self.graph_cb.setFont(self.cbFont)
        self.welcome_lb.setFont(self.wellcomeFont)
        self.backupButon.setFont(self.buttonFont)
        self.about.setFont(self.cbFont)
        self.viewList.setFont(self.labelFont)
        self.viewLabel.setFont(self.labelFont)
        self.lastvalue.setFont(self.labelFont)
        self.today.setFont(self.labelFont)

        self.edit_button.setStyleSheet("QPushButton  {background: #00589E; color: white;}")
        self.averages_b.setStyleSheet("QPushButton   {background: #00589E; color: white;}")
        self.saveRB.setStyleSheet("QPushButton       {background: #00589E; color: white;}")
        self.createExcel.setStyleSheet("QPushButton  {background: #00589E; color: white;}")
        self.dateLable.setStyleSheet("QLabel         {background: #00589E; color: white;}")
        self.backupButon.setStyleSheet("QPushButton  {background: #00589E; color: white;}")
        self.viewList.setStyleSheet("QListWidget     {background: #515050; color: #F5B041;}")
        self.about.setStyleSheet("QLabel             {color: white; font: italic;}")
        self.lastvalue.setStyleSheet("QLabel         {color: #48F408; background: #3A3A3A;}")

        self.drei_rb.setStyleSheet("QRadioButton    {color: #FFD700;}")
        self.ein_rb.setStyleSheet("QRadioButton     {color: #FFD700;}")
        self.shift_label.setStyleSheet("QLabel      {color: #DDDCDC;}")
        self.info.setStyleSheet("QLabel             {color: #DDDCDC;}")
        self.value_label.setStyleSheet("QLabel      {color: #DDDCDC;}")
        self.dateLable.setStyleSheet("QLabel        {color: #DDDCDC;}")
        self.months_lb.setStyleSheet("QLabel        {color: #DDDCDC;}")
        self.viewLabel.setStyleSheet("QLabel        {color: #DDDCDC;}")
        self.welcome_lb.setStyleSheet("QLabel       {color: #DDDCDC; font: italic;}")
        self.today.setStyleSheet("QLabel            {color: #9BFF02; font: bold; background: #3A3A3A;}}")
        self.today.setAlignment(QtCore.Qt.AlignRight)
        

    def dataPreProcessing(self):
        try:
            self.shift1_val  = []
            self.shift1_date = []

            self.shift2_val  = []
            self.shift2_date = []

            self.shift3_val  = []
            self.shift3_date = []

            self.shift4_val  = []
            self.shift4_date = []

            self.shift5_val  = []
            self.shift5_date = []

            self.current_month = self.months.currentText()

            if self.drei_rb.isChecked() == True:
                self.shift1_val.clear()
                self.shift1_date.clear()

                self.shift2_val.clear()
                self.shift2_date.clear()

                self.shift3_val.clear()
                self.shift3_date.clear()

                self.shift4_val.clear()
                self.shift4_date.clear()

                self.shift5_val.clear()
                self.shift5_date.clear()

                database = sqlite3.connect("database.db")
                cursor = database.cursor()
                self.info.setText("Verbunden (1)")

                #SHIFT 1
                cursor.execute("SELECT value FROM shift1 WHERE month = ?",[self.current_month])
                self.shift1_values = cursor.fetchall()
                for i in self.shift1_values:
                    self.shift1_val.append(list(i)[0])

                cursor.execute("SELECT date FROM shift1 WHERE month = ?",[self.current_month])
                self.shift1_dates = cursor.fetchall()
                for i in self.shift1_dates:
                    self.shift1_date.append(str(list(i)[0]))

                #SHIFT 2
                cursor.execute("SELECT value FROM shift2 WHERE month = ?",[self.current_month])
                self.shift2_values = cursor.fetchall()
                for k in self.shift2_values:
                    self.shift2_val.append(list(k)[0])
                

                cursor.execute("SELECT date FROM shift2 WHERE month = ?",[self.current_month])
                self.shift2_dates = cursor.fetchall()
                for k in self.shift2_dates:
                    self.shift2_date.append(str(list(k)[0]))
                
                #SHIFT 3
                cursor.execute("SELECT value FROM shift3 WHERE month = ?",[self.current_month])
                self.shift3_values = cursor.fetchall()
                for l in self.shift3_values:
                    self.shift3_val.append(list(l)[0])
                
                
                cursor.execute("SELECT date FROM shift3 WHERE month = ?",[self.current_month])
                self.shift3_dates = cursor.fetchall()
                for l in self.shift3_dates:
                    self.shift3_date.append(str(list(l)[0]))

                #SHIFT 4
                cursor.execute("SELECT value FROM shift4 WHERE month = ?",[self.current_month])
                self.shift4_values = cursor.fetchall()
                for x in self.shift4_values:
                    self.shift4_val.append(list(x)[0])
                

                cursor.execute("SELECT date FROM shift4 WHERE month = ?",[self.current_month])
                self.shift4_dates = cursor.fetchall()
                for x in self.shift4_dates:
                    self.shift4_date.append(str(list(x)[0]))

                #SHIFT 5
                cursor.execute("SELECT value FROM shift5 WHERE month = ?",[self.current_month])
                self.shift5_values = cursor.fetchall()
                for y in self.shift5_values:
                    self.shift5_val.append(list(y)[0])
                

                cursor.execute("SELECT date FROM shift5 WHERE month = ?",[self.current_month])
                self.shift5_dates = cursor.fetchall()
                for y in self.shift5_dates:
                    self.shift5_date.append(str(list(y)[0]))

                try:
                    self.shift1_average = mean(self.shift1_val)
                    self.shift2_average = mean(self.shift2_val)
                    self.shift3_average = mean(self.shift3_val)
                    self.shift4_average = mean(self.shift4_val)
                    self.shift5_average = mean(self.shift5_val)
                except StatisticsError:
                    pass

            elif self.ein_rb.isChecked() == True:
                self.shift1_val.clear()
                self.shift1_date.clear()

                self.shift2_val.clear()
                self.shift2_date.clear()

                self.shift3_val.clear()
                self.shift3_date.clear()

                self.shift4_val.clear()
                self.shift4_date.clear()

                self.shift5_val.clear()
                self.shift5_date.clear()

                database2 = sqlite3.connect("database2.db")
                cursor2 = database2.cursor()
                self.info.setText("Verbunden (2)")

                #SHIFT 1
                cursor2.execute("SELECT value FROM shift1 WHERE month = ?",[self.current_month])
                self.shift1_values = cursor2.fetchall()
                for i in self.shift1_values:
                    self.shift1_val.append(list(i)[0])
                self.shift1_average = mean(self.shift1_val)

                cursor2.execute("SELECT date FROM shift1 WHERE month = ?",[self.current_month])
                self.shift1_dates = cursor2.fetchall()
                for i in self.shift1_dates:
                    self.shift1_date.append(str(list(i)[0]))

                #SHIFT 2
                cursor2.execute("SELECT value FROM shift2 WHERE month = ?",[self.current_month])
                self.shift2_values = cursor2.fetchall()
                for k in self.shift2_values:
                    self.shift2_val.append(list(k)[0])
                self.shift2_average = mean(self.shift2_val)

                cursor2.execute("SELECT date FROM shift2 WHERE month = ?",[self.current_month])
                self.shift2_dates = cursor2.fetchall()
                for k in self.shift2_dates:
                    self.shift2_date.append(str(list(k)[0]))
                
                #SHIFT 3
                cursor2.execute("SELECT value FROM shift3 WHERE month = ?",[self.current_month])
                self.shift3_values = cursor2.fetchall()
                for l in self.shift3_values:
                    self.shift3_val.append(list(l)[0])
                self.shift3_average = mean(self.shift3_val)
                
                cursor2.execute("SELECT date FROM shift3 WHERE month = ?",[self.current_month])
                self.shift3_dates = cursor2.fetchall()
                for l in self.shift3_dates:
                    self.shift3_date.append(str(list(l)[0]))

                #SHIFT 4
                cursor2.execute("SELECT value FROM shift4 WHERE month = ?",[self.current_month])
                self.shift4_values = cursor2.fetchall()
                for x in self.shift4_values:
                    self.shift4_val.append(list(x)[0])
                self.shift4_average = mean(self.shift4_val)

                cursor2.execute("SELECT date FROM shift4 WHERE month = ?",[self.current_month])
                self.shift4_dates = cursor2.fetchall()
                for x in self.shift4_dates:
                    self.shift4_date.append(str(list(x)[0]))

                #SHIFT 5
                cursor2.execute("SELECT value FROM shift5 WHERE month = ?",[self.current_month])
                self.shift5_values = cursor2.fetchall()
                for y in self.shift5_values:
                    self.shift5_val.append(list(y)[0])
                self.shift5_average = mean(self.shift5_val)

                cursor2.execute("SELECT date FROM shift5 WHERE month = ?",[self.current_month])
                self.shift5_dates = cursor2.fetchall()
                for y in self.shift5_dates:
                    self.shift5_date.append(str(list(y)[0]))

                try:
                    self.shift1_average = mean(self.shift1_val)
                    self.shift2_average = mean(self.shift2_val)
                    self.shift3_average = mean(self.shift3_val)
                    self.shift4_average = mean(self.shift4_val)
                    self.shift5_average = mean(self.shift5_val)
                except StatisticsError:
                    pass

            self.setData()
        except ValueError:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("The month you selected hasn't any data.")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()

    def init_ui(self):

        #LABELS
        self.shift_label = QtWidgets.QLabel("Wählen Sie eine Schicht aus:")
        self.info        = QtWidgets.QLabel("Info...")
        self.value_label = QtWidgets.QLabel("Verhältnis Ist/Soll [%]:")
        self.dateLable   = QtWidgets.QLabel()
        self.months_lb   = QtWidgets.QLabel("Wählen Sie einen Monat aus:")
        self.logo        = QtWidgets.QLabel()
        self.welcome_lb  = QtWidgets.QLabel("Willkomen, Herr Güner.")
        self.about       = QtWidgets.QLabel("ThyssenKrupp AG©\nVersion 2.2 ~ 13/05/2019\nMade by Ethem Güner")
        self.viewLabel   = QtWidgets.QLabel("View of Data")
        self.lastvalue   = QtWidgets.QLabel("\n")
        self.today       = QtWidgets.QLabel()
        
        self.lastvalue.setAlignment(QtCore.Qt.AlignCenter)

        #ViewList
        self.viewList    = QtWidgets.QListWidget()

        #COMBOBOXES
        self.shift_cb    = QtWidgets.QComboBox()
        self.graph_cb    = QtWidgets.QComboBox()
        self.months      = QtWidgets.QComboBox()

        #LINE EDITS.
        self.value       = QtWidgets.QLineEdit()

        #MSGBOX.
        self.msgBox      = QtWidgets.QMessageBox()

        #CALENDAR
        self.cal         = QtWidgets.QCalendarWidget()

        #PUSH BUTTON
        self.edit_button = QtWidgets.QPushButton("Angaben Löschen")
        self.averages_b  = QtWidgets.QPushButton("Monatlicher Durchschnitt")
        self.saveRB      = QtWidgets.QPushButton("Wählen")
        self.createExcel = QtWidgets.QPushButton("Herstellen Excel Akte")
        self.backupButon = QtWidgets.QPushButton("Unterstützung Angabe")

        #RADIO BUTTONS.
        self.drei_rb     = QtWidgets.QRadioButton("Dreiflächenprüfung")
        self.ein_rb      = QtWidgets.QRadioButton("Einflächenprüfung")

        self.cal.setGridVisible(True)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)

        self.shift_cb.addItem("Schicht")
        self.shift_cb.addItems(["Schicht 1", "Schicht 2", "Schicht 3", "Schicht 4", "Schicht 5"])

        self.graph_cb.addItem("Täglich Graph")
        self.graph_cb.addItems(["Graph Schicht 1", "Graph Schicht 2", "Graph Schicht 3", "Graph Schicht 4", "Graph Schicht 5"])

        self.months.addItem("Monat")
        self.months.addItems(["Januar", "Februar", "März", "April", "Mai", "Juni", 
                              "Juli", "August", "September", "Oktober", "November", "Dezember"])
        
        self.logo.setPixmap(QtGui.QPixmap('logo.png'))

        now   = datetime.datetime.now()
        date  = now.strftime("%d/%m/%y")
        self.today.setText("{}".format(date) )

        self.dateLable.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.about.setAlignment(QtCore.Qt.AlignRight)

        ######################################################

        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        
        vbox.addWidget(self.logo)
        vbox.addWidget(self.welcome_lb)
        vbox.addWidget(self.drei_rb)
        vbox.addWidget(self.ein_rb)
        vbox.addWidget(self.months_lb)
        vbox.addWidget(self.months)
        vbox.addWidget(self.saveRB)
        vbox.addWidget(self.shift_label)
        vbox.addWidget(self.shift_cb)
        vbox.addWidget(self.cal)
        vbox.addWidget(self.dateLable)
        vbox2 = QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.today)
        vbox2.addWidget(self.value_label)
        vbox2.addWidget(self.value)
        vbox2.addWidget(self.info)
        vbox2.addWidget(self.graph_cb)
        vbox2.addWidget(self.createExcel)
        vbox2.addWidget(self.averages_b)
        vbox2.addWidget(self.edit_button)
        vbox2.addWidget(self.backupButon)
        vbox2.addWidget(self.viewLabel)
        vbox2.addWidget(self.viewList)
        vbox2.addWidget(self.lastvalue)
        vbox2.addWidget(self.about)

        vbox2.addStretch()

        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)
        self.setLayout(hbox)
        self.show()

        self.value.textChanged.connect(self.valueHolder)
        self.edit_button.clicked.connect(self.goPage2)
        self.averages_b.clicked.connect(self.setAverages)
        self.graph_cb.currentIndexChanged.connect(self.setGraph)
        self.shift_cb.currentIndexChanged.connect(self.viewData)
        self.saveRB.clicked.connect(self.dataPreProcessing)
        self.saveRB.clicked.connect(self.setAverages2)
        self.backupButon.clicked.connect(self.backupProcess)
        self.createExcel.clicked.connect(self.creatingExcelFile)
    
    def viewData(self):

        if self.shift_cb.currentIndex() == 1:
            shift = "shift1"

        elif self.shift_cb.currentIndex() == 2:
            shift = "shift2"

        elif self.shift_cb.currentIndex() == 3:
            shift = "shift3"

        elif self.shift_cb.currentIndex() == 4:
            shift = "shift4"

        elif self.shift_cb.currentIndex() == 5:
            shift = "shift5"

        if self.drei_rb.isChecked() == True:
            database = sqlite3.connect("database.db")
            cursor = database.cursor()

            current_month = self.months.currentText()
            dates  = []
            values = []

            cursor.execute("SELECT date FROM {} WHERE month = ?".format(shift),[current_month])
            temp_dates = cursor.fetchall()
            
            length = len(temp_dates)
            for i in range(0, length):
                date = str(list(temp_dates)[i]).replace("(","").replace("'","").replace(",","").replace(")","") 
                dates.append(date)
            
            cursor.execute("SELECT value FROM {} WHERE month = ?".format(shift),[current_month])
            temp_values = cursor.fetchall()
            
            length = len(temp_values)
            for i in range(0, length):
                value = str(list(temp_values)[i]).replace("(","").replace("'","").replace(",","").replace(")","") 
                values.append(value)
            
            all_data = []

            counter = 0
            length = len(temp_values)
            for i in range(0, length):
                item = "{}  |  {}".format(dates[i], values[i])
                all_data.append(item)

                counter += 1
                if counter == length:
                    self.lastvalue.setText("Zu letzt hinzugefügt:\n{}".format(str(item)) )
                
                

            self.viewList.clear()
            for i in all_data:
                self.viewList.addItem(str(i))
        else:

            database = sqlite3.connect("database2.db")
            cursor = database.cursor()

            current_month = self.months.currentText()
            dates  = []
            values = []

            cursor.execute("SELECT date FROM {} WHERE month = ?".format(shift),[current_month])
            temp_dates = cursor.fetchall()
            
            length = len(temp_dates)
            for i in range(0, length):
                date = str(list(temp_dates)[i]).replace("(","").replace("'","").replace(",","").replace(")","") 
                dates.append(date)
            
            cursor.execute("SELECT value FROM {} WHERE month = ?".format(shift),[current_month])
            temp_values = cursor.fetchall()
            
            length = len(temp_values)
            for i in range(0, length):
                value = str(list(temp_values)[i]).replace("(","").replace("'","").replace(",","").replace(")","") 
                values.append(value)
            
            all_data = []

            counter = 0
            length = len(temp_values)
            for i in range(0, length):
                item = "{}  |  {}".format(dates[i], values[i])
                all_data.append(item)

                counter += 1
                if counter == length:
                    self.lastvalue.setText("Zu letzt hinzugefügt:\n{}".format(str(item)) )
                
                

            self.viewList.clear()
            for i in all_data:
                self.viewList.addItem(str(i))

    def backupProcess(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        save_path = 'Backup'
        dir_name = 'database.db'
        dir_name2 = 'database2.db'
        
        shutil.make_archive("database {}".format(now), 'zip', '.', dir_name)
        shutil.move("database {}.zip".format(now), save_path)

        shutil.make_archive("database2 {}".format(now), 'zip', '.', dir_name2)
        shutil.move("database2 {}.zip".format(now), save_path)

    def setAverages(self):
        plt.close()
        try:
            plt.style.use('ggplot')
            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nMonatlicher Durchschnitt - {}".format(self.current_month))
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nMonatlicher Durchschnitt - {}".format(self.current_month))

            averages = [self.shift1_average, self.shift2_average, self.shift3_average, self.shift4_average, self.shift5_average]

            best_val = [103, 103, 103 , 103, 103]
            index = np.arange(len(averages))
            shifts = ["Schicht 1\n%{:.2f}".format(averages[0]), "Schicht 2\n%{:.2f}".format(averages[1]), "Schicht 3\n%{:.2f}".format(averages[2]), 
                    "Schicht 4\n%{:.2f}".format(averages[3]), "Schicht 5\n%{:.2f}".format(averages[4])]
            plt.bar(shifts, averages, color='r', width=0.5)
            plt.bar(shifts, best_val, color='g', width=0.5)
            plt.xticks(index, shifts, fontsize=12, rotation=0)
            plt.ylabel("%")
            plt.savefig('averages.png', bbox_inches='tight')
            plt.show()
        except:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("Failed. Data couldn't defined. Please check your selections.")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()

    def setAverages2(self):
        try:
            plt.style.use('ggplot')
            if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nMonatlicher Durchschnitt - {}".format(self.current_month))
            elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nMonatlicher Durchschnitt - {}".format(self.current_month))


            averages = [self.shift1_average, self.shift2_average, self.shift3_average, self.shift4_average, self.shift5_average]

            best_val = [103, 103, 103 , 103, 103]
            index = np.arange(len(averages))
            shifts = ["Schicht 1\n%{:.2f}".format(averages[0]), "Schicht 2\n%{:.2f}".format(averages[1]), "Schicht 3\n%{:.2f}".format(averages[2]), 
                        "Schicht 4\n%{:.2f}".format(averages[3]), "Schicht 5\n%{:.2f}".format(averages[4])]
            plt.bar(shifts, averages, color='r', width=0.5)
            plt.bar(shifts, best_val, color='g', width=0.5)
            plt.xticks(index, shifts, fontsize=12, rotation=0)
            plt.ylabel("%")
            plt.savefig('averages.png', bbox_inches='tight')
            plt.close()
        except:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("Failed. Data couldn't defined. Please check your selections.")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()

    def setGraph(self):
        try:

            plt.style.use('seaborn-darkgrid')

            best_val1 = []
            best_val2 = []
            best_val3 = []
            best_val4 = []
            best_val5 = []

            for i in range(0, len(self.shift1_date)):
                best_val1.append(103)

            for i in range(0, len(self.shift2_date)):
                best_val2.append(103)

            for i in range(0, len(self.shift3_date)):
                best_val3.append(103)

            for i in range(0, len(self.shift4_date)):
                best_val4.append(103)

            for i in range(0, len(self.shift5_date)):
                best_val5.append(103)

            if self.graph_cb.currentIndex() == 1:
                plt.close()

                if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 1 - {}".format(self.current_month) )
                elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 1 - {}".format(self.current_month) )
                
                index1 = np.arange(len(self.shift1_date))
                plt.bar(index1, self.shift1_val, color='r', width=0.5)
                plt.bar(index1, best_val1, color='g', width=0.5)
                plt.xticks(index1, self.shift1_date, fontsize=8, rotation=30)
                plt.ylabel("%")

                for i, v in enumerate(self.shift1_val):
                    plt.text(index1[i] - 0.25, v + 0.01, str(v))

                plt.tight_layout()
                plt.show()

            elif self.graph_cb.currentIndex() == 2:
                plt.close()

                if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 2 - {}".format(self.current_month) )
                elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 2 - {}".format(self.current_month) )

                index2 = np.arange(len(self.shift2_date))
                plt.bar(index2, self.shift2_val, color='r', width=0.5)
                plt.bar(index2, best_val2, color='g', width=0.5)
                plt.xticks(index2, self.shift2_date, fontsize=8, rotation=30)
                plt.ylabel("%")

                for i, v in enumerate(self.shift2_val):
                    plt.text(index2[i] - 0.25, v + 0.01, str(v))

                plt.show()

            elif self.graph_cb.currentIndex() == 3:
                plt.close()

                if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 3 - {}".format(self.current_month) )
                elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 3 - {}".format(self.current_month) )

                index3 = np.arange(len(self.shift3_date))
                plt.bar(index3, self.shift3_val, color='r', width=0.5)
                plt.bar(index3, best_val3, color='g', width=0.5)
                plt.xticks(index3, self.shift3_date, fontsize=8, rotation=30)
                plt.ylabel("%")

                for i, v in enumerate(self.shift3_val):
                    plt.text(index3[i] - 0.25, v + 0.01, str(v))

                plt.show()

            elif self.graph_cb.currentIndex() == 4:
                plt.close()

                if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 4 - {}".format(self.current_month) )
                elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 4 - {}".format(self.current_month) )

                index4 = np.arange(len(self.shift4_date))
                plt.bar(index4, self.shift4_val, color='r', width=0.5)
                plt.bar(index4, best_val4, color='g', width=0.5)
                plt.xticks(index4, self.shift4_date, fontsize=8, rotation=30)
                plt.ylabel("%")

                for i, v in enumerate(self.shift4_val):
                    plt.text(index4[i] - 0.25, v + 0.01, str(v))

                plt.show()

            elif self.graph_cb.currentIndex() == 5:
                plt.close()

                if self.drei_rb.isChecked() == True:
                    plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 5 - {}".format(self.current_month) )
                elif self.ein_rb.isChecked() == True:
                    plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 5 - {}".format(self.current_month) )

                index5 = np.arange(len(self.shift5_date))
                plt.bar(index5, self.shift5_val, color='r', width=0.5)
                plt.bar(index5, best_val5, color='g', width=0.5)
                plt.xticks(index5, self.shift5_date, fontsize=8, rotation=30)
                plt.ylabel("%")

                for i, v in enumerate(self.shift5_val):
                    plt.text(index5[i] - 0.25, v + 0.01, str(v))

                plt.show()
        except AttributeError:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("Failed. Data couldn't defined. Please check your selections.")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()
            
    def showDate(self):
        self.date = self.cal.selectedDate()
        self.dateLable.setText(self.date.toString("yyyy-MM-dd"))

    def valueHolder(self):
        try:
            if len(self.value.text()) == 5:
                self.info.setStyleSheet("QLabel  {color: #80FF00;}")
                if self.drei_rb.isChecked() == True:
                    database = sqlite3.connect("database.db")
                    cursor = database.cursor()

                    if self.shift_cb.currentIndex() == 1:
                        cursor.execute("INSERT INTO shift1 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 2:
                        cursor.execute("INSERT INTO shift2 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 3:
                        cursor.execute("INSERT INTO shift3 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 4:
                        cursor.execute("INSERT INTO shift4 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 5:
                        cursor.execute("INSERT INTO shift5 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                elif self.ein_rb.isChecked() == True:
                    database2 = sqlite3.connect("database2.db")
                    cursor2 = database2.cursor()

                    if self.shift_cb.currentIndex() == 1:
                        cursor2.execute("INSERT INTO shift1 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database2.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 2:
                        cursor2.execute("INSERT INTO shift2 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database2.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 3:
                        cursor2.execute("INSERT INTO shift3 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database2.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 4:
                        cursor2.execute("INSERT INTO shift4 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database2.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )

                    elif self.shift_cb.currentIndex() == 5:
                        cursor2.execute("INSERT INTO shift5 VALUES(?,?,?,?)",(self.months.currentText(), self.date.toString("yyyy-MM-dd"), 
                                                                            self.shift_cb.currentText(), float(self.value.text()) ))
                        database2.commit()
                        self.info.setText("{} wurde {}% hinzugefügt.".format(self.shift_cb.currentText(), self.value.text()) )
                self.viewData()
        except ValueError:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("Nur Zahl Eingabe!")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()

    def setData(self):
        self.min_shift1 = min(self.shift1_val)
        self.min_shift2 = min(self.shift2_val)
        self.min_shift3 = min(self.shift3_val)
        self.min_shift4 = min(self.shift4_val)
        self.min_shift5 = min(self.shift5_val)

        val_index1 = self.shift1_val.index(min(self.shift1_val))
        val_index2 = self.shift2_val.index(min(self.shift2_val))
        val_index3 = self.shift3_val.index(min(self.shift3_val))
        val_index4 = self.shift4_val.index(min(self.shift4_val))
        val_index5 = self.shift5_val.index(min(self.shift5_val))


        self.best_day1 = self.shift1_date[val_index1]
        self.best_day2 = self.shift2_date[val_index2]
        self.best_day3 = self.shift3_date[val_index3]
        self.best_day4 = self.shift4_date[val_index4]
        self.best_day5 = self.shift5_date[val_index5]


        print(self.min_shift1, self.min_shift2, self.min_shift3, self.min_shift4, self.min_shift5)

        self.min_values = [self.min_shift1, self.min_shift2, self.min_shift3, self.min_shift4, self.min_shift5]
        self.shifts     = ["Schicht 1", "Schicht 2", "Schicht 3", "Schicht 4", "Schicht 5"]

        for i in range(0,5):
            print("min value of {} = {}".format(self.shifts[i], self.min_values[i]))
        
        self.min_value = min(self.min_values)
        index_value = self.min_values.index(self.min_value)
        print("Best value of the month {} = {}".format(self.shifts[index_value], self.min_value))

        self.averages = [self.shift1_average, self.shift2_average, self.shift3_average, self.shift4_average, self.shift5_average]
        
        self.best_shift_month  = min(self.averages)
        index_average          = self.averages.index(self.best_shift_month)
        self.bestShift         = self.shifts[index_average]
        self.best_value_month  = self.best_shift_month

    def creatingExcelFile(self):
        try:
            workbook   = xlsxwriter.Workbook('schicht_graphs.xlsx')
            worksheet  = workbook.add_worksheet("General")
            worksheet1 = workbook.add_worksheet("Schicht 1")
            worksheet2 = workbook.add_worksheet("Schicht 2")
            worksheet3 = workbook.add_worksheet("Schicht 3")
            worksheet4 = workbook.add_worksheet("Schicht 4")
            worksheet5 = workbook.add_worksheet("Schicht 5")

            cell_format = workbook.add_format()
            cell_format.set_bold()
            cell_format.set_font_color('white')
            cell_format.set_bg_color('#037FD2')
            cell_format.set_font_name('Dubai')
            cell_format.set_align('center')
            cell_format.set_font_size(20)

            cell_format2 = workbook.add_format()
            cell_format2.set_bold()
            cell_format2.set_underline()
            cell_format2.set_align('center')
            cell_format2.set_bg_color('#9F9F9F')
            cell_format2.set_font_color('black')
            cell_format2.set_font_name('Trebuchet MS')
            cell_format2.set_font_size(15)


            cell_format3 = workbook.add_format()
            cell_format3.set_bold()
            cell_format3.set_italic()
            cell_format3.set_font_color('white')
            cell_format3.set_bg_color('#037FD2')
            cell_format3.set_font_name('Trebuchet MS')
            cell_format3.set_font_size(15)

            cell_format4 = workbook.add_format()
            cell_format4.set_bold()
            cell_format4.set_font('red')
            cell_format4.set_align('center')
            cell_format4.set_bg_color('#9F9F9F')
            cell_format4.set_font_name('Trebuchet MS')
            cell_format4.set_font_size(15)

            worksheet.set_column('A:A', 39)
            worksheet.set_column('B:B', 20)
            worksheet.write('A2', '	Monatsdurchschnitt', cell_format)
            worksheet.insert_image('A4', 'averages.png')
            worksheet.write('A28', 'Ziel erreichte Schicht:', cell_format2)
            worksheet.write('A29', self.bestShift, cell_format4)
            worksheet.write('B29', float(self.best_value_month), cell_format3)
            worksheet.write('B28', '%', cell_format2)

            plt.style.use('seaborn-darkgrid')

            best_val1 = []
            best_val2 = []
            best_val3 = []
            best_val4 = []
            best_val5 = []

            for i in range(0, len(self.shift1_date)):
                best_val1.append(103)

            for i in range(0, len(self.shift2_date)):
                best_val2.append(103)

            for i in range(0, len(self.shift3_date)):
                best_val3.append(103)

            for i in range(0, len(self.shift4_date)):
                best_val4.append(103)

            for i in range(0, len(self.shift5_date)):
                best_val5.append(103)


            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 1 - {}".format(self.current_month) )
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 1 - {}".format(self.current_month) )
            
            plt.figure(figsize=(8,6))
            index1 = np.arange(len(self.shift1_date))
            plt.bar(index1, self.shift1_val, color='r', width=0.5)
            plt.bar(index1, best_val1, color='g', width=0.5)
            plt.xticks(index1, self.shift1_date, fontsize=8, rotation=30)
            plt.ylabel("%")

            for i, v in enumerate(self.shift1_val):
                    plt.text(index1[i] - 0.25, v + 0.01, str(v))

            plt.tight_layout()
            plt.savefig('shift1.png', bbox_inches='tight')
            
            plt.close()

            worksheet1.set_column('A:A', 44)
            worksheet1.set_column('B:B', 20)
            worksheet1.write('A2', 'Tageswerte von Schicht 1', cell_format)
            worksheet1.insert_image('A4', 'shift1.png')
            worksheet1.write('A33', 'Bestleistung:', cell_format2)
            worksheet1.write('A34', self.best_day1, cell_format4)
            worksheet1.write('B34', float(self.min_shift1), cell_format3)
            worksheet1.write('B33', '%', cell_format2)

            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 2 - {}".format(self.current_month) )
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 2 - {}".format(self.current_month) )
            
            plt.figure(figsize=(8,6))
            index2 = np.arange(len(self.shift2_date))
            plt.bar(index2, self.shift2_val, color='r', width=0.5)
            plt.bar(index2, best_val2, color='g', width=0.5)
            plt.xticks(index2, self.shift2_date, fontsize=8, rotation=30)
            plt.ylabel("%")

            for i, v in enumerate(self.shift2_val):
                    plt.text(index2[i] - 0.25, v + 0.01, str(v))

            plt.tight_layout()
            plt.savefig('shift2.png', bbox_inches='tight')
            plt.close()

            worksheet2.insert_image('A4', 'shift2.png')
            worksheet2.set_column('A:A', 44)
            worksheet2.set_column('B:B', 20)
            worksheet2.write('A2', 'Tageswerte von Schicht 2', cell_format)
            worksheet2.write('A33', 'Bestleistung:', cell_format2)
            worksheet2.write('A34', self.best_day2, cell_format4)
            worksheet2.write('B34', float(self.min_shift2), cell_format3)
            worksheet2.write('B33', '%', cell_format2)

            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 3 - {}".format(self.current_month) )
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 3 - {}".format(self.current_month) )
            
            plt.figure(figsize=(8,6))
            index3 = np.arange(len(self.shift3_date))
            plt.bar(index3, self.shift3_val, color='r', width=0.5)
            plt.bar(index3, best_val3, color='g', width=0.5)
            plt.xticks(index3, self.shift3_date, fontsize=8, rotation=30)
            plt.ylabel("%")

            for i, v in enumerate(self.shift3_val):
                    plt.text(index3[i] - 0.25, v + 0.01, str(v))

            plt.tight_layout()
            plt.savefig('shift3.png', bbox_inches='tight')
            plt.close()


            worksheet3.insert_image('A4', 'shift3.png')
            worksheet3.set_column('A:A', 44)
            worksheet3.set_column('B:B', 20)
            worksheet3.write('A2', 'Tageswerte von Schicht 3', cell_format)
            worksheet3.write('A33', 'Bestleistung:', cell_format2)
            worksheet3.write('A34', self.best_day3, cell_format4)
            worksheet3.write('B34', float(self.min_shift3), cell_format3)
            worksheet3.write('B33', '%', cell_format2)

            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 4 - {}".format(self.current_month) )
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 4 - {}".format(self.current_month) )

            plt.figure(figsize=(8,6))
            index4 = np.arange(len(self.shift4_date))
            plt.bar(index4, self.shift4_val, color='r', width=0.5)
            plt.bar(index4, best_val4, color='g', width=0.5)
            plt.xticks(index4, self.shift4_date, fontsize=8, rotation=30)
            plt.ylabel("%")

            for i, v in enumerate(self.shift4_val):
                    plt.text(index4[i] - 0.25, v + 0.01, str(v))

            plt.tight_layout()
            plt.savefig('shift4.png', bbox_inches='tight')
            plt.close()

            worksheet4.insert_image('A4', 'shift4.png')
            worksheet4.set_column('A:A', 44)
            worksheet4.set_column('B:B', 20)
            worksheet4.write('A2', 'Tageswerte von Schicht 4', cell_format)
            worksheet4.write('A33', 'Bestleistung:', cell_format2)
            worksheet4.write('A34', self.best_day4, cell_format4)
            worksheet4.write('B34', float(self.min_shift4), cell_format3)
            worksheet4.write('B33', '%', cell_format2)

            if self.drei_rb.isChecked() == True:
                plt.title("Dreiflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 5 - {}".format(self.current_month) )
            elif self.ein_rb.isChecked() == True:
                plt.title("Einflächenprüfung\nVerhältnis Ist/Soll [%] - Schicht 5 - {}".format(self.current_month) )

            plt.figure(figsize=(8,6))
            index5 = np.arange(len(self.shift5_date))
            plt.bar(index5, self.shift5_val, color='r', width=0.5)
            plt.bar(index5, best_val5, color='g', width=0.5)
            plt.xticks(index5, self.shift5_date, fontsize=8, rotation=30)
            plt.ylabel("%")

            for i, v in enumerate(self.shift5_val):
                    plt.text(index5[i] - 0.25, v + 0.01, str(v))

            plt.tight_layout()
            plt.savefig('shift5.png', bbox_inches='tight')
            plt.close()
            
            worksheet5.insert_image('A4', 'shift5.png')
            worksheet5.set_column('A:A', 44)
            worksheet5.set_column('B:B', 20)
            worksheet5.write('A2', 'Tageswerte von Schicht 5', cell_format)
            worksheet5.write('A33', 'Bestleistung:', cell_format2)
            worksheet5.write('A34', self.best_day5, cell_format4)
            worksheet5.write('B34', float(self.min_shift5), cell_format3)
            worksheet5.write('B33', '%', cell_format2)

            workbook.close()
            os.startfile('schicht_graphs.xlsx')

        except AttributeError:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setText("Failed. Data couldn't defined. Please check your selections.")
            self.msgBox.setWindowTitle("Fehler entstanden.")
            self.msgBox.exec_()


    def goPage2(self):
        self.e_page = EditPage()

class EditPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setTheme()
        self.setWindowTitle("Bearbeitung")

    def setTheme(self):
        self.labelFont = QtGui.QFont("Trebuchet MS", 11, QtGui.QFont.Bold)
        self.buttonFont = QtGui.QFont("Trebuchet MS", 12, QtGui.QFont.Light)
        self.cbFont = QtGui.QFont("Trebuchet MS", 9, QtGui.QFont.Light)
        self.listFont = QtGui.QFont("Trebuchet MS", 10, QtGui.QFont.Light)

        self.drei_rb.setFont(self.labelFont)
        self.ein_rb.setFont(self.labelFont)
        self.shift_cb.setFont(self.cbFont)
        self.listWidget.setFont(self.listFont)
        self.deleteButton.setFont(self.buttonFont)

        self.deleteButton.setStyleSheet("QPushButton  {background: #00589E; color: white;}")

    def init_ui(self):
        self.left = 700
        self.top = 200
        self.width = 350
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.shift_cb     = QtWidgets.QComboBox()
        self.listWidget   = QtWidgets.QListWidget()
        self.deleteButton = QtWidgets.QPushButton("LÖSCHEN")
        self.drei_rb      = QtWidgets.QRadioButton("Dreiflächenprüfung")
        self.ein_rb       = QtWidgets.QRadioButton("Einflächenprüfung")
        self.questionBox  = QtWidgets.QMessageBox()

        self.shift_cb.addItem("Schicht")
        self.shift_cb.addItems(["Schicht 1", "Schicht 2", "Schicht 3", "Schicht 4", "Schicht 5"])

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.drei_rb)
        vbox.addWidget(self.ein_rb)
        vbox.addWidget(self.shift_cb)
        vbox.addWidget(self.listWidget)
        vbox.addWidget(self.deleteButton)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)
        self.show()

        self.shift_cb.currentIndexChanged.connect(self.bringData)
        self.listWidget.currentItemChanged.connect(self.defineItem)
        self.deleteButton.clicked.connect(self.deleteItem)

    def bringData(self):
        if self.shift_cb.currentIndex() == 1:
            shft = "shift1"

        elif self.shift_cb.currentIndex() == 2:
            shft = "shift2"

        elif self.shift_cb.currentIndex() == 3:
            shft = "shift3"

        elif self.shift_cb.currentIndex() == 4:
            shft = "shift4"

        elif self.shift_cb.currentIndex() == 5:
            shft = "shift5"

        if self.drei_rb.isChecked() == True:
            database = sqlite3.connect("database.db")
            cursor   = database.cursor()

            self.listWidget.clear()

            list_of_months = []
            list_of_dates  = []
            list_of_shifts = []
            list_of_values = []

            try:
                cursor.execute("SELECT * FROM {}".format(shft))
                self.all_row = cursor.fetchall()
            except UnboundLocalError:
                pass


            for i in self.all_row:
                list_of_months.append(list(i)[0])
                list_of_dates.append(str(list(i)[1]))
                list_of_shifts.append(list(i)[2])
                list_of_values.append(str(list(i)[3]))

            all_data = []
            len_x = len(self.all_row)

            for i in range(0, len_x):
                all_data.append("{}   -   {}   -   {}   -   {}".format(list_of_dates[i], list_of_months[i], list_of_shifts[i], list_of_values[i]))

            for i in all_data:
                self.listWidget.addItems([i])
        
        elif self.ein_rb.isChecked() == True:
            database2 = sqlite3.connect("database2.db")
            cursor   = database2.cursor()

            self.listWidget.clear()

            list_of_months = []
            list_of_dates  = []
            list_of_shifts = []
            list_of_values = []

            try:
                cursor.execute("SELECT * FROM {}".format(shft))
                self.all_row = cursor.fetchall()
            except UnboundLocalError:
                pass
                
            for i in self.all_row:
                list_of_months.append(list(i)[0])
                list_of_dates.append(str(list(i)[1]))
                list_of_shifts.append(list(i)[2])
                list_of_values.append(str(list(i)[3]))

            all_data = []
            len_x = len(self.all_row)

            for i in range(0, len_x):
                all_data.append("{}   -   {}   -   {}   -   {}".format(list_of_dates[i], list_of_months[i], list_of_shifts[i], list_of_values[i]))

            for i in all_data:
                self.listWidget.addItems([i])

    def defineItem(self):
        try:
            item = self.listWidget.currentItem().text()
            self.list_date = item.split(" ")[0]

        except AttributeError:
            pass
            
    def deleteItem(self):

        if self.shift_cb.currentIndex() == 1:
            shft = "shift1"

        elif self.shift_cb.currentIndex() == 2:
            shft = "shift2"

        elif self.shift_cb.currentIndex() == 3:
            shft = "shift3"

        elif self.shift_cb.currentIndex() == 4:
            shft = "shift4"

        elif self.shift_cb.currentIndex() == 5:
            shft = "shift5"

        self.questionMsgBox = QMessageBox.question(self, 'Warning', "Kennzahl wird gelöscht,\nsind Sie sicher das es gelöscht werden soll ?)", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if self.questionMsgBox == QMessageBox.Yes:

            if self.drei_rb.isChecked() == True:
                database = sqlite3.connect("database.db")
                cursor   = database.cursor()

                cursor.execute("DELETE FROM {} WHERE date = ?".format(shft), [self.list_date])
                database.commit()
                self.bringData()
            
            elif self.ein_rb.isChecked() == True:
                database2 = sqlite3.connect("database2.db")
                cursor    = database2.cursor()

                cursor.execute("DELETE FROM {} WHERE date = ?".format(shft), [self.list_date])
                database2.commit()
                self.bringData()
        else:
            pass
    

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.move(500, 150)
window.setFixedSize(700, 700)
app.setStyle("Fusion")
window.setStyleSheet("Window {background: #515050;}")
sys.exit(app.exec_())