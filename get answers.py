def get_answer(question):
	answers = {'Привет': 'привет', 'Как дела': 'нормально', 'до скорой встречи' : 'взаимно'}
	buff = str(answers [question])
	return buff.lower()
ask = input ('введите')
print (get_answer(ask))
