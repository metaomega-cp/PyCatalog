import miniapps.abstract_miniapp

import os
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore

import requests
from bs4 import BeautifulSoup
import re

folder_path = os.path.dirname(__file__)

class MiniApp(miniapps.abstract_miniapp.AbstractMiniApp):
    def __init__(self):
        self.ui = None

    def get_ui(self):
        if not self.ui:

            self.ui= PyQt6.QtWidgets.QWidget()
            layout = PyQt6.QtWidgets.QVBoxLayout()
            self.ui.setLayout(layout)

            self.formLayout = PyQt6.QtWidgets.QFormLayout()
            self.formLayout.setObjectName("formLayout")

            cities = self.loadCities()
            self.cityCombo = PyQt6.QtWidgets.QComboBox()
            keys = list(cities.keys())
            keys.sort()
            [self.cityCombo.addItem(city, cities[city]) for city in keys]
            self.formLayout.addRow("Select City:", self.cityCombo)

            self.submitButton = PyQt6.QtWidgets.QPushButton("Submit")
            self.submitButton.clicked.connect(lambda:self.on_button_clicked())
            self.formLayout.addRow("", self.submitButton)

            widget1 = PyQt6.QtWidgets.QWidget()
            widget1.setLayout(self.formLayout)
            layout.addWidget(widget1)

            widget2 = PyQt6.QtWidgets.QWidget()
            self.weather_label = PyQt6.QtWidgets.QLabel()
            layout2 = PyQt6.QtWidgets.QVBoxLayout()
            layout2.addWidget(self.weather_label)
            widget2.setLayout(layout2)
            layout.addWidget(widget2)

        return self.ui

    def on_button_clicked(self):
        data = self.cityCombo.currentData()
        url = f"https://www.timeanddate.com/weather/{data[1]}/{data[0]}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find("div", class_="h2").get_text(strip=True)
        description = soup.find("div", class_="h2").find_next("p").get_text(strip=True)

        text=f"""Weather in {data[2]}:
Temperature : {temperature}
Condition: {description}"""
        self.weather_label.setText(text)



    def get_properties_provider(self):
        return None

    def get_side_options(self):
        return None

    def loadCities(self):
        cities = {}
        url = "https://www.timeanddate.com/weather/?low=4"
        response = requests.get(url)
        pattern = r'<a href="/weather/[\w-]+/[\w-]+">[\w -]+'
        for r in re.findall(pattern, response.text):
            city_code = r.split('"')[1].split('/')[3]
            country_code = r.split('"')[1].split('/')[2]
            city_name = r.split('>')[1]
            cities[f"{city_name} ({country_code})"] = [city_code,country_code,city_name]
        return cities




