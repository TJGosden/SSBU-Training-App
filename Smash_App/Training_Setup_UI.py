from tkinter import BOTTOM
from PyQt6.QtWidgets import (QPushButton, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QListWidget, QTreeWidget, QTreeWidgetItem )
from PyQt6.QtCore import QTimer, QSize, Qt

from Smash_App import File as f
from datetime import timedelta

def setupPage(self):
    self.newPrompt = ""
    self.newCount = ""

    #TITLE
    title = QLabel("Training Mode Setup")
    title.setStyleSheet("color: white; background-color: #5d0032;")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    font = title.font()
    font.setPointSize(30)
    title.setFont(font)
    title.setFixedHeight(100)

    #PAGE BUTTONS
    hubButton = QPushButton("<")
    hubButton.clicked.connect(self.goHubPage)
    hubButton.setStyleSheet("color: white; background-color: #5d0032;")
    hubButton.setFixedSize(80, 80)
    font = hubButton.font()
    font.setPointSize(40)
    hubButton.setFont(font)
    
    toTraining = QPushButton("Finish Setup")
    toTraining.clicked.connect(self.goTrainingPage)
    toTraining.setStyleSheet("color: white; background-color: #5d104d;")
    toTraining.setFixedSize(300, 50)
    font = toTraining.font()
    font.setPointSize(20)
    toTraining.setFont(font)

    self.noTask = QLabel("Select at least one Task")
    font = self.noTask.font()
    font.setPointSize(30)
    self.noTask.setFont(font)
    self.noTask.setFixedHeight(100)

    #SPACING WIDGETS
    proxyButton = QPushButton("")    
    proxyButton.setFixedSize(100, 80)
    proxyButton.setStyleSheet("color: white; background-color: #f0f0f0; border-style: inset; border-width: 0px;")

    proxyButton2 = QPushButton("")    
    proxyButton2.setFixedSize(100, 50)
    proxyButton2.setStyleSheet("color: white; background-color: #5d0032; border-style: inset; border-width: 0px;")
    
    proxyButton3 = QPushButton("")    
    proxyButton3.setFixedSize(150, 50)
    proxyButton3.setStyleSheet("color: white; background-color: #f0f0f0; border-style: inset; border-width: 0px;")

    #SET TIME
    timeTitle = QLabel("Task Time Limit")
    timeTitle.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-color: #5d0032; border-width: 5px; ")
    timeTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    timeTitle.setFixedHeight(70)
    font = timeTitle.font()
    font.setPointSize(20)
    timeTitle.setFont(font)

    timeLabel = QLabel("  Task Duration (mins)")
    font = timeLabel.font()
    font.setPointSize(20)
    timeLabel.setFont(font)

    clock = timedelta(seconds = self.time)
    self.timeSetLabel = QLabel("Time Set: " + str(clock))
    font = self.timeSetLabel.font()
    font.setPointSize(40)
    self.timeSetLabel.setFont(font)
    self.timeSetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    taskTime = QLineEdit()       
    taskTime.setMaxLength(10)
    taskTime.setFixedSize(350, 50)
    taskTime.setPlaceholderText("Enter Task Time Limit in minutes")
    taskTime.textEdited.connect(self.return_pressed)
    taskTime.setInputMask('0000000000000000000000;_')

    #LIST INPUT
    self.list = QTreeWidget()
    self.list.setColumnCount(3)
    self.list.setHeaderLabels(['Selected Tasks','Training Tasks', 'Reps'])
    self.listEntry = f.File.search_list(self, "training.txt")
    self.listCount = f.File.search_list(self, "count.txt")
    for i in range(len(self.listEntry)):
            item=QTreeWidgetItem()
            item.setCheckState(0,Qt.CheckState(False))
            item.setText(1, self.listEntry[i])
            item.setText(2, self.listCount[i])
            #item.setData(2, Qt.UserRole, id(item) )
            #item.setText(2, str(id(item) ) )
            self.list.addTopLevelItem(item)
    #listButton.clicked.connect(self.goListPage)
        
    #self.list.addItems(self.listEntry)
    #self.list.setFixedHeight(300)

    listTitle = QLabel("Training Task List")
    listTitle.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-color: #5d0032; border-width: 5px; ")
    listTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    listTitle.setFixedHeight(70)
    font = listTitle.font()
    font.setPointSize(20)
    listTitle.setFont(font)

    listLabel = QLabel("  Enter New Task")
    listLabel.setFixedHeight(70)
    font = listLabel.font()
    font.setPointSize(20)
    listLabel.setFont(font)

    listAdd = QLineEdit()       
    listAdd.setMaxLength(60)
    listAdd.setFixedSize(350, 50)
    listAdd.setPlaceholderText("Enter New Training Task")
    listAdd.textEdited.connect(self.getNewPrompt)

    countAdd = QLineEdit()       
    countAdd.setMaxLength(3)
    countAdd.setFixedSize(100, 50)
    countAdd.setPlaceholderText("  Number of Reps")
    countAdd.textEdited.connect(self.getCount)
    countAdd.setInputMask('00;_')
    
    listAddPrompt = QPushButton("Add")
    listAddPrompt.clicked.connect(self.addPrompt)
    listAddPrompt.setStyleSheet("color: white; background-color: grey;")
    listAddPrompt.setFixedHeight(30)
    font = listAddPrompt.font()
    font.setPointSize(15)
    listAddPrompt.setFont(font)

    listRemovePrompt = QPushButton("Remove Selected")
    listRemovePrompt.clicked.connect(self.removePrompt)
    listRemovePrompt.setStyleSheet("color: white; background-color: grey;")
    listRemovePrompt.setFixedHeight(30)
    font = listRemovePrompt.font()
    font.setPointSize(15)
    listRemovePrompt.setFont(font)

    #Bottom Section Color
    bottomBorder = QLabel("")
    bottomBorder.setStyleSheet("background-color: #5d0032;")
    bottomBorder.setFixedHeight(100)
    bottomBorder.setAlignment(Qt.AlignmentFlag.AlignLeft)

    #LAYOUT
    layout = QGridLayout()
    layout.setContentsMargins(2,2,2,2)
    layout.setHorizontalSpacing(110)
    
    #SET TIME LAYOUT
    layoutTaskTime = QHBoxLayout()
    
    layoutTaskTime.addWidget(timeLabel, 0)
    layoutTaskTime.addWidget(taskTime, 1)
    layoutTaskTime.addWidget(proxyButton, 2)

    #NEW PROMPT LAYOUT
    layoutPromptList = QHBoxLayout()
    layoutPromptList.setSpacing(40)
    layoutPromptList.addWidget(listLabel, 0)
    layoutPromptList.addWidget(listAdd, 1)
    layoutPromptList.addWidget(countAdd, 2)    
    
    #SET LAYOUTS
    layout.addWidget(title, 0, 0, 1, 0)
    for n, widgets in enumerate([hubButton, listTitle]):
        layout.addWidget(widgets, n, 0, 1, 0)

    layout.addLayout(layoutPromptList, 2, 0, 1, 0)
    layout.addWidget(listAddPrompt, 3, 0, 1, 0)    
    layout.addWidget(self.list, 4, 0, 1, 0)
    layout.addWidget(listRemovePrompt, 5, 0, 1, 0)

    layout.addWidget(timeTitle, 6, 0, 1, 0)
    layout.addLayout(layoutTaskTime, 7, 0, 1, 0)
    layout.addWidget(self.timeSetLabel, 8, 0, 1, 0)

    layout.addWidget(bottomBorder, 9, 0, 1, 0)
    layout.addWidget(toTraining, 9, 1)
    layout.addWidget(proxyButton2, 9, 2)  

    container = QWidget()
    container.setLayout(layout)
    return container


