#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from money import Money
import os


def export_gastos(year, month):
    files = os.listdir('../records')

    record_name = ''
    for fname in files:
        tmp = fname.split('_')
        if int(tmp[0]) == year and int(tmp[1]) == month:
            record_name = fname
            break
    
    FILENAME = '../records/%s' % record_name
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        data = {'data': []}
        for i, row in enumerate(reader):
            if i == 0: continue

            amount = Money(row[2], 'CLP')
            amount = amount.format('es_CL', '#')
            amount = str(amount)
            
            data['data'].append([
                row[0],  # date
                row[1],  # item
                amount,  # amount
                row[3],  # tags
            ])

        return data
