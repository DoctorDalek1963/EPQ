#!/usr/bin/env python

from acca_lib import write_entry, take_multiline_input

if __name__ == '__main__':
    print('Please input a new Activity Log entry:\n')
    write_entry(take_multiline_input())
