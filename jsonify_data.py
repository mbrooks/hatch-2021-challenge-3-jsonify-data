#!/usr/bin/env python
import csv
import ast
import yaml
import json
import re

def remove_whitespaces(d):
  for k, v in d.items():
    if isinstance(v, dict):
      remove_whitespaces(v)
    if isinstance(v, str):
      d[k]=v.strip()

with open('./data/DomoArigatoData-utf8.txt', newline = '', encoding = "utf8") as csvfile:
    data  = csv.reader(csvfile, delimiter='\t', quotechar='"')
    i = 0
    for row in data:
        if i > 0:
            # Convert PHP type arrays to JSON and remove irrelavant REST metadata
            unPHPifyData = row[3].replace('=>', ':').replace('_method:patch ;', '')

            # Convert to a JSONish format
            jsonfyData = '{ ' + re.sub(r'([a-zA-Z0-9-_]+):([^;\[\]]+)', r'"\1":"\2"', unPHPifyData).replace(';', ',') + ' }'

            # YAML is less strict about JSON being formatted correctly
            parsedData = yaml.safe_load(jsonfyData)

            # remove whitespaces
            remove_whitespaces(parsedData)

            # print json
            print(json.dumps({
                'Pathogenic': row[0],
                'Gene': row[1],
                'history_class': row[2],
                'full_history': parsedData
            }))

        # increment row count
        i = i + 1

