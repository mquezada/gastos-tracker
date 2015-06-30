# -*- coding: utf-8 -*-

from src.model import Expense, Category
from src.methods import *
#import datetime
import sys
from money import Money
from gastos import b

from operator import itemgetter

#today = datetime.datetime.now().date()

if len(sys.argv) > 1:
    month = int(sys.argv[1])

    expenses = get_expenses_month(2015, month)
    #expenses = get_expenses_month(today.year, today.month)
    
else:
    expenses = get_expenses_all()

    
expenses_list = [(e.timestamp.date(), e.amount, e.description) for e in expenses]
expenses_list = sorted(expenses_list, key=itemgetter(0))
    
for e in expenses_list:
    if e[1] < 0:
        h = b.FAIL
    else:
        h = b.OKGREEN
        
    m = Money(e[1], 'CLP')
    m = h + m.format("es_ES", u"#,##0") + b.ENDC
    
    print "%s\t%s\t%s" % (e[0], m, e[2])

total = get_total(expenses)
if total < 0:
    h = b.FAIL
else:
    h = b.OKGREEN
        
m = Money(total, 'CLP')
m = h + m.format("es_ES", u"#,##0") + b.ENDC

print
print "Total\t%s" % m
