
from datetime import datetime
from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.product import Product, ProductsSchema
from models.production import Production, ProductionSchema

ruta_production = Blueprint("routes_production", __name__)

product_schema = ProductsSchema()
product_schemas = ProductsSchema(many=True)

production_schema   = ProductionSchema()
production_schemas = ProductionSchema(many=True)

@ruta_production.route('/production', methods=['GET'])
def get_production():
    resultall = Production.query.all()
    resultProduction= production_schemas.dump(resultall)
    return jsonify(resultProduction)

@ruta_production.route('/production/<int:id>', methods=['GET'])
def get_production_by_id(id):
    production = Production.query.get(id)

    if not production:
        return jsonify({'message': 'Production not found'}), 404

    return production_schema.jsonify(production)

@ruta_production.route('/production', methods=['POST'])
def post_production():
    date = datetime.now()
    price = request.json['price']
    id_package = request.json['id_package']

    new_production = Production(date=date, price=price, id_package=id_package)
    db.session.add(new_production)
    db.session.commit()

    return production_schema.jsonify(new_production)

@ruta_production.route('/production/<int:id>', methods=['PUT'])
def update_production(id):
    production = Production.query.get(id)

    if not production:
        return jsonify({'message': 'Production not found'}), 404

    production.date = datetime.now()
    production.price = request.json['price']
    production.id_package = request.json['id_package']

    db.session.commit()

    return production_schema.jsonify(production)



