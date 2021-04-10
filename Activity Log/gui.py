#!/usr/bin/env python

"""This is the module that holds the GUI for the Activity Logger.

Classes:
    ActivityLoggerGUI:
        The class for the GUI for the Activity Logger.

        You have to create an instance (no arguments taken) and then call show() on it to show the window.

Functions:
    show_window():
        Create an instance of the GUI window and show it. Takes no arguments.

"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget, QShortcut
from PyQt5.QtGui import QKeySequence
import sys
import library
import webbrowser
import os


class ActivityLoggerGUI(QMainWindow):
    """The class for the GUI for the Activity Logger.

    Subclasses PyQt5.QtWidgets.QMainWindow. It has no public methods or attributes and only has __init__().
    You have to create an instance (no arguments taken) and then call show() on it to show the window.
    """

    def __init__(self):
        """Create an instance of the Activity Logger GUI. Takes no arguments."""
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
                           '![an image stored online](https://link.to/image.png), etc.')
        self._info.setAlignment(QtCore.Qt.AlignCenter)

        self._link = QtWidgets.QLabel(self)
        self._link.setText(f'<a href="{self._markdown_link}" style="color: black; '
                           f'text-decoration: none;">[Click this]({self._markdown_link})</a> '
                           'to see everything you can do with markdown.')
        self._link.setAlignment(QtCore.Qt.AlignCenter)
        self._link.setOpenExternalLinks(True)

        self._text_box = QtWidgets.QTextEdit(self)
        self._text_box.setPlaceholderText('Type your Activity Log entry...')
        # This line will enable the write button when there is text in the text box
        self._text_box.textChanged.connect(lambda: self._write_button.setEnabled(bool(self._text_box.toPlainText())))

        self._write_button = QtWidgets.QPushButton(self)
        self._write_button.setText('Write entry to file')
        self._write_button.setEnabled(False)
        self._write_button.clicked.connect(self._write_entry)
        self._write_button.setToolTip('Write the contents of the text box to the HTML and markdown files.<br><b>(Ctrl + Enter)</b>')

        # This is a shortcut for the write entry button
        self._write_shortcut = QShortcut(QKeySequence('Ctrl+Return'), self)
        self._write_shortcut.activated.connect(self._write_button.click)

        self._open_html_button = QtWidgets.QPushButton(self)
        self._open_html_button.setText('Open HTML file')
        self._open_html_button.clicked.connect(lambda: webbrowser.open_new_tab(f"{os.getcwd()}/{library.get_filename_no_extension()}.html"))
        self._open_html_button.setToolTip('Open the HTML version of the Activity Log.<br><b>(Ctrl + O)</b>')

        if not os.path.isfile(library.get_filename_no_extension() + '.html'):
            self._open_html_button.setEnabled(False)

        # This is a shortcut for the open html button
        self._open_html_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self._open_html_shortcut.activated.connect(self._open_html_button.click)

        self._exit_button = QtWidgets.QPushButton(self)
        self._exit_button.setText('Exit')
        self._exit_button.clicked.connect(self._close_properly)
        self._exit_button.setToolTip('Exit the program and discard the contents of the text box.<br><b>(Ctrl + Q)</b>')

        # This is a shortcut for the exit button
        self._exit_shortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        self._exit_shortcut.activated.connect(self._exit_button.click)

        # ===== Arrange all widgets properly

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()
        self._arrange_widgets()

        self._central_widget = QWidget()
        self._central_widget.setLayout(self._vbox)
        self.setCentralWidget(self._central_widget)

    def _arrange_widgets(self):
        """Arrange the attributes created by __init__() nicely."""
        self._vbox.addWidget(self._info)
        self._vbox.addWidget(self._link)
        self._vbox.addWidget(self._text_box)
        # The margins are around the edges of the window and the spacing is between widgets
        self.setContentsMargins(10, 10, 10, 10)
        self._vbox.setSpacing(20)

        self._hbox.addWidget(self._write_button)
        self._hbox.addWidget(self._open_html_button)
        self._hbox.addWidget(self._exit_button)
        self._hbox.setSpacing(20)

        # The last item in the vbox is a hbox, so the final row can have two items side-by-side
        self._vbox.addLayout(self._hbox)

    def _write_entry(self):
        """Write the contents of the text box to the HTML and markdown files for the Activity Log."""
        self._entry_text = self._text_box.toPlainText()
        library.write_entry(self._entry_text)
        self._text_box.setText('')
        self._open_html_button.setEnabled(True)  # Enable the button because now the file definitely exists

    def _close_properly(self):
        """Set the _exists boolean to false to end the thread and then close the window."""
        self._exists = False
        self.close()


def show_window():
    """Create an instance of ActivityLoggerGUI and show it. Terminate the program when the user exits the window."""
    app = QApplication(sys.argv)
    window = ActivityLoggerGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
