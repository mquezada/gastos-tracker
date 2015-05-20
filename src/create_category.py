from create_session import session
from model import Category
from datetime import datetime


categories = []
print "Create categories"
print "=" * 10
while True:
    try:
        print "Enter Ctrl+C to exit"
        print
        name = raw_input("Category Name? ")
        while name.strip() == "":
            name = raw_input("[Error] Category Name? ")
            
        disp = raw_input("Special category? (will be displayed in a separate space in webapp) (y/[n]) ")
        while disp.strip() not in ("y", "n", ""):
            disp = raw_input("[Error] Special category? (y/[n]) ")
            
        if disp == "" or disp == "n":
            disp = False
        else:
            disp = True
            
        categories.append((name, disp))
    except KeyboardInterrupt:
        break

    
for name, disp in categories:
    c = Category(timestamp=datetime.now(), name=name, displayed=disp)
    session.add(c)

session.commit()
