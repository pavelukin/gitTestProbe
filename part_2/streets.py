import csv
info = []
streets = []
with open('streets.csv', 'r', encoding='cp1251') as f:
    fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street','AdmArea','District','RouteNumbers','StationName','Direction','Pavilion','OperatingOrgName','EntryState','global_id','geoData']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
       # print(row)
        info.append(row)
number = len(info)-1
street_dict = {}
for count in info:
    streets.append(count['Street'])
#print(streets)
street_dict = dict.fromkeys(streets,0)
#print (street_dict)
for i in street_dict:
    flag = 1
    for j in street_dict:
        if i == j:
            if flag == 0:
                street_dict.pop(j)
                flag = 1 
#print (street_dict)
for num in streets:
    street_dict[num] += 1
#print (street_dict)
count_list = street_dict.values()
buff = 0
for it in count_list:
    if it > buff:
        buff = it
print (buff)
result = 0
for new_count, value in iter(street_dict.items()):
    if value == buff:
        result = new_count
print (result)
print (street_dict[result])