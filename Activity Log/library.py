"""This module has the classes and functions for interpreting and writing user input to the HTML and markdown versions of the Activity Log.

Classes:
    Entry:
        The class for entries in the Activity Log. Each instance is an individual entry.

    TopText:
        The class for the preamble top text of the Activity Log.

    NoTopTextError:
        A simple exception if the file being written to doesn't have the preamble TopText.

Functions:
    ordinal_day(date_time: datetime.datetime) -> str:
        Takes a datetime object and returns an ordinal day ('23rd' or '12th', for example) as a string.

    get_filename_no_extension() -> str:
        Get the FILENAME value from .env, make sure it's valid, and return it with no extension.

    check_top_text(filename: str):
        Check if the file given by the filename argument has TopText.

    write_top_text(filename: str):
        Write TopText given by the variables in .env to the file given by the filename argument. WARNING: This will erase all other data in the file.

    write_entry(entry_text: str):
        Take some body text for an entry and write it to the file specified by the FILENAME value in `.env`. By default it's 'Activity Log'.

"""

import os
from datetime import datetime
import markdown
from decouple import config

default_filename = 'Activity Log'


def ordinal_day(date_time: datetime) -> str:
    """Take a datetime object and return an ordinal day ('23rd' or '12th', for example) as a string."""
    day = str(date_time.day)

    # Get day of month extension
    if day.endswith('1') and day != '11':
        extension = 'st'
    elif day.endswith('2') and day != '12':
        extension = 'nd'
    elif day.endswith('3') and day != '13':
        extension = 'rd'
    else:
        extension = 'th'

    return day + extension


class Entry:
    """The class for entries in the Activity Log. Each instance is an individual entry.

    Methods:
        create_html() -> str:
            Return a HTML representation of the entry.

        create_markdown() -> str:
            Return a markdown representation of the entry.

    """

    def __init__(self, body_text: str):
        """Create body_text and date_and_time attributes.

        Arguments:
            body_text:
                A string representation of the main text of the desired entry.
        """
        self.body_text = body_text.expandtabs(4)  # Replace tabs with 4 spaces

        now = datetime.now()

        day_of_month = ordinal_day(now)

        original_hour = now.hour
        hour = original_hour if original_hour < 13 else original_hour - 12  # Convert to 12 hour
        # Convert midnight
        if hour == 0:
            hour = 12

        self.date_and_time = now.strftime(f'%A {day_of_month} %B %Y, {hour}:%M %p')

    def create_html(self) -> str:
        """Return a HTML representation of the entry."""
        # markdown.markdown converts markdown formatting into HTML
        return f'''<div class="entry">
    <h3 class="date-and-time">{self.date_and_time}</h3>
    <p class="body-text">
        {markdown.markdown(self.body_text.replace('<', '&lt;').replace('>', '&gt;'))}
    </p>
</div>\n\n'''

    def create_markdown(self) -> str:
        """Return a markdown representation of the entry."""
        return f'''### {self.date_and_time}

{self.body_text}\n'''


class TopText:
    """The class for the preamble top text of the Activity Log.

    There should be one instance, from which you can call create_html() and create_markdown() to get the HTML and markdown versions of the top text.
    The variables can be adjusted in the .env file.

    Methods:
        create_html() -> str:
            Return string for the HTML Activity Log top text.

        create_markdown() -> str:
            Return string for the markdown Activity Log top text.

    """

    style_sheet = '''    <style>
        body {font-family: Arial, Helvetica, sans-serif;}
        div.top-text {
            margin: 0.5em;
            padding: 0.5em;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        div.top-text h1 {margin: 0 0 0.5em 0;}
        table, td {
            border: 1px solid black;
            padding: 0.2em;
            width: 400px;
        }
        table {border-collapse: collapse;}
        hr {
            margin-top: 2em;
            margin-bottom: 2em;
            width: 97vw;
        }
        div.entry-list {
            display: flex;
            flex-direction: column;
            margin: 0 3em 2em 3em; /* 2em margin on the bottom */
            padding: 0 2em 0 2em;
            width: auto; /* Fill up available space */
        }
        div.entry {margin: 0.5em 0 0.5em 0;}
        div.entry hr {width: 50%;}
    </style>'''

    def __init__(self):
        """Get the variables for TopText from the .env file."""
        self.learner_name = config('LEARNER_NAME', default='')
        self.learner_number = config('LEARNER_NUMBER', default='')
        self.centre_name = config('CENTRE_NAME', default='')
        self.centre_number = config('CENTRE_NUMBER', default='')
        self.unit_name = config('UNIT_NAME', default='')
        self.unit_number = config('UNIT_NUMBER', default='')
        self.teacher_assessor = config('TEACHER_ASSESSOR', default='')
        self.proposed_project_title = config('PROPOSED_PROJECT_TITLE', default='')

    def create_html(self) -> str:
        """Return string for the HTML Activity Log top text."""
        return f'''<head>
    <meta charset="UTF-8">
    <title>Activity Log</title>
    {TopText.style_sheet}
</head>
<body>
<div class="top-text">
<h1>Activity Log</h1>
<table>
<tbody>
<tr>
    <td>Learner Name:</td>
    <td>{self.learner_name}</td>
</tr>
<tr>
    <td>Learner Number:</td>
    <td>{self.learner_number}</td>
</tr>
<tr>
    <td>Centre Name:</td>
    <td>{self.centre_name}</td>
</tr>
<tr>
    <td>Centre Number:</td>
    <td>{self.centre_number}</td>
</tr>
<tr>
    <td>Unit Name:</td>
    <td>{self.unit_name}</td>
</tr>
<tr>
    <td>Unit Number:</td>
    <td>{self.unit_number}</td>
</tr>
<tr>
    <td>Teacher Assessor:</td>
    <td>{self.teacher_assessor}</td>
</tr>
<tr>
    <td>Proposed project title:</td>
    <td>{self.proposed_project_title}</td>
</tr>
</tbody>
</table>
</div>

<hr>

<div class="entry-list">\n\n\n'''

    def create_markdown(self) -> str:
        """Return string for the markdown Activity Log top text."""
        return f'''# Activity Log

Learner Name: {self.learner_name}

Learner Number: {self.learner_number}

Centre Name: {self.centre_name}

Centre Number: {self.centre_number}

Unit Name: {self.unit_name}

Unit Number: {self.unit_number}

Teacher Assessor: {self.teacher_assessor}

Proposed project title: {self.proposed_project_title}\n\n---\n\n\n'''


class NoTopTextError(Exception):
    """A simple class to create a custom exception if the file being written to doesn't have TopText."""

    pass


def get_filename_no_extension() -> str:
    """Get the FILENAME value from .env, make sure it's valid, and return it with no extension."""
    filename = config('FILENAME', default=default_filename)

    if filename == '':
        filename = default_filename

    # This will only remove '.html' or '.md' extensions, allowing filenames with dots in them
    # The .lower() method allows the user to write something like '.hTMl' if they really wanted to,
    # but it would still get removed
    if filename.lower().endswith('.html') or filename.lower().endswith('.md'):
        filename = os.path.splitext(filename)[0]

    return filename


def check_top_text(filename: str):
    """Check if the file given by the filename argument has TopText.

    If the file doesn't have TopText, raise NoTopTextError.
    If the file doesn't exist, create an empty file and raise NoTopTextError.
    """
    if not os.path.isfile(filename):
        try:
            open(filename, 'x')
        except FileNotFoundError:
            os.makedirs(os.path.split(filename)[0])
            open(filename, 'x')

    with open(filename, 'r') as f:
        if 'Activity Log' not in f.read():
            raise NoTopTextError(filename + ' has no top text')


def write_top_text(filename: str):
    """Write TopText given by the variables in .env to the file given by the filename argument. WARNING: This will erase all other data in the file.

    This function only accepts .md or .html files and writes the corresponding format of TopText to the given file. If the file is not .md or .html, the function will do nothing.
    """
    top_text = TopText()

    _, ext = os.path.splitext(filename)

    if ext == '.md':
        with open(filename, 'w') as f:
            f.write(top_text.create_markdown())
    elif ext == '.html':
        with open(filename, 'w') as f:
            f.write(top_text.create_html())


def write_entry(entry_text: str):
    """Take some body text for an entry and write it the the file specified by the FILENAME value in `.env`. By default it's 'Activity Log'."""
    entry = Entry(entry_text)

    filename = get_filename_no_extension()

    md_file = filename + '.md'
    html_file = filename + '.html'

    try:
        check_top_text(md_file)
    except NoTopTextError:
        write_top_text(md_file)

    with open(md_file, 'a') as f:
        f.write(entry.create_markdown())

    try:
        check_top_text(html_file)
    except NoTopTextError:
        write_top_text(html_file)

    with open(html_file, 'a') as f:
        f.write(entry.create_html())
