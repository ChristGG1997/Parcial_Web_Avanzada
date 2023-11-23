
from datetime import datetime
from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.product import Product, ProductsSchema
from models.package import Package, PackageSchema
from models.production import Production, ProductionSchema
from datetime import datetime
from flask import request, jsonify
from jwt import decode, InvalidTokenError


ruta_production = Blueprint("routes_production", __name__)

product_schema = ProductsSchema()
product_schemas = ProductsSchema(many=True)

production_schema   = ProductionSchema()
production_schemas = ProductionSchema(many=True)

# ---------------------------------------------------------------------------- #
#                                  PRODUCTIONS                                 #
# ---------------------------------------------------------------------------- #

@ruta_production.route('/production', methods=['GET'])
def get_production():
    """
    Devuelve todos los datos de producción en formato JSON.

    Devoluciones:
        JSON: un objeto JSON que contiene todos los datos de producción.
    """
    resultall = Production.query.all()
    resultProduction= production_schemas.dump(resultall)
    return jsonify(resultProduction)

@ruta_production.route('/production/<int:id>', methods=['GET'])
def get_production_by_id(id):
    """
    Recuperar una producción por su ID.

    Argumentos:
        id (int): El ID de la producción a recuperar.

    Devoluciones:
        Una representación JSON del objeto de producción si se encuentra, o un mensaje de error 404 si no se encuentra.
    """
    production = Production.query.get(id)

    if not production:
        return jsonify({'message': 'Production not found'}), 404

    return production_schema.jsonify(production)

@ruta_production.route('/production', methods=['POST'])
@ruta_production.route('/production', methods=['POST'])
def post_production():
    """
    Punto final para crear un nuevo registro de producción.

    Devoluciones:
        Una representación JSON del registro de producción recién creado.
    """
    # token_required = token_required()

    # if token_required == False:
    #     return jsonify({'message': 'Token is missing'}), 401

    date = datetime.now()
    id_package = request.json['id_package']
    packages = Package.query.filter_by(id=id_package).first()
    quantity_products = request.json['quantity_products']
    price = request.json['price']

    if packages != {}:
        total_pay = request.json['total_pay']
        user_id = request.json['user_id']
        state = 0

        if quantity_products == 12 or packages.quantity_products == 12:
            packages.state = 1
            db.session.commit()

        if quantity_products < 12 or packages.quantity_products < 12:

            for i in range(quantity_products):
                new_production = Production(date=date, price=price, id_package=id_package)
                db.session.add(new_production)
                db.session.commit()

            packages.quantity_products = request.json.get('quantity_products', quantity_products)
            db.session.commit()

        else:
            return jsonify({'message': 'Quantity products is greater than 12'}), 404
        
    
    else:
        if packages.quantity_products < 12:
            date = datetime.now()

            for i in range(quantity_products):
                new_production = Production(date=date, price=price, id_package=id_package)
                db.session.add(new_production)
                db.session.commit()

            if quantity_products == 12:
                state = 1
            
            if  quantity_products > 12:
                return jsonify({'message': 'Quantity products is greater than 12'}), 404

            new_package = Package(date=date, quantity_products=quantity_products, total_pay=total_pay, id_user=user_id, state=state)
            db.session.add(new_package)
            db.session.commit()

    return production_schema.jsonify({'message': 'ADD'}), 201

@ruta_production.route('/production/<int:id>', methods=['PUT'])
def update_production(id):
    """
    Actualizar un registro de producción en la base de datos.

    Argumentos:
        id (int): El ID del registro de producción a actualizar.

    Devoluciones:
        Una respuesta JSON que contiene el registro de producción actualizado.
    """
    production = Production.query.get(id)

    if not production:
        return jsonify({'message': 'Production not found'}), 404

    production.date = datetime.now()
    production.price = request.json['price']
    production.id_package = request.json['id_package']

    db.session.commit()

    return production_schema.jsonify(production)

# ---------------------------------------------------------------------------- #
#                                   PRODUCTOS                                  #
# ---------------------------------------------------------------------------- #

@ruta_production.route('/product', methods=['GET'])
def get_products():
    """
    Devuelve todos los datos de la tabla Product en formato JSON.

    Devoluciones:
        JSON: un objeto JSON que contiene todos los datos de la tabla Product.
    """
    resultall = Product.query.all()
    resultProduct = product_schemas.dump(resultall)
    return jsonify(resultProduct)

@ruta_production.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(id):
    """
    Obtener un registro de product por su ID.

    Argumentos:
        id (int): El ID del registro de producción a obtener.

    Devoluciones:
        Una respuesta JSON que contiene el registro de producción correspondiente al ID.
    """
    production = Production.query.get(id)

    if not production:
        return jsonify({'message': 'Production not found'}), 404

    return production_schema.jsonify(production), 200

@ruta_production.route('/product', methods=['POST'])
def post_product():
    """
    Agrega un nuevo producto a la tabla Product.

    Argumentos:
        name (str): El nombre del producto.
        number (float): El número del producto.

    Devoluciones:
        Una respuesta JSON que contiene el nuevo producto agregado.
    """
    name = request.json['name']
    number = request.json['number']

    new_product = Product(name=name, number=number)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify({'message': 'Product created'}), 201

@ruta_production.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    """
    Actualiza un registro de product existente por su ID.

    Argumentos:
        id (int): El ID del registro de producción a actualizar.

    Devoluciones:
        Una respuesta JSON que contiene el registro de producción actualizado.
    """
    product = Product.query.get(id)

    if not product:
        return jsonify({'message': 'Product not found'}), 404

    # Update production record with new data
    product.name = request.json['name']
    product.number = request.json['number']

    db.session.commit()

    return production_schema.jsonify({'message': 'Product updated'}), 200

@ruta_production.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    """
    Elimina un registro de producto existente por su ID.

    Argumentos:
        id (int): El ID del registro de producto a eliminar.

    Devoluciones:
        Una respuesta JSON que indica si el producto fue eliminado correctamente.
    """
    product = Product.query.get(id)

    if not product:
        return jsonify({'message': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted'}), 200



def token_required():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split()[1]
        try:
            decoded_token = decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # Do something with the decoded token, such as checking if the user_id is valid
            user_id = decoded_token['user_id']
            # ...
            return jsonify({'message': 'Valid token', 'state': True}), 200
        except InvalidTokenError:
            return jsonify({'message': 'Invalid token', 'state': False}), 401
    else:
        return jsonify({'message': 'Token is missing', 'state': False}), 401
