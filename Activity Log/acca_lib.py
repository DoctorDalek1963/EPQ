import os
from datetime import datetime


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
        return f'''<div class="entry">
    <h3>{self.date_and_time}</h3>
    <p>{self.body_text}<p>
</div>\n'''

    def create_markdown(self) -> str:
        """Return a HTML representation of the entry."""
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
