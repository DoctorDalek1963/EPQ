#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget, QShortcut
from PyQt5.QtGui import QKeySequence
import sys
import library
import threading


class ActivityLoggerGUI(QMainWindow):
    def __init__(self):
        super(ActivityLoggerGUI, self).__init__()

        # A boolean to see if the window exists. Used to close properly
        self._exists = True

        self.setWindowTitle('Activity Logger')
        # This 550 just makes the window taller to make the text box bigger
        self.setGeometry(200, 200, 500, 550)

        self._entry_text = ''
        self._markdown_link = 'https://www.markdownguide.org/basic-syntax/'

        # ===== Create widgets

        self._info = QtWidgets.QLabel(self)
        self._info.setText('This text box supports markdown formatting. For instance, you can do *italics*, **bold text**, \n'
                           '`inline code`, [a link](https://google.com), ![an image stored in a folder](image_folder/example.png),\n'
                           '![an image stored online](https://link.to/image.png)etc.')
        self._info.setAlignment(QtCore.Qt.AlignCenter)

        self._link = QtWidgets.QLabel(self)
        self._link.setText(f'<a href="{self._markdown_link}"><span style="color: black; '
                           f'text-decoration: none;">[Click this]({self._markdown_link})</span></a> '
                           'to see everything you can do with markdown.')
        self._link.setAlignment(QtCore.Qt.AlignCenter)
        self._link.setOpenExternalLinks(True)

        self._text_box = QtWidgets.QTextEdit(self)
        self._text_box.setPlaceholderText('Type your Activity Log entry...')

        self._write_button = QtWidgets.QPushButton(self)
        self._write_button.setText('Write entry to file')
        self._write_button.setEnabled(False)
        self._write_button.clicked.connect(self._write_entry)

        # This is a shortcut for the write entry button
        self._write_shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        self._write_shortcut.activated.connect(self._write_entry)

        self._exit_button = QtWidgets.QPushButton(self)
        self._exit_button.setText('Exit')
        self._exit_button.clicked.connect(self._close_properly)

        # This is a shortcut for the exit button
        self._exit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self._exit_shortcut.activated.connect(self._close_properly)

        # ===== Arrange all widgets properly

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()
        self._arrange_widgets()

        self._central_widget = QWidget()
        self._central_widget.setLayout(self._vbox)
        self.setCentralWidget(self._central_widget)

        # Start a thread to check the text box and enable the write button if it's got text in it
        self._button_enable_thread = threading.Thread(target=self._button_enable_loop)
        self._button_enable_thread.start()

    def _arrange_widgets(self):
        self._vbox.addWidget(self._info)
        self._vbox.addWidget(self._link)
        self._vbox.addWidget(self._text_box)
        # The margins are around the edges of the window and the spacing is between widgets
        self.setContentsMargins(10, 10, 10, 10)
        self._vbox.setSpacing(20)

        self._hbox.addWidget(self._write_button)
        self._hbox.addWidget(self._exit_button)
        self._hbox.setSpacing(20)

        # The last item in the vbox is a hbox, so the final row can have two items side-by-side
        self._vbox.addLayout(self._hbox)

    def _write_entry(self):
        self._entry_text = self._text_box.toPlainText()
        library.write_entry(self._entry_text)
        self._text_box.setText('')

    def _check_text_box(self):
        if self._text_box.toPlainText() != '':
            self._write_button.setEnabled(True)
        else:
            self._write_button.setEnabled(False)

    def _button_enable_loop(self):
        while self._exists:
            self._check_text_box()

    def _close_properly(self):
        self.close()
        self._exists = False


def show_window():
    app = QApplication(sys.argv)
    window = ActivityLoggerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
