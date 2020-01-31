#!/usr/bin/python

import mutagen
import os
import filetype
import sys

input_directory = sys.argv[1]
files = []
output_file = open(os.path.join(input_directory, "metadata-report.txt"), 'w+')
output_file.write(f'Report for {os.path.abspath(input_directory)}\n\n')

for entry in os.listdir(input_directory):
  file_path = os.path.join(input_directory, entry)
  if os.path.isfile(file_path):
    if filetype.guess(file_path) is not None:
      files.append(entry)

for file in files:
  output_file.write(f'{file}:\n')
  file_type = mutagen.File(os.path.join(input_directory, file))
  if file_type is not None:
    output_file.write(file_type.pprint())
    output_file.write('\n\n')
