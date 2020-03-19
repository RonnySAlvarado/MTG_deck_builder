from flask import request, jsonify
from models_schema.user_model_schema import User, user_schema
from config import app, db

# ADD A SINGLE USER
@app.route('/register', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']

    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# GET USER BY ID
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    found_user = User.query.get(id)
    return user_schema.jsonify(found_user)

# UPDATE USER BY ID
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    found_user = User.query.get(id)

    username = request.json['username']
    # decks = request.json['decks']

    found_user.username = username
    # found_user.decks = decks

    db.session.commit()

    return user_schema.jsonify(found_user)

# DELETE CARD BY ID
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    found_user = User.query.get(id)
    db.session.delete(found_user)
    db.session.commit()
    return user_schema.jsonify(found_user)
