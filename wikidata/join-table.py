#!/usr/bin/env python3

import csv
import sys


reader = csv.reader(sys.stdin)
for idx, row in enumerate(reader):
    if idx == 0:
        continue # skip header
    gacsid = row[0]
    label = row[1]
    data = ' / '.join([col.replace('\n', ' ') for col in row[2:] if col != ''])
    print("\t".join([gacsid, label, data, 'location']))

