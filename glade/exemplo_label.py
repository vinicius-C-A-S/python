from Pyside6.Qtwidgets import Qapplication, Qlabel
app = Qapplication()

label = Qlabel("Este é um exemplo!")
label.show()

app.exec()