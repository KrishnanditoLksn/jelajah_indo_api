import csv
import os

import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plesirbe.settings')
    django.setup()
    from plesirbe.models import Destination
    file_path = "destinasi.csv"
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        """Loop to read files"""

        for row in reader:
            travel = Destination(
                place_name=row['Place_Name'],
                description=row['Description'],
                category=row['Category'],
                city=row['City'],
                price=float(row['Price']),
                hour=int(row['Hour']),
                rating=int(row['Rating'])
            )
            travel.save()


if __name__ == "__main__":
    main()
