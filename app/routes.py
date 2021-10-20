from flask import Blueprint, jsonify, make_response

from app.models import db, User

routes = Blueprint('routes', __name__)

@routes.route('/user', methods=['GET'])
def get_user():
  users = User.query.all()
  
  return make_response(jsonify([{'id': u.id, 'name': u.name} for u in users]))


@routes.route('/user', methods=['POST'])
def post_user():
  user = User()
  user.name = "Fred"

  db.session.add(user)
  db.session.commit()
  
  return make_response(jsonify({'id': user.id, 'name': user.name}))
