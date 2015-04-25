"""migrate existing data from csv files to sqlite database"""

import csv
import os
import datetime
from model import Expense
from create_session import session


files = os.listdir('records')
expenses = []

for fname in files:
    with open('records/' + fname, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line == ['Fecha', 'Item', 'Monto', 'Tags']:
                continue
            d = datetime.datetime.strptime(line[0], '%Y-%m-%d')
            expense = Expense(timestamp=d, description=line[1], amount=int(line[2]))
            expenses.append(expense)

session.add_all(expenses)
session.commit()
            
            
