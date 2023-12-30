from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([]) #сторюємо віконний додаток
from main_window import*
from main_window import main_line

win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)

def answer_click():
    if anser_btn.text() == "ВІдповісти":
        group_box.hide()
        result_box.show()
        anser_btn.setText("Наступне питання")
    else:
        group_box.show()
        result_box.hide()
        anser_btn.setText("Відповісти")



anser_btn.clicked.connect(answer_click)
win.show() #показує вікно
app.exec_() # запускаємо додаток