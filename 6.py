def get_answer(question):
	answers = {'hello': 'HI', 'how_are_u': 'fine', 'by': 'see u later'}
	buff = str(answers [question])
	return buff.lower()
ask = input ('введите')
print (get_answer(ask))
