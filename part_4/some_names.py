from sql import db_session, User

authors = [
	{
	'first_name':'name_1',
	'last_name':'last_name_1',
	'email':'somemail1@ya.ru',
    },
    {
	'first_name':'name_2',
	'last_name':'last_name_2',
	'email':'somemail2@ya.ru',
    },
    {
	'first_name':'name_3',
	'last_name':'last_name_3',
	'email':'somemail3@ya.ru',
    }
]

for count in authors:
	author = User(count['first_name'],count['last_name'],count['email'])
	db_session.add(author)
db_session.commit()