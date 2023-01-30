#import qt core

from PySide6.QtCore import *
from PySide6.QtGui import*
from PySide6.QtWidgets import*

#main window
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        #set initial parameters
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)
        
        #Create Central Widget
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")
        
        #Create Main Layout
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargin(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        #Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
    
        #Content
        self.content = QFrame()
        self.left_menu.setStyleSheet("background-color: 282a36")
    
        #Add Widgets to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        #SET Central Widget
        parent.setCentralWidget(self.central_frame)
