
import datetime
import ephem
date = datetime.datetime.now()
print (date)
planet = 'Mars'
info = ephem.Mars(date)
print (info)