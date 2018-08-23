#! /usr/bin/env python
import re
import sys
def read_file(filename):
    """Reads the todo.txt file and returns a list of 2-tuples, where the first
    element is the due date, and the second element is the original line"""
    file_handle = open(filename)
    todo_entries = []
    for line in file_handle:
        todo_entry = parse_line(line.strip())
        todo_entries.append(todo_entry)
    todo_entries.sort(key = lambda entry: entry[0])
    return todo_entries

def parse_line(todo_line):
    compiled_regex = re.compile(r'(?P<due_date>due:\d{4}-\d{2}-\d{2})')
    due_date = re.findall(compiled_regex, todo_line)[0]
    return (due_date, todo_line)

def write_file(filename, todo_entries):
    file_handle = open(filename, 'w')
    for entry in todo_entries:
        file_handle.write(entry[1] + "\n")
    file_handle.flush()
    file_handle.close()

def usage():
    print("Usage: todo_sorter <input_file> <output_file>")

def main():
    if len(sys.argv) < 3:
        usage()
        raise SystemExit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    entries = read_file(input_filename)
    write_file(output_filename, entries)

if __name__ == '__main__':
    main()




