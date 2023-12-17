from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([]) #сторюємо віконний додаток
from main_window import main_line
win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)
win.show() #показує вікно
app.exec_() # запускаємо додаток