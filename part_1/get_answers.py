def get_answer(question):
    answers = {'Привет': 'привет', 'Как дела': 'нормально', 'до скорой встречи' : 'взаимно'}
    buff = str(answers [question])
    return buff.lower()


