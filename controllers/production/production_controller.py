from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.product import Product, ProductsSchema
from models.production import Production, ProductionSchema

ruta_production = Blueprint("routes_production", __name__)

product_schema = ProductsSchema()
product_schemas = ProductsSchema(many=True)

production_schema   = ProductionSchema()
production_schemas = ProductionSchema(many=True)

@ruta_production.route('/package', methods=['GET'])
def production():
    resultall = Product.query.all()
    resultProduct= product_schemas.dump(resultall)

    resultall = Production.query.all()
    resultProduction= production_schemas.dump(resultall)

    return jsonify(resultProduction)