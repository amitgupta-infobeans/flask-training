import os
from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)
jwt = JWT(app, authenticate, identity)


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello':"World"}    
# api.add_resource(HelloWorld, '/')



#---------------model---------------------
class Puppy(db.Model):

    name = db.Column(db.String(80), primary_key=True, )


    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name':self.name}
#-------------------------------------------


puppies = [{'name':"tomy"}, {'name':"Jacky"}, {'name':'Sheru'}]


class PuppyNames(Resource):

    # to get one records
    def get(self, name):
        # using model:
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:
            return {'name':None},404


    # to insert one records
    def post(self, name):

        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()


    # to delete one records
    def delete(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note': "Deleted successfully."}


class AllName(Resource):

    # @jwt_required()
    # return all the records
    def get(self):
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]


#Register
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllName, '/puppies')


if __name__ == '__main__':
    app.run(debug=True)

