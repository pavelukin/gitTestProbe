from datetime import datetime, timedelta
import locale
dt_now = datetime.now()
print (dt_now)
locale.setlocale(locale.LC_ALL, "russian")
delta = timedelta(days=1, hours=0, minutes = 0, seconds=0)
date_today = datetime.now()
date_yesterday = date_today - delta
cur_month = dt_now.month
cur_year = dt_now.year
if (cur_month == 1):
	date_last_month = dt_now.replace(year = cur_year - 1)
	date_last_month = dt_now.replace (month = 12)
else: 
	date_last_month = dt_now.replace (month = cur_month - 1)

dt_1 = date_last_month.strftime('%A %d %B %Y')
dt_2 = dt_now.strftime('%A %d %B %Y')
dt_3 = date_yesterday.strftime('%A %d %B %Y')
print ('дата прошлого месяца: '+ str (dt_1))
print ('сегодняшнее число: '+ str(dt_2))
print ( 'вчерашняя дата: '+ str(dt_3))
date_test =  "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_test, "%m/%d/%y %H:%M:%S.%f")
print (date_dt)
