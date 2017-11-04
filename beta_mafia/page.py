from flask import Flask, render_template,session,request,g
from social_flask_sqlalchemy.models import init_social
from social_flask.routes import social_auth
from db import *
from flask.ext.login import LoginManager
from flask_login import *

from flask import request
from help_for_game import *


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
               
        
        for counter in range (1,session["count"]):
            name = request.form.get("%s_name"%counter)
            role = request.form.get("%s_role"%counter)
            User = GameUser(name,session["id"],role,"Alive",)
            db_session.add(User)
        db_session.commit() 
        session["first_night"] = True
        session["need_vote"] = False
        return render_template('lets_go.html')
    else:
        game = Game.query.filter(Game.id == session["id"]).first()
        return render_template('Some_page.html', count = game.number + 1)

@my_flask_app.route('/night/', methods=['POST','GET'])
def night():
    people = GameUser.query.filter(GameUser.id_game == session["id"])
    
    if session["need_vote"] == False: #and request.method == "POST":
        
        
        victim = request.form.get("victim")
        for counter in people:
            if counter.name == victim:
                counter.status = "Death"
                db_session.commit()
        
        session["first_night"] = False
        
        init_lists()
        
        for counter in people:
            if counter.role != "Мафия" and counter.status == "Alive":
                mafia_target.append(counter.name)
               
            if counter.role != "Шериф" and counter.status == "Alive":
                police_target.append(counter.name)
                
            if  counter.status == "Alive":
                doctor_target.append(counter.name)
                
            if counter.role != "Маньяк" and counter.status == "Alive":
                murderer_target.append(counter.name)
                
            if counter.role != "Красотка" and counter.status == "Alive":
                curtizane_target.append(counter.name)
        session["need_vote"] = True 
        return render_template('night.html',for_mafia = mafia_target,for_curtizane = curtizane_target,for_police = police_target, for_murderer = murderer_target,for_doctor = doctor_target)
    else:
        init_parameters()
        mafia_victim = request.form.get("mafia")
        murderer_victim = request.form.get("murderer")
        police_check = request.form.get("police")
        curtizane_visit = request.form.get("curtizane")
        doctor_saved = request.form.get("doctor")
        
        detective = GameUser.query.filter(GameUser.role == "Шериф" and GameUser.id_game == session["id"]).first()
        crime = GameUser.query.filter(GameUser.name == police_check and GameUser.id_game == session["id"]).first()
        
        if detective.status == "Alive" and crime !=None:
            if  crime.role == "Мафия":
                
                police_lucky = "Шериф угадал"
            
            else:
                
                police_lucky = "Шериф не угадал"
        else:
            
            police_lucky = "Шериф не угадал"


        if mafia_victim != police_check and mafia_victim != curtizane_visit and mafia_victim != doctor_saved:
            for counter in people:
                                 
                if counter.name == mafia_victim:
                    counter.status = "Death"
                    db_session.commit()
                    death_list.append(counter.name)
        if murderer_victim != police_check and murderer_victim != curtizane_visit and murderer_victim != doctor_saved:
            for counter in people:
                if counter.name == murderer_victim:
                    counter.status = "Death"
                    db_session.commit()
                    death_list.append(counter.name)
        for counter in people:
            if counter.status == "Alive":
                for_vote.append(counter.name)
        session["need_vote"] = False
        return render_template('vote.html', lucky = police_lucky, death = death_list, vote_list = for_vote)       



if __name__ == "__main__":
    my_flask_app.run(debug=True)
