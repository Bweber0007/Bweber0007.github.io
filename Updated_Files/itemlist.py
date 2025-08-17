# The ItemList class is used as a database helper class that also manipulates
# the data at the application level.

import sqlite3
from item import Item

class ItemList:
    def __init__(self, filename, db_name='items.db'):
        self.db_name = db_name
        self.items = [] 
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.create_table()
        self.load_from_db()
        if not self.items:
            self.add_from_file(filename)
        self.sortByName = False
        self.sortByFreq = False

# Database Helper functions

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Grocery (
                        Item TEXT PRIMARY KEY,
                        Frequency INTEGER)''')
        self.conn.commit()

    def load_from_db(self):
        self.items.clear()
        c = self.conn.cursor()
        c.execute('SELECT Item, Frequency FROM Grocery')
        rows = c.fetchall()
        for name, freq in rows:
            self.items.append(Item(name, freq))

    def save_to_db(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM Grocery')  # Reset table
        for item in self.items:
            c.execute('''INSERT INTO Grocery (Item, Frequency)
                         VALUES (?, ?)''',
                      (item.name, item.frequency))
        self.conn.commit()

    # This function is used to pull the initial data from a local file
    # before the database table is created
    def add_from_file(self, filename):
        if self.items:
            print("Data already exists. Skipping file import.")
            return
        try:
            with open(filename, 'r') as f:
                for line in f:
                    item_name = line.strip()
                    if item_name:
                        self.add_or_increment(item_name)
            self.save_to_db()
            print(f"Imported items from {filename} successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

# Application level data manipulation
    
    # This function is used when adding an item to the list from the user interface
    # If the item already exists, this function will increment the existing item
    def add_or_increment(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.increment()
                self.save_to_db()
                return
        # If item not found, add a new one
        self.items.append(Item(name))
        self.save_to_db()

    def decrement(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.decrement()
                self.save_to_db()
                return

    def get_all_items(self):
        return self.items

    def sort_by_frequency(self):
        n = len(self.items)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if self.items[j].frequency > self.items[max_idx].frequency:
                    max_idx = j
            self.items[i], self.items[max_idx] = self.items[max_idx], self.items[i]
        return self.items

    def sort_by_name(self):
        n = len(self.items)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.items[j].name.lower() < self.items[min_idx].name.lower():
                    min_idx = j
            self.items[i], self.items[min_idx] = self.items[min_idx], self.items[i]
        return self.items

