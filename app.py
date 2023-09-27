import sys
from tkinter import CENTER
from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QPushButton, QLabel, 
        QVBoxLayout, QMenu, QWidget, QGridLayout, QListWidget, QSizePolicy,
        QLineEdit, QTreeWidgetItem, QTreeWidget
    )
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import QTimer, QDateTime, QSize, Qt
from PyQt5.uic import loadUi
import random 
from datetime import timedelta
from Smash_App import Smash_Randomiser as sr
from Smash_App import File as f
from Smash_App import Randomiser_UI as uiR
from Smash_App import Training_UI as uiT
from Smash_App import Training_Setup_UI as uiS

screenWidth = 720

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Smash Training App")

        self.character = ""
        self.sectionText = ""

        self.timer = QTimer()
        self.timerCountdown = QTimer()

        self.time = 10
        self.countdown = self.time
        self.timerBool = False

        self.entry = ""
        self.trainingList = []
        self.trainingCountList = []

        self.setFixedSize(QSize(screenWidth, 1000))

        Initialise = self.hubPage()

        # Set the central widget of the Window.
        self.setCentralWidget(Initialise)        

    #PAGE INITIALISERS
    def goHubPage(self):
        self.hubPage()
        self.setCentralWidget(self.containerHub)

    def goRandomPage(self):
        container = uiR.randomPage(self, screenWidth)
        self.setCentralWidget(container)        

    def goTrainingPage(self):        
        self.trainingList = []
        self.trainingCountList = []
        self.getCheckedPrompts()            
        print(self.trainingList)
        print(self.trainingCountList)
        if(self.trainingList != []):
            uiT.trainingPage(self)
            self.setCentralWidget(self.container2)
        else:
            self.noTask.show()
            print("Select at least one Task")

    def goSetupPage(self):
        self.stopTimer()
        self.countdown = self.time
        container = uiS.setupPage(self)
        self.setCentralWidget(container)
        
    def goListPage(self):
        self.listPage()
        self.listContainer.show()
    
    #FUNCTIONS
    def setClock(self):
        self.countdown = self.time
        clock = timedelta(seconds = self.countdown)
        self.labelTimer.setText(self.sectionText + str(clock))

    def display(self):
        print(self.sender().value())
        self.time = self.sender().value() * 60
        self.setClock()
        #self.label.adjustSize()  # Expands label size as numbers get larger

    def the_button_was_clicked(self):
        self.character = sr.Randomiser()
        self.label.setText("Character: " + self.character)
        self.setClock()

    def nextCharacter(self):        
        self.stopTimer()
        self.setClock()
        self.randomiserTimer()
        self.the_button_was_clicked()

    def return_pressed(self, s):
        self.time = int(s) * 60        
        clock = timedelta(seconds = self.time)
        self.timeSetLabel.setText("Time Set: " + str(clock))
        print(s + " minutes")
        
    def timerCountdownStart(self):        
        self.countdown = self.countdown - 1
        if (self.countdown <= 1 and self.count >= int(self.countTarget)):
            self.countdown = self.time
            self.timer.start()
            self.timerCountdown.stop()
            self.timerCountdown.start()
            self.countButton.setText(self.sectionCountText)
            self.count = 0
            self.getPrompt()
        elif(self.count != self.countTarget and self.countdown == 1):
            self.timer.stop()            

        print(self.countdown)
        clock = timedelta(seconds = self.countdown)
        if(self.countdown > 0):
            self.labelTimer.setText(self.sectionText + str(clock))
        else:
            self.labelTimer.setText(self.sectionText + str(self.countdown))

    def timerCharacterCountdownStart(self):        
        self.countdown = self.countdown - 1 
        print(self.countdown)
        clock = timedelta(seconds = self.countdown)
        if(self.countdown > 0):
            self.labelTimer.setText(self.sectionText + str(clock))
        else:
            self.labelTimer.setText(self.sectionText + str(clock))
            self.countdown = self.time

    def randomiserTimer(self):
        if(self.character == ""):            
            self.the_button_was_clicked()
            #self.skipButton.setEnabled(True)

        if (self.timerBool == False):            
            self.startTimer()
            self.button.setEnabled(False)
            self.skipButton.setEnabled(True)
            self.randomiserSlider.hide()
        else:            
            self.stopTimer()
            self.button.setEnabled(True)
            self.skipButton.setEnabled(False)
            self.randomiserSlider.show()
            self.timerButton.setText("Play")


    def taskTimer(self):
        if(self.iList == 0):            
            self.getPrompt()
            self.skipButton.setEnabled(True)

        if(self.iList == len(self.nList)):
            self.iList = 0
            self.stopTimer()
            self.countdown = self.time
            self.setClock()
            self.timerButton.setText("Start Training")
        else:
            if (self.timerBool == False):            
                self.startTimer()                
            else:            
                self.stopTimer()
                self.timerButton.setText("Play")
                

    def startTimer(self):
        self.timer.start(self.time * 1000)
        self.timerCountdown.start(1000)
        self.timerBool = True
        self.timerButton.setText("Pause")

    def stopTimer(self):
        self.timer.stop()
        self.timerCountdown.stop()
        #self.countdown = self.time
        self.timerBool = False

    def countIncrease(self):
        self.count = self.count + 1
        self.countButton.setText("Count: " + str(self.count))
    
    #PROMPT FUCNTIONS
    def getPrompt(self):
        if (self.iList < len(self.nList)):
            #Get item from prompt list         
            self.entry = self.nList[self.iList]
            self.countTarget = self.cList[self.iList]
            print(self.entry)
            print(self.countTarget)
            #"/n2" at the end of some entries, find a way to remove
            self.label.setText(self.sectionTaskText + str(self.countTarget) + " " + self.entry)
            self.countButton.setText(self.sectionCountText)
            self.count = 0
            self.iList = self.iList + 1
            print(self.iList)
        
        #RESTART Timer
        if(self.iList == len(self.nList)):
            self.timerButton.setText("Restart")
            self.skipButton.setEnabled(False)
    
    def getNewPrompt(self, s):
        self.newPrompt = s

    def getCount(self, s):
        self.newCount = s

    def addPrompt(self):
        if (self.newPrompt != ""):
            item = QTreeWidgetItem()
            if(self.newCount == ""):
                insertCount = "10" #defaultCount
            else:
                insertCount = str(self.newCount)
            insertPrompt = self.newPrompt            
            item.setCheckState(0, Qt.CheckState(False))
            item.setText(1, insertPrompt)
            item.setText(2, insertCount)
            self.list.addTopLevelItem(item)

            print (self.newPrompt)
            f.File.add_to_file(self.newPrompt, "training.txt")
            f.File.add_to_file(insertCount, "count.txt")
        else:
            print("No Task Entered")

    def removePrompt(self):
        listItems = self.list.selectedItems()
        if not listItems: return   
        for item in listItems:
            itemIndex=self.list.indexOfTopLevelItem(item)
            self.list.takeTopLevelItem(itemIndex)
        print ('Number of items remaining', self.list.topLevelItemCount())
        #print(item.checkState(0))
        #print(itemIndex)
        f.File.remove_from_file(self, itemIndex, "training.txt")
        f.File.remove_from_file(self, itemIndex, "count.txt")

    def nextPrompt(self):        
        self.stopTimer()
        self.countdown = self.time
        self.taskTimer()
        self.getPrompt()

    def getCheckedPrompts(self):
        self.listEntry = f.File.search_list(self, "training.txt")
        self.listCount = f.File.search_list(self, "count.txt")
        for i in range(self.list.topLevelItemCount()):
            item = self.list.topLevelItem(i)
            #print (item.checkState(0))
            if(item.checkState(0) == Qt.CheckState.Checked):                
                self.trainingList += [self.listEntry[i]]
                self.trainingCountList += [self.listCount[i]]
    
    #PAGES
    def hubPage(self):
        self.title = QLabel("SSBU Trainer")
        self.title.setStyleSheet("QLabel {background-color: #5d0032;}")
        self.title.setStyleSheet("color: white; background-color: #5d0032;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.title.font()
        font.setPointSize(30)
        self.title.setFont(font)

        self.toRandomiser = QPushButton("Randomiser")
        self.toRandomiser.clicked.connect(self.goRandomPage)
        self.toRandomiser.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-color: #5d0032; border-width: 8px; ")
        font = self.toRandomiser.font()
        font.setPointSize(40)
        self.toRandomiser.setFont(font)

        self.toTraining = QPushButton("Training")
        self.toTraining.clicked.connect(self.goSetupPage)
        self.toTraining.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-color: #5d0032; border-width: 8px; ")
        font = self.toTraining.font()
        font.setPointSize(40)
        self.toTraining.setFont(font)

        self.toRandomiser.setFixedHeight(900)
        self.toTraining.setFixedHeight(900)          

        layout = QGridLayout()
        layout.setContentsMargins(2,2,2,2)
        layout.addWidget(self.title, 0, 0, 1, 2)
        layout.addWidget(self.toTraining, 1, 0)
        layout.addWidget(self.toRandomiser, 1, 1)

        self.containerHub = QWidget()
        self.containerHub.setLayout(layout)
        return self.containerHub
          
    def listPage(self):
        self.list = QListWidget()        
        self.listEntry = f.File.search_list(self)
        self.list.addItems(self.listEntry)

        self.listBackButton = QPushButton("Back")
        self.listBackButton.clicked.connect(self.goTrainingPage)

        self.listLayout = QGridLayout()
        self.listLayout.addWidget(self.list, 0, 0)
       #self.listLayout.addWidget(self.listBackButton, 1, 0)

        self.listContainer = QWidget()
        self.listContainer.setLayout(self.listLayout)
        return self.listContainer



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()