from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db  import app, db, ma
from models.roles import Role, RoleSchema
from models.users import User, UserSchema


ruta_user = Blueprint("routes_user", __name__)

roles_schema = RoleSchema()
roles_schemas = RoleSchema(many=True)

users_schema = UserSchema()
users_schemas = UserSchema(many=True)

@ruta_user.route('/user', methods=['GET'])
def user():
    resultall = User.query.all()
    resultallRol = Role.query.all()
    resultUser = users_schemas.dump(resultall)
    resultRol = roles_schemas.dump(resultallRol)
    return jsonify(resultUser)