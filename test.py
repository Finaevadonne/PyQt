from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel('Привет, мир!')
label.show()

app.exec_()
