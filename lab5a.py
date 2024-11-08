#!/usr/bin/env python3
# Author ID: isingh176

def read_file_string(file_name):
    # Takes file_name as a string for a file name and returns its entire contents as a string
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def read_file_list(file_name):
    # Takes a file_name as a string for a file name as above then
    # returns its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as file:
        content = file.readlines()
        # Remove new-line characters
        content = [line.strip() for line in content]
    return content

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
