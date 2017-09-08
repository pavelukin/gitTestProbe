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
            except  KeyError:
                print ('задайте вопрос нормально')
            except KeyboardInterrupt:
                print ("...")
            except EOFError:
                print ('нормально же общались')

            
ask_user()  