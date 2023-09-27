from PyQt6.QtWidgets import (QPushButton, QLabel, QWidget, QGridLayout, QLineEdit)
from PyQt6.QtCore import QTimer, QSize, Qt
from Smash_App import File as f
from datetime import timedelta

def trainingPage(self):
    self.time = self.time
    self.countdown = self.time
    self.count = 0
    self.countTarget = 10
    self.iList = 0
    self.nList = self.trainingList
    self.cList = self.trainingCountList

    self.sectionText = "Next Task in: "
    self.sectionTaskText = "Task: " 
    self.sectionCountText = "Count"

    #TITLE
    self.title = QLabel("Training Mode")
    self.title.setStyleSheet("color: white; background-color: #5d0032;")
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    font = self.title.font()
    font.setPointSize(30)
    self.title.setFont(font)
    self.title.setFixedHeight(100)

    #BOTTOM Section
    self.bottomBorder = QLabel("")
    self.bottomBorder.setStyleSheet("background-color: #5d0032;")
    self.bottomBorder.setFixedSize(720, 100)
    self.bottomBorder.setAlignment(Qt.AlignmentFlag.AlignLeft)

    #BUTTONS
    self.hubButton = QPushButton("<")
    self.hubButton.clicked.connect(self.goSetupPage)
    self.hubButton.clicked.connect(self.stopTimer)
    self.hubButton.setStyleSheet("color: white; background-color: #5d0032;")
    self.hubButton.setFixedSize(80, 80)
    font = self.hubButton.font()
    font.setPointSize(40)
    self.hubButton.setFont(font)

    self.timerButton = QPushButton("Start Training")
    self.timerButton.clicked.connect(self.taskTimer)
    self.timerButton.setFixedSize(300, 50)
    self.timerButton.setStyleSheet("color: white; background-color: #5d104d;")
    font = self.timerButton.font()
    font.setPointSize(20)
    self.timerButton.setFont(font)
    
    self.skipButton = QPushButton("Skip")
    self.skipButton.clicked.connect(self.nextPrompt)
    self.skipButton.setFixedSize(100, 50)
    self.skipButton.setStyleSheet("color: white; background-color: #5d104d;")
    font = self.skipButton.font()
    font.setPointSize(20)
    self.skipButton.setFont(font)

    #Test Button
    self.promptButton = QPushButton("Test")
    self.promptButton.clicked.connect(self.getPrompt)

    self.countButton = QPushButton("Count")
    self.countButton.clicked.connect(self.countIncrease)
    self.countButton.setFixedHeight(80)
    font = self.countButton.font()
    font.setPointSize(40)
    self.countButton.setFont(font)
    self.countButton.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-width: 6px; border-color: #5d0032; border-radius: 40px;")

    #TIMERS
    self.timer = QTimer()
    self.timer.timeout.connect(self.getPrompt)

    self.timerCountdown = QTimer()
    self.timerCountdown.timeout.connect(self.timerCountdownStart)

    #LABELS
    clock = timedelta(seconds = self.countdown)
    self.labelTimer = QLabel("Next Task in: " + str(clock))
    font = self.labelTimer.font()
    font.setPointSize(50)
    self.labelTimer.setFont(font)
    self.labelTimer.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelTimer.setWordWrap(True)

    self.label = QLabel(self.sectionTaskText)
    font = self.label.font()
    font.setPointSize(50)
    self.label.setFont(font)
    self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.label.setWordWrap(True)

    #LAYOUT
    self.layout2 = QGridLayout()
    self.layout2.setContentsMargins(2,2,2,2)
    self.layout2.setHorizontalSpacing(110)

    self.layout2.addWidget(self.title, 0, 0, 1, 0)
    self.layout2.addWidget(self.countButton, 3, 0, 1, 0)

    #self.layout2.addWidget(self.promptButton, 1, 0, 1, 0)

    self.layout2.addWidget(self.labelTimer, 5, 0, 1, 0)
    self.layout2.addWidget(self.label, 2, 0, 1, 0)

    self.layout2.addWidget(self.hubButton, 0, 0, 1, 0)    

    self.layout2.addWidget(self.bottomBorder, 7, 0, 1, 0)    
    self.layout2.addWidget(self.timerButton, 7, 1)
    self.layout2.addWidget(self.skipButton, 7, 2)

    #self.layout2.addWidget(self.promptAdd, 8, 0)

    self.skipButton.setEnabled(False)

    self.container2 = QWidget()
    self.container2.setLayout(self.layout2)
    return self.container2


