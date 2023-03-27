import qt, ctk
from slicer_core import*
from interface.gui.widgets.widgets_core import*
from interface.gui.Functions import WidgetConnection
from interface.gui.Functions import MarkupClass


class PagePlanning(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"PlanningPage")
        planningLayout = qt.QVBoxLayout(self)
        planningLayout.setContentsMargins(0,0,0,0)
        planningLayout.setSpacing(10)
        planningLayout.setAlignment(qt.Qt.AlignCenter)

# Frames
        self.frame1 = qt.QFrame(self)
        self.frame2 = qt.QFrame(self)
        self.frame3 = qt.QFrame(self)
        self.frame4 = qt.QFrame(self)


# Label
    # Select Label
        self.selectLabel = qt.QLabel('Eletrode Selection:')
        self.selectLabel.setStyleSheet('color: white; font-size: 16px;')
    
    # Information Label
        self.infoLabel = qt.QLabel('Electrode information')
        self.infoLabel.setStyleSheet('color: white; font-size: 16px;')
    
    # Eletrode Name
        coordLabel = qt.QLabel('Coordinates table')
        coordLabel.setStyleSheet('color: white; font-size: 16px;')
    
    # Contact Number
        contactNumber = qt.QLabel('Contact numbers:')
        contactNumber.setStyleSheet('color: white; font-size: 14px;')
        self.contactN = qt.QLabel('10')
        self.contactN.setAlignment(qt.Qt.AlignCenter)
        self.contactN.setStyleSheet(f'''QLabel{{border: none; 
                                                background-color: #2a2a2a; 
                                                min-width: 45px; 
                                                min-height: 20px;
                                                border-radius: 10px; 
                                                color: white; 
                                                font-size: 14px;}}''')
    # electrode size
        electrodeSize = qt.QLabel('Electrode size:')
        electrodeSize.setStyleSheet('color: white; font-size: 14px;')
    
    # Contact
        contactLabel = qt.QLabel('Contact') 
        contactLabel.setStyleSheet('color: white; font-size: 14px;')

# Switch Button 
        self.switch = PyToogle()

# Spin Double Box
        # self.size = DoubleSpinBox()
        self.lineSize = DoubleSpinBox()

# ComboBox
        self.selectNode = ComboBox() 

# Check line view
        eye = findPath('eye.svg')
        eyeOff = findPath('eye-off.svg')
        self.viewcheck = qt.QCheckBox(self.frame1)
        self.viewcheck.setStyleSheet(f'''
                                    QCheckBox::indicator{{
                                        border: none;
                                        width:  16px;
                                        height: 16px;
                                        border-radius: 8px;
                                        background-color: rgba(46, 121, 240, 236);
                                        border-image: url({eye});
                                    }}

                                    QCheckBox::indicator::checked{{
                                        border: none;
                                        width: 16px;
                                        height: 16px;
                                        border-radius: 8px;
                                        border-color: rgb(35, 37, 46);
                                        background-color: rgb(135,135,135);
                                        border-image: url({eyeOff});
                                    }}''')

        sizePolicy = qt.QSizePolicy(qt.QSizePolicy.Fixed, qt.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewcheck.sizePolicy.hasHeightForWidth())
        self.viewcheck.setSizePolicy(sizePolicy)

# Line Edit
        self.LineName = qt.QLineEdit('Line Name')
        self.LineName.setAlignment(qt.Qt.AlignCenter)
        self.LineName.setStyleSheet(f'''
                                        QLineEdit{{
                                            border:none;
                                            border-radius: 10px;
                                            background-color: #2a2a2a;
                                            height: 20px;
                                            max-width: 210px;
                                            font: 14px;}}

                                        QLineEdit:focus{{
                                             border: 1px solid #0084d9;}}
                                       ''')   
# Button
        self.RenameButton = Button(text = 'Rename',
                                    height= 30,
                                    font_size = 8,
                                    minimum_width = 40,
                                    text_align='right',
                                    text_color = '#555',
                                    bgc_color = ' #333333',
                                    bgc_hover = '#1a1a1a',
                                    bgc_pressed = '#2a2a2a')
# Tool Button
        self.ToolButton = ToolButton()

#Collapsible Button Electrode
        self.CollapseEletrode = ctk.ctkCollapsibleButton()
        self.CollapseEletrode.text = 'Electrode Selection'
        self.CollapseEletrode.setStyleSheet('''ctkColapsibleButton{
                                                color: white;
                                                font: 14px;
                                                border: 5px;
                                                border-color: black;
                                                height: 20px;
                                                background-color:   #0000FF;}''')
#Collapsible Button Coordinates
        
        self.CollapsableTable = ctk.ctkCollapsibleButton()
        self.CollapsableTable.text = 'Coordinates Table'
        self.CollapsableTable.setStyleSheet('''ctkCollapsibleButton{
                                                color: white;
                                                font: 14px;
                                                border: 5px;
                                                border-color: black;
                                                height: 20px;
                                                background-color: #018df7;}''')

# Table
        self.Table = PyTableWidget()
        self.Table.numberColunmsAndLines(row=10, colunm=4, name = 'Coord')
        sizePolicyT = qt.QSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Fixed)
        self.Table.setSizePolicy(sizePolicyT)
        
        
# Spacer
        spacerE = qt.QSpacerItem(20,20, qt.QSizePolicy.Expanding, qt.QSizePolicy.Minimum)
        spacerM = qt.QSpacerItem(20,20, qt.QSizePolicy.Minimum, qt.QSizePolicy.Minimum)

# LAYOUT
    # Selection Layout
        SelectionLayout = qt.QHBoxLayout()
        SelectionWidgets = [self.selectLabel, self.selectNode, self.viewcheck, self.ToolButton]

    # Name Layout     
        NameLayout = qt.QHBoxLayout()
        NameWidgets = [self.LineName, self.RenameButton]
    
    # Eletrode Information
        numberLayout = qt.QHBoxLayout()
        numberList = [contactNumber, self.contactN]
        sizeLayout = qt.QHBoxLayout()
        sizeList = [electrodeSize, self.lineSize]
    
    # Contacts ON OFF 
        contactLayout = qt.QHBoxLayout()
        contactList = [contactLabel, self.switch]   

    # Top Layout
        topLayout = qt.QVBoxLayout(self.frame1)
        topLayout.addSpacing(10)
        topLayout.addLayout(WidgetConnection.hLayout(widgets=SelectionWidgets, layout=SelectionLayout, spacing=8, id=2))
        topLayout.addLayout(WidgetConnection.hLayout(widgets=NameWidgets, layout=NameLayout, space=spacerE, id=0))
        topLayout.addSpacing(10)
        topLayout.addWidget(self.infoLabel)
        topLayout.addWidget(self.CollapseEletrode) 
        
    # Frame inside Collpse Top Button
        self.frame3Layout = qt.QVBoxLayout(self.frame3)
        self.frame3Layout.addSpacing(8)
        self.frame3Layout.addLayout(WidgetConnection.hLayout(widgets=contactList, layout=contactLayout, space=spacerE))
        self.frame3Layout.addSpacing(5)
        self.frame3Layout.addLayout(WidgetConnection.hLayout(widgets=numberList, layout=numberLayout, space=spacerE))
        self.frame3Layout.addSpacing(5)
        self.frame3Layout.addLayout(WidgetConnection.hLayout(widgets=sizeList, layout=sizeLayout, space=spacerE))
       
    # Collapseble Layout
        self.CollapsebleLayout = qt.QVBoxLayout(self.CollapseEletrode)
        self.CollapsebleLayout.setContentsMargins(0,0,0,0)
        self.CollapsebleLayout.addWidget(self.frame3)
        
    # Low Layout
        lowLayout = qt.QVBoxLayout(self.frame2)
        lowLayout.addWidget(self.CollapsableTable)
        
    #Frame inside Collpse Low Button
        self.frame4Layout = qt.QVBoxLayout(self.frame4)
        self.frame4Layout.addWidget(coordLabel)
        tableLayout = qt.QHBoxLayout()
        tableLayout.addWidget(self.Table)
        tableLayout.setAlignment(qt.Qt.AlignCenter)
        self.frame4Layout.addLayout(tableLayout)
        
        
    # MainLayout
        planningLayout.addWidget(self.frame1)
        planningLayout.setSpacing(20)
        planningLayout.addWidget(self.frame2)
        planningLayout.addSpacerItem(qt.QSpacerItem(20,20, qt.QSizePolicy.Minimum, qt.QSizePolicy.Expanding))
    
        
    # # Markup object
    #     self.functions = MarkupClass.Markup(self.selectNode, 
    #                                 self.selectLabel, 
    #                                 self.ToolButton, 
    #                                 self.viewcheck, 
    #                                 self.lineSize,
    #                                 self.Table,
    #                                 self.switch)

    
    # # Connection
    #     self.connection = WidgetConnection.ConnectionUI(self.selectNode, self.selectLabel, self.ToolButton, 
    #                                                     self.viewcheck, self.RenameButton, self.lineSize, 
    #                                                     self.Table, self.switch, self.functions)
    
