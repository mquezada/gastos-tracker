from sqlalchemy.sql import func, and_
from create_session import session
from model import Expense, Category
import datetime
import dateutil.relativedelta


def get_expenses_month(year, month):
	date = "%d-%02d-%02d" % (year, month, 1)
	date_o = datetime.datetime.strptime(date, "%Y-%m-%d")
	
	p_date_o = date_o + dateutil.relativedelta.relativedelta(months=1)
	p_date = datetime.datetime.strftime(p_date_o, "%Y-%m-%d")
	
	expenses = session.query(Expense).filter(Expense.timestamp.between(date, p_date))
	return expenses
	
	
def get_total(expenses):
	return sum(map(lambda e: e.amount, expenses))


def get_dates_comparison():
	today = datetime.datetime.now()
	prev_date = today + dateutil.relativedelta.relativedelta(months=-1)
	return today.year, today.month, prev_date.year, prev_date.month