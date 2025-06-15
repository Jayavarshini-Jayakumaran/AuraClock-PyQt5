import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt, QDate
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.date_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    # setting up the user interface
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.setSpacing(10)  # small space between time and date
        vbox.setContentsMargins(15, 15, 15, 15)  # no margins

        # Add stretch before and after to center vertically
        vbox.addStretch(1)
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.date_label, alignment=Qt.AlignCenter)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # loading the custom font
        # Construct the absolute path to the DS-DIGIT.TTF font file, relative to this script
        font_path = os.path.join(os.path.dirname(__file__), "assets/fonts/DS-DIGIT.TTF")
        # Try to load the custom font from the given path
        font_id = QFontDatabase.addApplicationFont(font_path)
        # Retrieve the font family names associated with the loaded font
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] if font_id != -1 else "Consolas"
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # Time styling
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size: 150px;"
            "color: hsl(111, 100%, 50%);"
            "padding-top: 60px;"
        )

        # Date styling
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont(font_family, 30))
        self.date_label.setStyleSheet("color: white;"
        "padding-bottom: 80px;"                        
        )

        self.setStyleSheet(
            "background-color: black;"
        )

        # starting the clock timer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        current_date = QDate.currentDate().toString("dddd, MMMM d, yyyy")
        self.time_label.setText(current_time)
        self.date_label.setText(current_date)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())