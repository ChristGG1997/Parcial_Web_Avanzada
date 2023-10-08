from flask import Blueprint, redirect, request, jsonify, session, render_template
from ...config.database import app, db, ma
from ...models.users import User, UserSchema

ruta_user = Blueprint("routes_user", __name__)

users_schema   = UserSchema()
users_schemas = UserSchema(many=True)

@ruta_user.route('/user', methods=['GET'])
def user():
    resultall = User.query.all()
    resultUser= users_schemas.dump(resultall)
    return jsonify(resultUser)