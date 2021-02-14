#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget
import sys
import library
import threading


class ActivityLoggerGUI(QMainWindow):
    def __init__(self):
        super(ActivityLoggerGUI, self).__init__()

        # A boolean to see if the window exists. Used to close properly
        self.exists = True

        self.setWindowTitle('Activity Logger')
        # This 550 just makes the window taller to make the text box bigger
        self.setGeometry(200, 200, 500, 550)

        self.entry_text = ''
        self.markdown_link = 'https://www.markdownguide.org/basic-syntax/'

        # ===== Create widgets

        self.info = QtWidgets.QLabel(self)
        self.info.setText('This text box supports markdown formatting. For instance, you can do *italics*, **bold text**, \n'
                          '`inline code`, [a link](https://google.com), ![an image stored in a folder](image_folder/example.png),\n'
                          '![an image stored online](https://link.to/image.png)etc.')
        self.info.setAlignment(QtCore.Qt.AlignCenter)

        self.link = QtWidgets.QLabel(self)
        self.link.setText(f'<a href="{self.markdown_link}"><span style="color: black; '
                          f'text-decoration: none;">[Click this]({self.markdown_link})</span></a> '
                          'to see everything you can do with markdown.')
        self.link.setAlignment(QtCore.Qt.AlignCenter)
        self.link.setOpenExternalLinks(True)

        self.text_box = QtWidgets.QTextEdit(self)
        self.text_box.setPlaceholderText('Type your Activity Log entry...')

        self.write_button = QtWidgets.QPushButton(self)
        self.write_button.setText('Write entry to file')
        # self.write_button.setEnabled(False)
        self.write_button.clicked.connect(self.write_entry)

        self.exit_button = QtWidgets.QPushButton(self)
        self.exit_button.setText('Exit')
        self.exit_button.clicked.connect(self.close_properly)

        # ===== Arrange all widgets properly

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.arrange_widgets()

        central_widget = QWidget()
        central_widget.setLayout(self.vbox)
        self.setCentralWidget(central_widget)

        # Start a thread to check the text box and enable the write button if it's got text in it
        self.button_enable_thread = threading.Thread(target=self.button_enable_loop)
        self.button_enable_thread.start()

    def arrange_widgets(self):
        self.vbox.addWidget(self.info)
        self.vbox.addWidget(self.link)
        self.vbox.addWidget(self.text_box)
        # The margins are around the edges of the window and the spacing is between widgets
        self.setContentsMargins(10, 10, 10, 10)
        self.vbox.setSpacing(20)

        self.hbox.addWidget(self.write_button)
        self.hbox.addWidget(self.exit_button)
        self.hbox.setSpacing(20)

        # The last item in the vbox is a hbox, so the final row can have two items side-by-side
        self.vbox.addLayout(self.hbox)

    def write_entry(self):
        self.entry_text = self.text_box.toPlainText()
        library.write_entry(self.entry_text)
        self.text_box.setText('')

    def check_text_box(self):
        if self.text_box.toPlainText() != '':
            self.write_button.setEnabled(True)
        else:
            self.write_button.setEnabled(False)

    def button_enable_loop(self):
        while self.exists:
            self.check_text_box()

    def close_properly(self):
        self.close()
        self.exists = False


def show_window():
    app = QApplication(sys.argv)
    window = ActivityLoggerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
