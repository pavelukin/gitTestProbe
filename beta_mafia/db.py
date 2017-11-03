
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mafia.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base=declarative_base()
Base.query = db_session.query_property()

class Game(Base): 
    __tablename__ = 'Game'
    id = Column(Integer,primary_key=True)
    number = Column(Integer)
    def __init__(self, number=None):
        self.number = number
    def __repr__(self):
        return'<number{}'.format(self.number)
class Role(Base):

    __tablename__ = 'Role'
    id_role = Column(Integer,primary_key=True)
    name = Column(String(140))
    description = Column(String(50))
    actions = Column(Text)

    def __init__(self, name = None, description = None, action = None):
        self.name = name
        self.decription = description
        self.action = action

    def __repr__(self):
        return '<Role {}, Description {}, Action {}>'.format(self.name,self.description,self.action)

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    social_network = Column(Text)
    email = Column(Text)

    def __init__(self, name = None, surname = None, social_network = None, email = None):
        self.name = name
        self.surname = surname
        self.social_network = social_network
        self.email = email

    def __repr__(self):
        return '<Name {} {},Social Network {}, Email {}>'.format(self.name,self.surname,self.social_network,self.email)


class GameUser(Base):
    __tablename__ = 'GameUser'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    id_game = Column(Integer,ForeignKey('Game.id'))
    role = Column(String(50))
    status = Column(String(50))

    def __init__(self, name = None, id_game = None, role = None, status = None):
        
        self.name = name
        self.id_game = id_game
        self.role = role
        self.status = status
        

    def __repr__(self):
        return '<name {}, status {}, role {}>'.format(self.name,self.status,self.role)

class Night(Base):

    __tablename__ = 'Night'
    id_night = Column(Integer,primary_key=True)
    id_game = Column(Integer,ForeignKey('Game.id'))
    id_night_during_game = Column(Integer)

    def __init__(self, id_game = None, id_night_during_game = None):
        self.id_game = id_game
        self.id_night_during_game = id_night_during_game

    def __repr__(self):
        return '<Night during game {}>'.format(self.id_night_during_game)

class Election(Base):
    __tablename__ = 'Election'
    id_election = Column(Integer,primary_key=True)
    id_game = Column(Integer,ForeignKey('Game.id'))

    def __init__(self, id_game = None):
        self.id_game = id_game










if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)



    
