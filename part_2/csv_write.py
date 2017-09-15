import csv
from some_dict import *

with open('export_final.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'Last_name', 'email', 'number']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in some_dict:
        writer.writerow(user)