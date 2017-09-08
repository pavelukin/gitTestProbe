def ask_user():
    answer = ''
    while True:
        print ('Как дела?')
        answer = input ('Напиши что-нибудь ')
        if answer == 'Хорошо':
            print ('досвидос')
            break
        else: 
            print ('И?')
ask_user()