#!/usr/local/bin/python

import datetime
import sys
import csv
import re
import os
from src.create_session import session
from src.model import Expense, Category

class b:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

categories = []
for cat in session.query(Category).order_by(Category.id):
    categories.append(cat)
tot_cats = len(categories)


def user_input():
    while True:
        try:
            ################# HEADER ###################
            print b.WARNING + "Enter Ctrl+C to exit" + b.ENDC
            print


            ################# MONTO ###################
            price = raw_input(b.BOLD + "Monto? " + b.ENDC)
            price = price.strip()
            
            match = re.search(r'(\d+)', price)
            while match is None:
                price = raw_input(b.FAIL + "(Error) Monto? " + b.ENDC)
                price = price.strip()
                match = re.search(r'(\d+)', price)
            price = abs(int(price))

                            
            ################# DESC ###################                
            item = raw_input(b.BOLD + "Descripcion? " + b.ENDC)

                
            ################# FECHA ###################
            today = datetime.datetime.strftime(datetime.date.today(), '%d-%m-%Y')
            date = raw_input((b.OKBLUE + "Fecha [%s]: " + b.ENDC) % today)

            match = re.search(r'(\d+-\d+-\d+)', date)
            while match is None and date != "":
                date = raw_input((b.FAIL + "(Error) Fecha [%s]: " + b.ENDC) % today)
            
            if date == "":
                date = today

            date = datetime.datetime.strptime(date, '%d-%m-%Y')

            ################# TIPO ###################            
            _type = raw_input(b.OKBLUE + "Gasto (g) o Ingreso (i) ([g]/i)? " + b.ENDC)
            
            while _type not in ("", "g", "i"):
                _type = raw_input((b.FAIL + "(Error) Gasto (g) o Ingreso (i)? [g] " +b.ENDC))
            
            if _type == "":
                _type = "g"
            if _type == 'g':
                price = -price


            ################# CATEGORIA ###################
            print "Categoria?"
            for i, cat in enumerate(categories):
                print "  %d) %s" % (i + 1, cat.name)
            print "  %d) Crear nueva" % (tot_cats + 1)

            cat_idx = 0
            cat = raw_input(b.OKBLUE + "Choose: ([0] for none) " + b.ENDC)
            cat = cat.strip()
            
            if cat != "":
                match = re.search(r'(\d+)', cat)
                while match is None or int(cat) not in range(0, tot_cats + 2):
                    cat = raw_input(b.FAIL + "[Error] Choose: ([0] for none) " + b.ENDC)
                    cat = cat.strip()
                    match = re.search(r'(\d+)', cat)
                cat_idx = int(cat)
            if cat_idx < tot_cats + 1:
                category_id = categories[cat_idx].id
            elif cat_idx == tot_cats + 1:
                cname = raw_input(b.BOLD + "Nombre de categoria? " + b.ENDC)
                while cname.strip == "":
                    cname = raw_input("[Error] Nombre de categoria? ")
                disp = raw_input("Categoria especial? (y/[n]) ")
                disp = disp.strip()
                while disp not in ("y", "n", ""):
                    disp = raw_input(b.FAIL + "[Error] Categoria especial? (y/[n]) " + b.ENDC)
                    disp = disp.strip()
                if disp == "y":
                    disp = True
                else:
                    disp = False
                c = Category(timestamp=date, name=cname, displayed=disp)
                session.add(c)
                session.commit()
                category_id = c.id
            else:
                category_id = None

            ################# YIELD ###################
            yield (date, item, price, category_id)
            print
        except KeyboardInterrupt:
            print
            print
            break

        
if __name__ == '__main__':
    items = list(user_input())

    for date, desc, price, cat_id in items:
        expense = Expense(timestamp=date, description=desc, amount=price, category_id=cat_id)
        session.add(expense)

    session.commit()
        

    

    
