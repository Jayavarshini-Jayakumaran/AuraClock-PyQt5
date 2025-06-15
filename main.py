import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QPushButton, QVBoxLayout,
    QWidget, QHBoxLayout, QStackedLayout
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from digital_clock import DigitalClock
from stopwatch import Stopwatch
from weather_app import WeatherApp

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AuraClock")
        self.setGeometry(600, 300, 500, 500)
        self.setWindowIcon(QIcon("assets/icons/AuraClock-Logo"))

        # Central container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        content_layout = QStackedLayout()
        bottom_layout = QHBoxLayout()

        # Tabs for clock and stopwatch
        self.tabs = QTabWidget()
        self.tabs.addTab(DigitalClock(), QIcon("assets/icons/Clock-Icon.jpg"), "Digital Clock")
        self.tabs.addTab(Stopwatch(), QIcon("assets/icons/Stopwatch-Icon.png"), "Stopwatch")

        self.tabs.setIconSize(QSize(18, 18))

        # Add tabs to content area
        content_layout.addWidget(self.tabs)

        # Fun Weather button
        weather_button = QPushButton("☁️ Wanna Check the Weather?")
        weather_button.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: #00FF99;
                font-family: Arial;
                font-size: 14px;
                padding: 6px 12px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #444;
                color: white;
            }
        """)
        weather_button.clicked.connect(self.open_weather_window)

        # Align button to right
        bottom_layout.addStretch()
        bottom_layout.addWidget(weather_button)

        # Assemble layouts
        main_layout.addLayout(content_layout)
        main_layout.addLayout(bottom_layout)
        central_widget.setLayout(main_layout)

        # Global background
        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QTabBar::tab {
                background: black;
                color: white;
                font-family: Arial;
                font-size: 14px;
                font-weight: Bold;
                padding: 6px 20px;
                min-height: 36px;
                min-width: 120px;
                border: 1.5px solid gray;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #1c1c1c;
                color: lime;
                font-weight: bold;
            }
            QTabWidget::pane {
                border-top: 2px solid gray;
                top: 0px;
                background-color: black;
            }
        """)

    def open_weather_window(self):
        self.weather_window = WeatherApp()
        self.weather_window.setWindowTitle("Weather Forecast")
        self.weather_window.setGeometry(self.geometry().x() + 50, self.geometry().y() + 50, 400, 400)
        self.weather_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())