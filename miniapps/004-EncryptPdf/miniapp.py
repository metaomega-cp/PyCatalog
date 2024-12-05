from PyQt6.QtWidgets import QFileDialog

import miniapps.abstract_miniapp

import os
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore

import PyPDF2


folder_path = os.path.dirname(__file__)

class MiniApp(miniapps.abstract_miniapp.AbstractMiniApp):
    def __init__(self):
        self.ui = None

    def get_ui(self):
        self.ui= PyQt6.QtWidgets.QWidget()
        layout = PyQt6.QtWidgets.QVBoxLayout()
        self.ui.setLayout(layout)

        self.formLayout = PyQt6.QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.label_path = PyQt6.QtWidgets.QLabel()
        select_file_button = PyQt6.QtWidgets.QPushButton()
        select_file_button.setText("Select File")
        select_file_button.setFixedSize(300,20)
        select_file_button.clicked.connect(lambda: self.select_file())
        self.formLayout.addRow("PDF to Encrypt:", self.label_path)
        self.formLayout.addRow(select_file_button)

        self.password = PyQt6.QtWidgets.QLineEdit()
        self.password.textChanged.connect(lambda: self.updateSubmitButton())
        self.formLayout.addRow("Password:", self.password)

        self.outputfile = PyQt6.QtWidgets.QLabel()
        self.formLayout.addRow("Output File:", self.outputfile)

        self.submitButton = PyQt6.QtWidgets.QPushButton("Submit")
        self.submitButton.setEnabled(False)
        self.submitButton.clicked.connect(lambda:self.on_button_clicked())
        self.formLayout.addRow("", self.submitButton)

        self.feedback = PyQt6.QtWidgets.QLabel()
        self.formLayout.addRow(self.feedback)


        widget1 = PyQt6.QtWidgets.QWidget()
        widget1.setLayout(self.formLayout)
        layout.addWidget(widget1)

        self.widget2 = PyQt6.QtWidgets.QWidget()
        layout.addWidget(self.widget2)

        return self.ui

    def select_file(self):
        fname = PyQt6.QtWidgets.QFileDialog.getOpenFileName(None, "Open PDF", "", "Pdf (*.pdf)")
        if fname[0]:
            self.label_path.setText(fname[0])

    def updateSubmitButton(self):
        self.submitButton.setEnabled(len(self.password.text()) != 0 and os.path.exists(self.label_path.text()))
        self.outputfile.setText(self.label_path.text()[:-4]+" ENCRYPTED.pdf")

    def on_button_clicked(self):
        writer = PyPDF2.PdfWriter()
        reader = PyPDF2.PdfReader(self.label_path.text())
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])
        writer.encrypt(self.password.text())
        with open(self.outputfile.text(), "wb") as f:
            writer.write(f)
        self.feedback.setText(f"{self.outputfile.text()} succesfully encrypted")



    def get_properties_provider(self):
        return None

    def get_side_options(self):
        return None

