from model import Base, engine
import os

if not os.path.exists('./data/'):
    os.makedirs('./data/')

Base.metadata.create_all(engine)
