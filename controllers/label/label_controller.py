
from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.label import Label, LabelSchema

ruta_label = Blueprint("routes_label", __name__)

label_schema   = LabelSchema()
label_schemas = LabelSchema(many=True)

@ruta_label.route('/label', methods=['GET'])
def label():
    """
    Devuelve todas las etiquetas de la base de datos.

    Devoluciones:
        Un objeto JSON que contiene todas las etiquetas de la base de datos.
    """
    resultall = Label.query.all()
    resultLabel= label_schemas.dump(resultall)
    return jsonify(resultLabel)

@ruta_label.route('/label/<int:id>', methods=['GET'])
def get_label_by_id(id):
    """
    Devuelve una etiqueta con la identificación dada.

    Argumentos:
        id (int): la identificación de la etiqueta a buscar.

    Devoluciones:
        Objeto JSON: la etiqueta encontrada como un objeto JSON.
    """
    label = Label.query.get(id)

    if not label:
        return jsonify({'message': 'Label not found'})

    return label_schema.jsonify(label)

@ruta_label.route('/label', methods=['POST'])
def add_label():
    """
    Agregue una nueva etiqueta a la base de datos.

    Devoluciones:
        Una representación JSON de la etiqueta recién creada.
    """
    name = request.json['name']
    id_package = request.json['id_package']
    id_user = request.json['id_user']

    new_label = Label(name, id_package, id_user)

    db.session.add(new_label)
    db.session.commit()

    return label_schema.jsonify(new_label)

@ruta_label.route('/label/<int:id>', methods=['PUT'])
def update_label(id):
    """
    Actualiza una etiqueta con la identificación dada.

    Argumentos:
        id (int): la identificación de la etiqueta a actualizar.

    Devoluciones:
        Objeto JSON: la etiqueta actualizada como un objeto JSON.
    """
    label = Label.query.get(id)

    if not label:
        return jsonify({'message': 'Label not found'})

    name = request.json['name']
    id_package = request.json['id_package']
    id_user = request.json['id_user']

    label.name = name
    label.id_package = id_package
    label.id_user = id_user

    db.session.commit()

    return label_schema.jsonify(label)

