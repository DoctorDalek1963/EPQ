#!/usr/bin/env python

"""This module just calls library.take_multiline_input() and writes the return value of that to the HTML and markdown files.

Functions:
    take_multiline_input(prompt='> ') -> str:
        Give the user a prompt where they can enter multiple lines in the console.

"""

from library import write_entry


def take_multiline_input(prompt='> ') -> str:
    """Give the user a prompt where they can enter multiple lines in the console."""
    lines = []

    if not prompt.endswith(' '):
        prompt += ' '

    print('This is a multiline input. You can use as many lines as you want. You cannot edit a line after you have pressed enter.\n\nWhen you want to finish, simply type "done" on a line on its own. Press Ctrl+C at any time to cancel the entry and exit.\n')

    while True:
        line = input(prompt)
        if line == 'done':
            break  # Break out of the loop to concat all the other lines
        else:
            lines.append(line)

    return '\n'.join(lines)


if __name__ == '__main__':
    print('Please input a new Activity Log entry:\n')
    write_entry(take_multiline_input())
