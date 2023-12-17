from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QSpinBox, QHBoxLayout, QRadioButton, QButtonGroup,



menu_bth = QPushButton("Меню")
rest_bth = QPushButton("Відпочити")

time_spin = QSpinBox()
time_spin.setValue(3)
time_lb = QLabel('хвилин')


row1 = QHBoxLayout()
row1.addWidget(menu_bth)
row1.addStretch(1)
row1.addWidget(rest_bth)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питання")
bth1 = QRadioButton()
bth2 = QRadioButton()
bth3 = QRadioButton()
bth4 = QRadioButton()

row2 = QHBoxLayout()
radio_group = QButtonGroup
radio_group.addButton(bth1)
radio_group.addButton(bth2)
radio_group.addButton(bth3)
radio_group.addButton(bth4)


main_line = QVBoxLayout()
main_line.addLayout(row1)

