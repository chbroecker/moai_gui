import sys
from PySide2 import QtCore, QtWidgets, QtGui 
from PySide2.QtWidgets import QGridLayout, QRadioButton, QVBoxLayout, QGroupBox, QTableWidget, QFrame, QSpinBox

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.button_load_warehouse_info = QtWidgets.QPushButton("Load Warehouse information")
        self.button_load_order_info = QtWidgets.QPushButton("Load Order")

        self.warehouse_info = QtWidgets.QTextEdit()
        self.warehouse_info.setReadOnly(True)

        self.warehouse_order = QtWidgets.QTextEdit()
        self.warehouse_order.setReadOnly(True)

        self.createSearchAlgoSelect()
        self.createButtonGroupBox()
        self.createResultGroupBox()

        result_label = QtWidgets.QLabel("Results:")

        main_layout = QGridLayout()
        main_layout.addWidget(self.button_load_warehouse_info, 0, 1)
        main_layout.addWidget(self.button_load_order_info, 0, 2)
        main_layout.addWidget(self.warehouse_info, 1, 1)
        main_layout.addWidget(self.warehouse_order, 1, 2)
        main_layout.addWidget(self.algorithm_select, 2, 1, 1, 2)
        main_layout.addWidget(self.button_list, 3, 1, 2, 1)
        main_layout.addWidget(result_label, 3, 2)
        main_layout.addWidget(self.result_textEdit, 4, 2)
        self.setLayout(main_layout)

        self.button_load_warehouse_info.clicked.connect(self.open_warehouse_info)
        self.button_load_order_info.clicked.connect(lambda:self.open_warehouse_order(self.button_load_order_info))

    def createSearchAlgoSelect(self):
        self.algorithm_select = QGroupBox()

        radioButton1 = QRadioButton("Hill-Climbing")
        radioButton2 = QRadioButton("First-choice Hill-Climbing")
        radioButton3 = QRadioButton("Random Restart")
        radioButton4 = QRadioButton("Simulated Annealing")
        radioButton5 = QRadioButton("Local Beam Search")
        radioButton1.setChecked(True)

        selection_label = QtWidgets.QLabel("Select a search algorithm:")
        num_states_label = QtWidgets.QLabel("Number of States:")
        num_states2_label = QtWidgets.QLabel("Number of States:")

        spinBox = QSpinBox()
        spinBox.setValue(2)

        spinBox2 = QSpinBox()
        spinBox2.setValue(2)

        g_layout = QGridLayout()
        g_layout.addWidget(selection_label, 0, 1)
        g_layout.addWidget(radioButton1, 1, 1)
        g_layout.addWidget(radioButton2, 2, 1)
        g_layout.addWidget(radioButton3, 3, 1)
        g_layout.addWidget(radioButton4, 4, 1)
        g_layout.addWidget(radioButton5, 5, 1)

        g_layout.addWidget(spinBox, 3, 3)
        g_layout.addWidget(spinBox2, 5, 3)

        g_layout.addWidget(num_states_label, 3, 2)
        g_layout.addWidget(num_states2_label, 5, 2)

        self.algorithm_select.setLayout(g_layout)

        self.selected_algorithm = ""
        #radioButton1.clicked.toggled(lambda: self.updateSelectedAlgorithm(radioButton1.text()))
        #radioButton2.clicked.toggled(lambda: self.updateSelectedAlgorithm(radioButton2.text()))
        #radioButton3.clicked.toggled(lambda: self.updateSelectedAlgorithm(radioButton3.text()))
        #radioButton4.clicked.toggled(lambda: self.updateSelectedAlgorithm(radioButton4.text()))
        #radioButton5.clicked.toggled(lambda: self.updateSelectedAlgorithm(radioButton5.text()))

    def updateSelectedAlgorithm(self, algorithm):
        self.selectedAlgorithm = algorithm
        print(self.selectedAlgorithm)

    def createButtonGroupBox(self):
        self.button_compute = QtWidgets.QPushButton("Compute")
        self.button_help = QtWidgets.QPushButton("Help")
        self.button_credits = QtWidgets.QPushButton("Credits")

        self.button_list = QFrame()
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button_compute)
        button_layout.addWidget(self.button_help)
        button_layout.addWidget(self.button_credits)

        self.button_list.setLayout(button_layout)

    def createResultGroupBox(self):
        self.result_textEdit = QtWidgets.QTextEdit()
        self.result_textEdit.setText(self.selected_algorithm)
        #result_textEdit.setReadOnly(True)

    def open_warehouse_info(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        
        try:
            file = open(name, 'r')

            with file:
                text = file.read()
                self.warehouse_info.setText(text)
        except FileNotFoundError:
            pass

    def open_warehouse_order(self, button):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        
        try:
            file = open(name, 'r')

            with file:
                text = file.read()
                self.warehouse_order.setText(text.replace(' ', '\n'))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
