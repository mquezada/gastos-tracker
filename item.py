import csv

class Item:
    def __init__(self, csvfile, date, amount, description, tags):
        self.date = date
        self.amount = amount
        self.description = description
        self.tags = tags
        self.csvfile = csvfile

    def save_item(self):
        with open(self.csvfile, "a") as f:
            writer = csv.writer(f)
            writer.writerow((self.date, self.description, self.amount, self.tags))
