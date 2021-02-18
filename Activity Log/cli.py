#!/usr/bin/env python

"""This module just calls library.take_multiline_input() and writes the return value of that to the HTML and markdown files."""

from library import write_entry, take_multiline_input

if __name__ == '__main__':
    print('Please input a new Activity Log entry:\n')
    write_entry(take_multiline_input())
