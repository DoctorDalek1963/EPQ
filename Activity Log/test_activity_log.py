#!/usr/bin/env python
"""A simple unittest for testing the Activity Logger."""

import os
import unittest
from datetime import datetime

import library


def dict_to_env(dictionary: dict) -> str:
    """Convert a dictionary of values to a string to write to the .env file."""
    lines = []

    for key, value in dictionary.items():
        if ' ' in str(value):  # If the value has spaces
            value = '"' + value + '"'
        lines.append(str(key) + '=' + str(value))

    return '\n'.join(lines)


class TestingEnv:
    """A class to be used as a context manager to allow the use of custom .env files in tests."""

    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary
        self.filename = self.__dictionary['FILENAME']

    def __enter__(self):
        with open('.env', 'r') as f:
            self.old_env = f.read()

        with open('.env', 'w') as f:
            f.write(dict_to_env(self.__dictionary))

        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('.env', 'w') as f:
            f.write(self.old_env)


class TestActivityLogger(unittest.TestCase):
    """A class to hold methods for testing the Activity Logger."""

    # This dictionary will be turned into a .env file to test things
    NEW_ENV_DICT = {
        'LEARNER_NAME': 'Test Name',
        'LEARNER_NUMBER': 123456,
        'CENTRE_NAME': 'Test Centre',
        'CENTRE_NUMBER': 789012,
        'UNIT_NAME': 'Test Unit Name',
        'UNIT_NUMBER': 345678,
        'TEACHER_ASSESSOR': 'Test Teacher',
        'PROPOSED_PROJECT_TITLE': 'Test Title',
        'FILENAME': 'TEST_ACTIVITY_LOG',
        'CREATE_HTML': True,
        'CREATE_MARKDOWN': True
    }

    def test_ordinal_day(self) -> None:
        """Test the simple ordinal_day() function."""
        expected_values = [
            '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
            '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
            '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th',
            '31st'
        ]

        datetime_objects = []
        for i in range(1, 32):
            datetime_objects.append(datetime.strptime(str(i), '%d'))

        returned_values = list(map(library.ordinal_day, datetime_objects))

        self.assertEqual(expected_values, returned_values)

    def test_entry(self) -> None:
        """Test a basic entry."""
        entry = library.Entry('This is a basic entry.\n\nHere is some text. This bit is **bold**. This is *italic*. <3')

        entry_html = entry.create_html()
        entry_markdown = entry.create_markdown()

        self.assertIn('This is a basic entry.', entry_html)
        self.assertIn('Here is some text. This bit is <strong>bold</strong>. This is <em>italic</em>. &lt;3', entry_html)

        self.assertIn('This is a basic entry.', entry_markdown)
        self.assertIn('Here is some text. This bit is **bold**. This is *italic*. <3', entry_markdown)

    def test_top_text(self):
        """Test for TopText creation."""
        expected_html = '''<body>
<div class="top-text">
<h1>Activity Log</h1>
<table>
<tbody>
<tr>
    <td>Learner Name:</td>
    <td>Test Name</td>
</tr>
<tr>
    <td>Learner Number:</td>
    <td>123456</td>
</tr>
<tr>
    <td>Centre Name:</td>
    <td>Test Centre</td>
</tr>
<tr>
    <td>Centre Number:</td>
    <td>789012</td>
</tr>
<tr>
    <td>Unit Name:</td>
    <td>Test Unit Name</td>
</tr>
<tr>
    <td>Unit Number:</td>
    <td>345678</td>
</tr>
<tr>
    <td>Teacher Assessor:</td>
    <td>Test Teacher</td>
</tr>
<tr>
    <td>Proposed project title:</td>
    <td>Test Title</td>
</tr>
</tbody>
</table>
</div>

<hr>

<div class="entry-list">'''

        expected_markdown = '''# Activity Log

Learner Name: Test Name

Learner Number: 123456

Centre Name: Test Centre

Centre Number: 789012

Unit Name: Test Unit Name

Unit Number: 345678

Teacher Assessor: Test Teacher

Proposed project title: Test Title

---
'''

        with TestingEnv(TestActivityLogger.NEW_ENV_DICT) as filename:
            library.write_top_text(filename + '.html')
            library.write_top_text(filename + '.md')

            with open(filename + '.html', 'r') as f:
                self.assertIn(expected_html, f.read())

            with open(filename + '.md', 'r') as f:
                self.assertIn(expected_markdown, f.read())

            os.remove(filename + '.html')
            os.remove(filename + '.md')


if __name__ == '__main__':
    unittest.main()
