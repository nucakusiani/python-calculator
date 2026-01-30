from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout
)

app = QApplication([])
mainWindow = QWidget()
mainWindow.setWindowTitle("kalkulator")
mainWindow.resize(400, 400)

textBox = QLineEdit()
textBox.setReadOnly(True)

grid = QGridLayout()
masterlayout = QVBoxLayout()
buttonRow = QHBoxLayout()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '+',
    '1', '2', '3', '-',
    '0', '.', '=', '*'
]

clear = QPushButton("clear")
delete = QPushButton("del")


def button_click():
    button = app.sender()
    text = button.text()

    if text == "=":
        try:
            result = eval(textBox.text())
            textBox.setText(str(result))
        except:
            textBox.setText("error")

    elif text == "clear":
        textBox.clear()

    elif text == "del":
        textBox.setText(textBox.text()[:-1])

    else:
        textBox.setText(textBox.text() + text)


row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)

    col += 1
    if col > 3:
        col = 0
        row += 1

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

buttonRow.addWidget(clear)
buttonRow.addWidget(delete)

masterlayout.addWidget(textBox)
masterlayout.addLayout(grid)
masterlayout.addLayout(buttonRow)

mainWindow.setLayout(masterlayout)
mainWindow.show()

app.exec()




