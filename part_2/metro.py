import csv

with open('metro.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'number']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        print(row)