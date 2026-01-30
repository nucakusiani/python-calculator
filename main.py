from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QPushButton, QLineEdit, QGridLayout

app=QApplication([])
mainWindow=QWidget()
mainWindow.setWindowTitle("kalkulator")
mainWindow.resize(400, 400)

textBox=QLineEdit()
grid=QGridLayout()

buttons=['7', '8', '9', '/', '4', '5', '6', '+', '1', '2', '3', '-', '0', '.', '=', '*']
clear=QPushButton("clear")
delete=QPushButton("del")

row=0
col=0
for text in buttons:
    button=QPushButton(text)

    grid.addWidget(button, row, col)
    col+=1
    if col>3:
        col=0
        row+=1


masterlayout=QVBoxLayout()
masterlayout.addWidget(textBox)
masterlayout.addLayout(grid)

buttonRow=QHBoxLayout()
buttonRow.addWidget(clear)
buttonRow.addWidget(delete)

masterlayout.addLayout(buttonRow)

mainWindow.setLayout(masterlayout)



mainWindow.show()
app.exec()










