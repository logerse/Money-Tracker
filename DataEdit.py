#!/usr/bin/env python3
#---

FILE = "Data.csv"

#---

import csv

#---

def get_field(field):
    """
    Get values of a field
    """
    obj = open(FILE, newline = "")
    reader = csv.DictReader(obj, delimiter = ",")
    values = []
    for row in reader:
        values.append(row[field])
    obj.close()
    return values

def set_field(**kwargs):
    """
    Set values of a field
    """
    obj = open(FILE,"a")
    writer = csv.DictWriter(obj, fieldnames = list(kwargs.keys()))
    for row in [kwargs]:
        writer.writerow(row)
