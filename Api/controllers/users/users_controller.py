
from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.roles import Role, RoleSchema
from models.users import User, UserSchema
import hashlib
from jwt import encode

ruta_user = Blueprint("routes_user", __name__)

roles_schema = RoleSchema()
roles_schemas = RoleSchema(many=True)

users_schema = UserSchema()
users_schemas = UserSchema(many=True)

@ruta_user.route('/user', methods=['GET'])
def get_user():
    """
    Recupera todos los usuarios de la base de datos y los devuelve como un objeto JSON.

    Devoluciones:
        Un objeto JSON que contiene todos los usuarios de la base de datos.
    """
    resultall = User.query.all()
    resultUser = []
    for user in resultall:
        role = Role.query.get(user.role_id)
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': role.name,
            'salario': user.salario,
            'tarifa': user.tarifa,
        }
        resultUser.append(user_data)
    return jsonify(resultUser)

@ruta_user.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Recuperar un usuario por su ID.

    Argumentos: 
        user_id (int): el ID del usuario a recuperar.

    Devoluciones:
        Una respuesta JSON que contiene la información del usuario si se encuentra, o un error 404 si no se encuentra.
    """
    user = User.query.get(user_id)
    role = Role.query.get(user.role_id)
    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': role.name
        'salario': user.salario,
        'tarifa': user.tarifa,
    }
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return users_schema.jsonify(user_data)

@ruta_user.route('/user', methods=['POST'])
def add_user():
    """
    Agrega un nuevo usuario a la base de datos.

    Devoluciones:
        Una representación JSON del usuario recién creado.
    """
    nombre = request.json['name']
    email = request.json['email']

    passwordDe = request.json['password']

    password = encrypt_password(passwordDe)
    print(f'PasswordDe: {passwordDe}')
    print(f'Password: {password}')

    role_id = request.json['role_id']
    salario = request.json['salario']
    tarifa = request.json['tarifa']
    new_user = User(nombre, email, password, role_id, tarifa, salario)
    db.session.add(new_user)
    db.session.commit()
    return users_schema.jsonify({'message': 'User created successfully', 'data': False}), 201

@ruta_user.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Actualiza la información de un usuario en la base de datos.

    Argumentos:
        user_id (int): el ID del usuario a actualizar.

    Devoluciones:
        JSON: un objeto JSON que contiene la información del usuario actualizada.
    """
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
    """
    Inicia sesión como usuario con el correo electrónico y la contraseña proporcionados.

    Devoluciones:
        Un objeto JSON que contiene un token si el inicio de sesión se realiza correctamente.
        De lo contrario, devuelve un objeto JSON con un mensaje de error y un código de estado.

    """
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not check_password(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401

    # token = jwt.encode({'user_id': user.id}, app.config['SECRET_KEY'])
    token = encode({'user_id': user.id}, app.config['SECRET_KEY'])
    # return jsonify({'SECRET_KEY': token.decode('UTF-8')})
    return jsonify({'SECRET_KEY': token})

def encrypt_password(password):
    """Cifra una contraseña utilizando el algoritmo SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(encrypted_password, password):
    """Comprueba si una contraseña coincide con su versión cifrada"""
    return encrypted_password == encrypt_password(password)






