from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime


engine = create_engine('sqlite:///data/gastos.db', echo=False)
Base = declarative_base()


class Expense(Base):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    description = Column(String)
    amount = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'))
    
    def __repr__(self):
        return "<Expense(timestamp='%s', description='%s', amount='%d')>" % (self.timestamp, self.description, self.amount)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    name = Column(String)
    displayed = Column(Boolean)
    expenses = relationship('Expense')
    budgets = relationship('Budget')

    def __repr__(self):
        return "<Category(timestamp='%s', name='%s', displayed='%s'>" % (self.timestamp, self.name, self.displayed)


class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    amount = Column(Integer)
    category = Column(Integer, ForeignKey('category.id'))

    def __repr__(self):
        return "<Budget(timestamp='%s', amount='%d', category='%s')>" % (self.timestamp, self.amount, self.category)
