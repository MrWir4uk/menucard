from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QSpinBox, QHBoxLayout, QRadioButton, QButtonGroup



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
bth1 = QRadioButton("Варіант 1")
bth2 = QRadioButton("Варіант 2")
bth3 = QRadioButton("Варіант 3")
bth4 = QRadioButton("Варіант 4")

row2 = QHBoxLayout()
radio_group = QButtonGroup()
radio_group.addButton(bth1)
radio_group.addButton(bth2)
radio_group.addButton(bth3)
radio_group.addButton(bth4)

group_box = QGroupBox("Варіанти перекладу")
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(bth1)
col1.addWidget(bth2)
col2.addWidget(bth3)
col2.addWidget(bth4)

row2.addLayout(col1)
row2.addLayout(col2)

group_box.setLayout(row2)

result_box = QGroupBox("Варіанти перекладу")
result_text = QLabel("правильно")
right_answer_text = ("відповідь")
anser_btn = QPushButton("Відповісти")
resualt_line = QVBoxLayout()
resualt_line.addWidget(result_text)
resualt_line.addWidget(right_answer_text, alignment=Qt.AlignCenter, stretch=2)
result_box.setLayout(resualt_line)
result_box.hide()

main_line = QVBoxLayout()
main_line.addLayout(row1, stretch=1)
main_line.addWidget(question_lb, stretch=2, alignment=Qt.AlignCenter)
main_line.addWidget(group_box, stretch=6)
main_line.addWidget(result_box, stretch=6)
main_line.addWidget(anser_btn,stretch=3)



