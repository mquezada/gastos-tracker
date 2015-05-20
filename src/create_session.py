"""creates sqlalchemy session to handle data"""

import model
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=model.engine)
session = Session()
