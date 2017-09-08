age = int(input ('введите свой возраст: '))
age_end_kindergarten = 6
age_end_school = 18
age_end_university = 24

if (age) >= age_end_university:
	employment = ' объект работает'
else: 	
	if age >=age_end_school:
		employment = 'объект учится в университете'
	elif age >=age_end_kindergarten:
		employment = 'объект учится в школе'
	else: 
		employment = 'объект ходит в детский сад'	
print (employment) 

