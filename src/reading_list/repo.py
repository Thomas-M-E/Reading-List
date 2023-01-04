import csv
from typing import List
from pathlib import Path

class BookRepo():
    def __init__(self, reading_list_path):
        self.path = reading_list_path
        with open(reading_list_path) as f:
            result = csv.DictReader(f)
        self.data = result

    def add(self, rows: List[List[str]]):
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    def delete(self, to_remove):
        lines = []
        with open(self.path, 'r') as read_file:
            reader = csv.reader(read_file)
            for row_number, row in enumerate(reader, start=1):
                if(row_number not in to_remove):
                    lines.append(row)

        with open(self.path, 'w') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(lines)

    def modify(self):
        pass
