def find_name (some_name):
    name = ''
    names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
    while name != some_name:
        name = names.pop()
    print ('Валера нашелся')
find_name ('Валера')
