#!/usr/bin/env python

# This is a PyQt5 based refactoring of the Activity Logger GUI

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import library


class ActivityLoggerGUI(QMainWindow):
    def __init__(self):
        super(ActivityLoggerGUI, self).__init__()

        self.setWindowTitle('Activity Logger')
        self.setGeometry(200, 200, 500, 500)

        # Create widgets
        self.info = QtWidgets.QLabel(self)
        self.info.setText('This text box supports markdown formatting. For instance, you can do *italics*, **bold text**, \n'
                          '`inline code`, [a link](https://google.com), ![an image stored in a folder](image_folder/example.png),\n'
                          '![an image stored online](https://link.to/image.png)etc.\n\n')

        self.link = QtWidgets.QLabel(self)
        self.link.setText('[Click this](https://www.markdownguide.org/basic-syntax/) to see everything you can do with markdown.')

        self.text_box = QtWidgets.QTextEdit(self)

        self.write_button = QtWidgets.QPushButton(self)
        self.write_button.setText('Write entry to file')

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setText('Exit')

        self.update_widgets()

    def update_widgets(self):
        self.info.adjustSize()
        self.link.adjustSize()
        self.text_box.adjustSize()
        self.write_button.adjustSize()
        self.exit_button.adjustSize()


def show_window():
    app = QApplication(sys.argv)
    window = ActivityLoggerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
