from item import Item
import datetime
import sys
import csv
import re
import os

meses = ('enero', 'febrero', 'marzo',
         'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre',
         'octubre', 'noviembre', 'diciembre')


def user_input():
    while True:
        try:
            print "Press CTRL+C to exit"
            print

            today = str(datetime.date.today())
            date = raw_input("Fecha [%s]: " % today)

            match = re.search(r'(\d+-\d+-\d+)', date)
            while match is None and date != "":
                date = raw_input("(Error) Fecha [%s]: " % today)
            
            if date == "":
                date = today
                
            _type = raw_input("Gasto (g) o Ingreso (i) ([g]/i)? ")
            while _type not in ("", "g", "i"):
                _type = raw_input("(Error) Gasto (g) o Ingreso (i)? [g] ")
            
            if _type == "":
                _type = "g"
                
            item = raw_input("Item? ")
           
            price = raw_input("Monto? ")
            match = re.search(r'(\d+)', price)
            while match is None:
                price = raw_input("(Error) Monto? ")
                match = re.search(r'(\d+)', price)
            price = abs(int(price))

            if _type == 'g':
                price = -price

            tags = raw_input("Tags? (separados por coma) ")
            
            yield (date, item, price, tags)
            print
        except KeyboardInterrupt:
            break

        
if __name__ == '__main__':
    this_month = datetime.date.today().month
    this_year = datetime.date.today().year

    F_GASTOS = "records/%d_%02d_%s.csv" % (this_year, this_month, meses[this_month - 1])

    if not os.path.exists("records"):
        os.makedirs("records")
    
    if not os.path.exists(F_GASTOS):
        with open(F_GASTOS, 'w') as f:
            f.write("Fecha,Item,Monto,Tags\n")

    items = user_input()
    for date, desc, price, tags in items:
        item = Item(F_GASTOS, date, price, desc, tags)
        item.save_item()

    

    
