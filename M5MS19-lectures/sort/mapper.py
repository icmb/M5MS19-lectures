#!/usr/bin/env python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:

	# ignore the first line of data (the header line)
	if doneFirst == 0:
		doneFirst = 1
		continue

	# remove leading and trailing whitespace
    line = line.strip()
    # split the line by empty space
	cols = line.split("\t")


