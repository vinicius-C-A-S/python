from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
app = QApplication()

font = QFont()
font.setPointSize(70)
label = QLabel('Este é um exemplo!')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
label.show
botao = QPushButton('botão!')
botao.setFont(font)
botao.show()
app.exec()