#!/usr/local/bin/python

import datetime
import sys
import csv
import re
import os
from create_session import session
from model import Expense


def user_input():
    while True:
        try:
            print "Type Ctrl+C to exit"
            print

            today = datetime.datetime.strftime(datetime.date.today(), '%d-%m-%Y')
            date = raw_input("Fecha [%s]: " % today)

            match = re.search(r'(\d+-\d+-\d+)', date)
            while match is None and date != "":
                date = raw_input("(Error) Fecha [%s]: " % today)
            
            if date == "":
                date = today

            date = datetime.datetime.strptime(date, '%d-%m-%Y')
            
            _type = raw_input("Gasto (g) o Ingreso (i) ([g]/i)? ")
            
            while _type not in ("", "g", "i"):
                _type = raw_input("(Error) Gasto (g) o Ingreso (i)? [g] ")
            
            if _type == "":
                _type = "g"
                
            item = raw_input("Descripcion? ")
           
            price = raw_input("Monto? ")
            
            match = re.search(r'(\d+)', price)
            while match is None:
                price = raw_input("(Error) Monto? ")
                match = re.search(r'(\d+)', price)
            price = abs(int(price))

            if _type == 'g':
                price = -price
            
            yield (date, item, price)
            print
        except KeyboardInterrupt:
            print
            print
            break

        
if __name__ == '__main__':
    items = list(user_input())

    for date, desc, price in items:
        expense = Expense(timestamp=date, description=desc, amount=price)
        session.add(expense)

    session.commit()
        

    

    
