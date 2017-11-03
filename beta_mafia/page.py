from flask import Flask, render_template,session,request,g
from social_flask_sqlalchemy.models import init_social
from social_flask.routes import social_auth
from db import *
from flask.ext.login import LoginManager
from flask_login import *

from flask import request


my_flask_app = Flask(__name__)
my_flask_app.secret_key = "abcdef"
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
        session["id"] = game.id
        session["count"] = players_number
        return render_template('begin.html')
    else:
        return render_template('Mafia_game_support.html')
    

@my_flask_app.route('/game/', methods=['POST','GET'])
def game():
    if request.method == "POST":
               # вот здесь, я, бля, считываю в базу все это гавно
        
        for counter in range (1,session["count"]):
            name = request.form.get("%s_name"%counter)
            role = request.form.get("%s_role"%counter)
            User = GameUser(name,session["id"],role,"Alive",)
            db_session.add(User)
        db_session.commit() 

        narod = GameUser.query.filter(GameUser.id_game == session["id"])
        
        narod[1].status = "deat h"
        db_session.commit()
       
        return render_template('vote.html', ololo = narod[1])
    else:
        game = Game.query.filter(Game.id == session["id"]).first()
        return render_template('Some_page.html', count = game.number + 1)

@my_flask_app.route('/night/', methods=['POST','GET'])
def night():
    alist = []
    narod = GameUser.query.filter(GameUser.id_game == session["id"])
    for counter in range (0,session["count"] - 1):
        alist.append(narod[counter].name)
    return render_template('night.html', count = session["count"], players = alist)



if __name__ == "__main__":
    my_flask_app.run(debug=True)
