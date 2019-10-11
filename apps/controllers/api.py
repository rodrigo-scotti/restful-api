from flask_restful import Api, Resource
from apps.models.User import User


class Index(Resource):
  def get(self):
    return {'Hello': 'World'}


class User(Resource):
  def get(self):
    user = User()
    return user.get()


  def post(self, data):
    user = User()
    return user.set(data)


api = Api()


def configure_api(app):
  api.add_resource(Index, '/')
  api.add_resource(User, '/user')
  api.init_app(app)

