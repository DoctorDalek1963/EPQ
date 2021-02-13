#!/usr/bin/env python

# This is a PyQt5 based refactoring of the Activity Logger GUI

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget
import sys
import library


class ActivityLoggerGUI(QMainWindow):
    def __init__(self):
        super(ActivityLoggerGUI, self).__init__()

        self.setWindowTitle('Activity Logger')
        self.setGeometry(200, 200, 500, 500)

        # Create widgets
        self.widgets = []

        self.info = QtWidgets.QLabel(self)
        self.info.setText('This text box supports markdown formatting. For instance, you can do *italics*, **bold text**, \n'
                          '`inline code`, [a link](https://google.com), ![an image stored in a folder](image_folder/example.png),\n'
                          '![an image stored online](https://link.to/image.png)etc.\n\n')
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.widgets.append(self.info)

        self.link = QtWidgets.QLabel(self)
        self.link.setText('[Click this](https://www.markdownguide.org/basic-syntax/) to see everything you can do with markdown.')
        self.link.setAlignment(QtCore.Qt.AlignCenter)
        self.widgets.append(self.link)

        self.text_box = QtWidgets.QTextEdit(self)
        self.widgets.append(self.text_box)

        self.write_button = QtWidgets.QPushButton(self)
        self.write_button.setText('Write entry to file')
        self.widgets.append(self.write_button)

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setText('Exit')
        self.widgets.append(self.exit_button)

        self.update_widget_size()

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.arrange_widgets()

        central_widget = QWidget()
        central_widget.setLayout(self.vbox)
        self.setCentralWidget(central_widget)

    def update_widget_size(self):
        for widget in self.widgets:
            widget.adjustSize()

    def arrange_widgets(self):
        self.vbox.addWidget(self.info)
        self.vbox.addWidget(self.link)
        self.vbox.addWidget(self.text_box)

        self.hbox.addWidget(self.write_button)
        self.hbox.addWidget(self.exit_button)

        self.vbox.addLayout(self.hbox)


def show_window():
    app = QApplication(sys.argv)
    window = ActivityLoggerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
