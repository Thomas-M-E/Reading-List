import csv
from pathlib import Path

class BookRepo():
    def __init__(self, reading_list_path):
        with open(reading_list_path) as f:
            result = csv.DictReader(f)
        self.data = result

    def 
