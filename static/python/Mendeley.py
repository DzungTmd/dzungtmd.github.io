#! python3

'''
Written by: DT (May,2020)

This program will:
- remove unnecessary fields from the Bib file generated by Mendeley over Overleaf
- fix the capitalization of the titles

Note: The program will create a backup file with the same name (.bak) and
modify the original file

Usage:
python Mendeley.py <path-to-bib-file>
'''

import sys
import re
import fileinput
from titlecase import titlecase #pip install titlecase

# -----------Regular Expression ---------------------
# Define the fields for deleting
DelRegex = re.compile(r'''
(
## add more fields that you want to delete here
(abstract.*\n)|             ## abstract
(file.*\n)|                 ## file location
(mendeley-tags.*\n)|        ## mendeley-tags
(url.*\n)|                  ## url
(isbn.*\n)|                 ## isbn
(issn.*\n)|                 ## issn
(keywords.*\n)              ## keywords field
)
''', re.VERBOSE)

# Get the title to fix the capitalization
TitleRegex = re.compile(r'''
title.*\{\{ (.*) \}\} ## title
''', re.VERBOSE)
# --------------------------------------------------

# Process the file-content line by line
for line in fileinput.input(inplace=1, backup='.bak'):
    line = DelRegex.sub(r'\b\b\b\b',line) # Delete the redundance fields
    title = TitleRegex.findall(line)
    if title: #if not empty list
        line = 'title = {' + titlecase(title[0]) + '},\n' # adjust title
    sys.stdout.write(line)
