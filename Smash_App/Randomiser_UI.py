from PyQt6.QtWidgets import (QPushButton, QLabel, QWidget, QGridLayout, QLineEdit, QSlider)
from PyQt6.QtCore import QTimer, QSize, Qt
from datetime import timedelta

def randomPage(self, screenWidth):
    self.sectionText = "Next Character in: "
    self.time = 60
    self.countdown = self.time
    clock = timedelta(seconds = self.countdown)

    #TITLE
    self.title = QLabel("Character Randomiser")
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
    self.hubButton.clicked.connect(self.goHubPage)
    self.hubButton.clicked.connect(self.stopTimer)
    self.hubButton.setStyleSheet("color: white; background-color: #5d0032;")
    self.hubButton.setFixedSize(80, 80)
    font = self.hubButton.font()
    font.setPointSize(40)
    self.hubButton.setFont(font)

    self.timerButton = QPushButton("Start Randomiser")
    self.timerButton.clicked.connect(self.randomiserTimer)
    self.timerButton.setFixedSize(300, 50)
    self.timerButton.setStyleSheet("color: white; background-color: #5d104d;")
    font = self.timerButton.font()
    font.setPointSize(20)
    self.timerButton.setFont(font)

    self.skipButton = QPushButton("Next")
    self.skipButton.clicked.connect(self.nextCharacter)
    self.skipButton.setFixedSize(100, 50)
    self.skipButton.setStyleSheet("color: white; background-color: #5d104d;")
    font = self.skipButton.font()
    font.setPointSize(20)
    self.skipButton.setFont(font)
    self.skipButton.setEnabled(False)

    self.randomiserSlider = QSlider(Qt.Orientation.Horizontal)      
    self.randomiserSlider.setMinimum(0)
    self.randomiserSlider.setMaximum(60)
    self.randomiserSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
    self.randomiserSlider.setTickInterval(5)
    self.randomiserSlider.setSingleStep(5)
    self.randomiserSlider.setFixedHeight(100)
    #taskTime.setPlaceholderText("Set Ranomiser Countdown Time (minutes)")
    self.randomiserSlider.valueChanged.connect(self.display)

    self.timeSetLabel = QLabel("Time Set: " + str(clock))
    font = self.timeSetLabel.font()
    font.setPointSize(40)
    self.timeSetLabel.setFont(font)
    self.timeSetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    #TIMERS
    self.timer = QTimer()
    self.timer.timeout.connect(self.the_button_was_clicked)

    self.timerCountdown = QTimer()
    self.timerCountdown.timeout.connect(self.timerCharacterCountdownStart)

    #LABELS
    self.label = QLabel("Character: " + self.character)
    font = self.label.font()
    font.setPointSize(40)
    self.label.setFont(font)
    self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.label.setWordWrap(True)

    timeTitle = QLabel("Randomiser Time Limit")
    timeTitle.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-color: #5d0032; border-width: 5px; ")
    timeTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    timeTitle.setFixedHeight(70)
    font = timeTitle.font()
    font.setPointSize(20)
    timeTitle.setFont(font)

    self.labelTimer = QLabel(self.sectionText + str(clock))
    font = self.labelTimer.font()
    font.setPointSize(40)
    self.labelTimer.setFont(font)
    self.labelTimer.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.labelTimer.setWordWrap(True)

    self.button = QPushButton("Give Me a Random Character!")
    self.button.setStyleSheet("color: white; background-color: #5d104d; border-style: inset; border-width: 6px; border-color: #5d0032; border-radius: 40px;")
    font = self.button.font()
    font.setPointSize(30)
    self.button.setFont(font)
    self.button.clicked.connect(self.the_button_was_clicked)
    self.button.setFixedHeight(100)


    layout = QGridLayout()
    layout.setContentsMargins(2,2,2,2)
    layout.setHorizontalSpacing(110)

    layout.addWidget(self.title, 0, 0, 1, 0)
    layout.addWidget(self.hubButton, 0, 0, 1, 0)

    layout.addWidget(self.button, 1, 0, 1, 0)
    layout.addWidget(self.label, 2, 0, 1, 0)

    layout.addWidget(timeTitle, 3, 0, 1, 0)
    layout.addWidget(self.randomiserSlider, 4, 0, 1, 0)     
    layout.addWidget(self.labelTimer, 5, 0, 1, 0)
    
    layout.addWidget(self.bottomBorder, 6, 0, 1, 0)
    layout.addWidget(self.timerButton, 6, 1)
    layout.addWidget(self.skipButton, 6, 2)

    container = QWidget()
    container.setLayout(layout)
    return container
