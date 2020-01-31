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
    file_type = mutagen.File(file_path)
    if file_type is not None:
      output_file.write(f'{entry}:\n')
      output_file.write(file_type.pprint())
      output_file.write('\n\n')
