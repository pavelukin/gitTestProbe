from get_answers import get_answer
def ask_user():
    question = ''
    while True:
        question = input ('Введите текст: ')
        if  question == 'Пока':
            print ('досвидос')
            break
        else: 
            try : 
                print (get_answer(question))
            except  (KeyError,KeyboardInterrupt):
                print ('задайте вопрос нормально')
            except EOFError:
                print ('нормально же общались')

            
ask_user()  