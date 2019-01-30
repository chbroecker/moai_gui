import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui 
from PySide2.QtWidgets import QGridLayout, QRadioButton, QVBoxLayout, QGroupBox, QTableWidget, QFrame

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.button2 = QtWidgets.QPushButton("Load Warehouse information")
        self.button3 = QtWidgets.QPushButton("Load Order")
        self.button_compute = QtWidgets.QPushButton("Compute")
        self.button_help = QtWidgets.QPushButton("Help")
        self.button_credits = QtWidgets.QPushButton("Credits")

        self.text = QtWidgets.QLabel("Select a Search Algorithm:")
        self.result_label = QtWidgets.QLabel("PSUs needed:")

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setReadOnly(True)

        self.textEdit2 = QtWidgets.QTextEdit()
        self.textEdit2.setReadOnly(True)

        main_layout = QGridLayout()
        main_layout.addWidget(self.button2, 0, 1)
        main_layout.addWidget(self.button3, 0, 2)
        main_layout.addWidget(self.text, 0, 3)
        main_layout.addWidget(self.textEdit, 1, 1)
        main_layout.addWidget(self.textEdit2, 1, 2)
        main_layout.addWidget(self.result_label, 2, 3)

        radioButton1 = QRadioButton("Hill-Climbing")
        radioButton2 = QRadioButton("First-choice Hill-Climbing")
        radioButton3 = QRadioButton("Random Restart")
        radioButton4 = QRadioButton("Simulated Annealing")
        radioButton5 = QRadioButton("Local Beam Search")
        radioButton1.setChecked(True)

        radio_list = QGroupBox()
        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(radioButton4)
        layout.addWidget(radioButton5)
        radio_list.setLayout(layout)

        main_layout.addWidget(radio_list, 1, 3)

        button_list = QFrame()
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button_compute)
        button_layout.addWidget(self.button_help)
        button_layout.addWidget(self.button_credits)
        button_list.setLayout(button_layout)

        main_layout.addWidget(button_list, 3, 1)

        dummy_label = QtWidgets.QLabel("Results:")
        main_layout.addWidget(dummy_label, 2, 2)

        result_list = QGroupBox()
        result_layout = QVBoxLayout()
        num_psus_title_label = QtWidgets.QLabel("Number of PSUs used:")
        num_psus_label = QtWidgets.QLabel("2")
        num_psus_label.setWordWrap(True);
        num_psus_label.setAlignment(QtCore.Qt.AlignCenter)
        algo_used_title_label = QtWidgets.QLabel("Search algorithm used:")
        algo_used_label = QtWidgets.QLabel("Random-restart")
        algo_used_label.setWordWrap(True);
        algo_used_label.setAlignment(QtCore.Qt.AlignCenter)
        result_layout.addWidget(num_psus_title_label)
        result_layout.addWidget(num_psus_label)
        result_layout.addWidget(algo_used_title_label)
        result_layout.addWidget(algo_used_label)
        result_list.setLayout(result_layout)

        main_layout.addWidget(result_list, 3, 2)

        result_textEdit = QtWidgets.QTextEdit()
        #result_textEdit.setReadOnly(True)

        radioButton1.clicked.connect(lambda: result_textEdit.setText(radioButton2.text()))

        main_layout.addWidget(result_textEdit, 3, 3)

        self.setLayout(main_layout)

        self.button2.clicked.connect(self.open_file)
        self.button3.clicked.connect(lambda:self.open_file2(self.button3))

        self.dummy_open()
        self.dummy_open2()

    def dummy_open(self):
        file = open('/Users/chbroecker/projects/moai_gui/data/warehouseinfo.txt', 'r')

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def dummy_open2(self):
        file = open('/Users/chbroecker/projects/moai_gui/data/order.txt', 'r')

        with file:
            text = file.read()
            self.textEdit2.setText(text)

    def open_file(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        
        file = open(name, 'r')

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def open_file2(self, button):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        
        print(button.text())
        file = open(name, 'r')

        with file:
            text = file.read()
            self.textEdit2.setText(text)

    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
