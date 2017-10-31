from flask import Flask, render_template,session,request,g
from social_flask_sqlalchemy.models import init_social
from social_flask.routes import social_auth
from db import *
from flask.ext.login import LoginManager
from flask_login import *

from flask import request


my_flask_app = Flask(__name__)
my_flask_app.config['SOCIAL_AUTH_USER_MODEL'] = 'db.User'
my_flask_app.register_blueprint(social_auth)
init_social(my_flask_app, session)
login_manager = LoginManager()
login_manager.init_app(my_flask_app)





@login_manager.user_loader
def load_user(userid):
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass


@my_flask_app.before_request
def global_user():
    g.user = current_user


# Make current user available on templates
@my_flask_app.context_processor
def inject_user():
    try:
        return {'user': g.user}
    except AttributeError:
        return {'user': None}





@my_flask_app.route('/', methods=['POST','GET'])
def Mafia_game_support():
    if request.method == "POST":
        game = Game()
        game.number = int(request.form.get("count"))
        db_session.add(game)
        db_session.commit() 
        players_number = int(request.form.get("count"))+1
        return render_template('begin.html', count=int(request.form.get("count"))+1)
    else:
        return render_template('Mafia_game_support.html')
    

@my_flask_app.route('/game', methods=['POST','GET'])
def game():
    if request.method == "POST":
        game = Game()
        game.number = int(request.form.get("count"))
        db_session.add(game)
        db_session.commit() 
        players_number = int(request.form.get("count"))+1
        return render_template('begin.html', count=int(request.form.get("count"))+1)
    else:
        return render_template('Mafia_game_support.html')

if __name__ == "__main__":
    my_flask_app.run(debug=True)
