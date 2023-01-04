import csv
from pathlib import Path
import 

def test_csv_write():
    path = Path(__file__).parent.parent / "assets/test.csv"
    fieldnames = ['name', 'type', 'position', 'length']
    row = {'name': 'thing', 'type': 'thing2', 'position': 'thing3', 'length': 'thing4'}
    with open(path, 'w') as f:
        writer = csv.DictWriter(f=f, fieldnames=fieldnames)
        writer.writerow(row)

    with open(path, 'r') as f:
        dict_read = csv.DictReader(f)
        for read_row in dict_read: 
            assert read_row == {'name': 'thing', 'type': 'thing2', 'position': 'thing3', 'length': 'thing4'}
    


def test_repo_add():
