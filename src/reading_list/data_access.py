import csv
from pathlib import Path

def read_list(reading_list_path: Path):
    with open(reading_list_path) as f:
        result = csv.reader(f)
        read_list = [i[0] for i in result]
    return read_list
