from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

menu = QWidget() # створємо вікно

menu.resize(400, 200)
menu.setWindowTitle("Memory Card Menu")

title_lb = QLabel("Статистика")
count_lb = QLabel("Разів відповіли:")
right_lb = QLabel("Правильних відповідей:")
succes_lb = QLabel("Успішність:")
back_btn = QPushButton("Назад")
v_line = QVBoxLayout()
v_line.addWidget(title_lb)
v_line.addWidget(count_lb)
v_line.addWidget(right_lb)
v_line.addWidget(succes_lb)
v_line.addWidget(back_btn)


menu.setLayout(v_line)