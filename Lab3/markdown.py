"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

blockquote = False
i = 0
for line in fileinput.input():
  line = line.rstrip()
  line = convertStrong(line)
  line = convertEm(line)
  if blockquote and line[0] == '>':
    print '\t',
  elif blockquote and line[0] != '>':
    print '</blockquote>\n',
    blockquote = False
    i = 0
  if line[i] == '>':
    print '<blockquote>\n\t' + '<p>' + line[2:] + '</p>',
    blockquote = True
    i = 2
  elif line[i] == '#':
    if line[i+1] == '#':
      if line[i+2] == '#':
        print '<h3>' + line[i+4:] + '</h3>',
      else:
        print '<h2>' + line[i+3:] + '</h2>',
    else:
      print '<h1>' + line[i+2:] + '</h1>',
  else:
    print '<p>' + line[i:] + '</p>',
