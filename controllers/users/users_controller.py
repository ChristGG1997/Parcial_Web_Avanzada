
from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.roles import Role, RoleSchema
from models.users import User, UserSchema
import hashlib
import jwt

ruta_user = Blueprint("routes_user", __name__)

roles_schema = RoleSchema()
roles_schemas = RoleSchema(many=True)

users_schema = UserSchema()
users_schemas = UserSchema(many=True)

@ruta_user.route('/user', methods=['GET'])
def get_user():
    resultall = User.query.all()
    resultUser = users_schemas.dump(resultall)
    return jsonify(resultUser)

@ruta_user.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return users_schema.jsonify(user)

@ruta_user.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']

    passwordDe = request.json['password']
    password = encrypt_password(passwordDe)

    role_id = request.json['role_id']
    new_user = User(name, email, password, role_id)
    db.session.add(new_user)
    db.session.commit()
    return users_schema.jsonify(new_user)

@ruta_user.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = request.json.get('name', user.name)
    user.email = request.json.get('email', user.email)
    user.role_id = request.json.get('role_id', user.role_id)
    db.session.commit()
    return users_schema.jsonify(user)

@ruta_user.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not check_password(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401

    token = jwt.encode({'user_id': user.id}, app.config['SECRET_KEY'])

    return jsonify({'token': token.decode('UTF-8')})

def encrypt_password(password):
    """Encrypts a password using SHA-256 algorithm"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(encrypted_password, password):
    """Checks if a password matches its encrypted version"""
    return encrypted_password == encrypt_password(password)






