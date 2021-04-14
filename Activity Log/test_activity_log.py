#!/usr/bin/env python
"""A simple unittest for testing the Activity Logger."""

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
        'CENTRE_NAME': 'Test School',
        'CENTRE_NUMBER': 789012,
        'UNIT_NAME': 'Test Unit Name',
        'UNIT_NUMBER': 345678,
        'TEACHER_ASSESSOR': 'Test Teacher',
        'PROPOSED_PROJECT_TITLE': 'Test Title',
        'FILENAME': 'Activity Log',
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


if __name__ == '__main__':
    unittest.main()
