from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.label import Label, LabelSchema

ruta_label = Blueprint("routes_label", __name__)

label_schema   = LabelSchema()
label_schemas = LabelSchema(many=True)

@ruta_label.route('/label', methods=['GET'])
def label():
    resultall = Label.query.all()
    resultLabel= label_schemas.dump(resultall)
    return jsonify(resultLabel)