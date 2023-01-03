from reading_list import data_access
from pathlib import Path
import random

def main():
    reading_list_path = Path(__file__).parent / "reading_list.csv"
    list = data_access.read_list(reading_list_path)
    choice = random.choice(list)
    print(choice)