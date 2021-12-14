#!/usr/bin/python
# Filename: backup_ver3.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['C:\\tmp', 'C:\\temp']
# Notice we had to use double quotes inside the string for names with spaces in it.

# 2. The backup must be stored in a main backup directory
target_dir = 'C:\\Backup' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now + '_'+comment.replace(' ', '_') + '.rar'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = "rar a -m5 {0} {1}".format(target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
