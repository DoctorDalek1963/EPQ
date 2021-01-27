import os
from datetime import datetime
import markdown


def ordinal_day(date_time: datetime) -> str:
    """Take a datetime object and return an ordinal day ('23rd' or '12th', for example)."""
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
    """A class where each instance is an entry in the activity log."""
    def __init__(self, body_text: str):
        self.body_text = body_text.expandtabs(4)  # Replace tabs with 4 spaces

        now = datetime.now()

        day_of_month = ordinal_day(now)

        original_hour = now.hour
        hour = original_hour if original_hour < 12 else original_hour - 12  # Convert to 12 hour

        self.date_and_time = now.strftime(f'%A {day_of_month} %B %Y, {hour}:%M %p')

    def create_html(self) -> str:
        """Return a HTML representation of the entry."""
        # markdown.markdown converts markdown formatting into HTML
        return f'''<div class="entry">
    <h3 class="date-and-time">{self.date_and_time}</h3>
    <p class="body-text">
        {markdown.markdown(self.body_text)}
    </p>
</div>\n'''

    def create_markdown(self) -> str:
        """Return a markdown representation of the entry."""
        return f'''### {self.date_and_time}

{self.body_text}\n'''


def write_entry(entry_text: str, filename: str = 'Activity Log'):
    """Take an entry body text and an optional filename and write the entry with the current date and time to filename.md and filename.html in the respective formats.

If no filename is specified, 'Activity Log' is used."""
    entry = Entry(entry_text)

    # Get rid of . if filename has it
    filename, _ = os.path.splitext(filename)

    with open(filename + '.md', 'a') as f:
        f.write(entry.create_markdown())

    with open(filename + '.html', 'a') as f:
        f.write(entry.create_html())


class TopText:
    """A class where there should only be one instance, which is the text at the top of the Activity Log containing all the necessary information."""
    def __init__(self, learner_name='LEARNER NAME', learner_number='LEARNER NUMBER', centre_name='CENTRE NAME',
                 centre_number='CENTRE NUMBER', unit_name='UNIT NAME', unit_number='UNIT NUMBER',
                 teacher_assessor='TEACHER ASSESSOR', proposed_project_title='PROPOSED PROJECT TITLE'):
        """All arguments are strings. Even the numbers.

If left blank, they will default to the name of the argument in all caps."""
        self.learner_name = learner_name
        self.learner_number = learner_number
        self.centre_name = centre_name
        self.centre_number = centre_number
        self.unit_name = unit_name
        self.unit_number = unit_number
        self.teacher_assessor = teacher_assessor
        self.proposed_project_title = proposed_project_title

    def create_html(self):
        """Create the top text for the HTML Activity Log."""
        return f'''<head>
    <title>Activity Log</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
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

<div class="entry-list">\n\n\n'''

    def create_markdown(self):
        """Create the top text for the markdown Activity Log."""
        return f'''# Activity Log

Learner Name: {self.learner_name}

Learner Number: {self.learner_number}

Centre Name: {self.centre_name}

Centre Number: {self.centre_number}

Unit Name: {self.unit_name}

Unit Number: {self.unit_number}

Teacher Assessor: {self.teacher_assessor}

Proposed project title: {self.proposed_project_title}\n\n\n'''


class NoTopTextError(Exception):
    """A simple class to create a custom error if the file being written to doesn't have top text.

This is just to handle this particular error and prompt the user to create the top text."""
    pass
