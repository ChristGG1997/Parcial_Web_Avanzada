from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.package import Package, PackageSchema

ruta_package = Blueprint("routes_package", __name__)

package_schema   = PackageSchema()
package_schemas = PackageSchema(many=True)

@ruta_package.route('/package', methods=['GET'])
def package():
    """
    Devuelve una respuesta JSON que contiene todos los paquetes de la base de datos.

    Devoluciones:
        Una respuesta JSON que contiene todos los paquetes de la base de datos.
    """
    resultall = Package.query.all()
    resultPackage= package_schemas.dump(resultall)
    return jsonify(resultPackage)

@ruta_package.route('/package/<int:id>', methods=['GET'])
def get_package_by_id(id):
    """
    Devuelve una respuesta JSON que contiene el paquete con el ID especificado.

    Argumentos:
        id: El ID del paquete a buscar.

    Devoluciones:
        Una respuesta JSON que contiene el paquete con el ID especificado.
    """
    result = Package.query.get(id)
    if result is None:
        return jsonify({'error': 'No se encontró el paquete especificado.'}), 404
    return package_schema.jsonify(result)

@ruta_package.route('/package', methods=['POST'])
def add_package():
    """
    Agrega un nuevo paquete a la base de datos.

    Argumentos:
        date: La fecha del paquete.
        quantity_products: La cantidad de productos en el paquete.
        total_pay: El total a pagar por el paquete.
        id_user: El ID del usuario que creó el paquete.
        state: El estado del paquete.

    Devoluciones:
        Una respuesta JSON que contiene el paquete agregado.
    """
    date = request.json['date']
    quantity_products = request.json['quantity_products']
    total_pay = request.json['total_pay']
    id_user = request.json['id_user']
    state = request.json['state']

    new_package = Package(date=date, quantity_products=quantity_products, total_pay=total_pay, id_user=id_user, state=state)

    db.session.add(new_package)
    db.session.commit()

    return package_schema.jsonify(new_package)

@ruta_package.route('/package/<int:id>', methods=['PUT'])
def update_package(id):
    """
    Actualiza un paquete existente en la base de datos.

    Argumentos:
        id: El ID del paquete a actualizar.
        date: La fecha del paquete.
        quantity_products: La cantidad de productos en el paquete.
        total_pay: El total a pagar por el paquete.
        id_user: El ID del usuario que creó el paquete.
        state: El estado del paquete.

    Devoluciones:
        Una respuesta JSON que contiene el paquete actualizado.
    """
    package = Package.query.get(id)
    if package is None:
        return jsonify({'error': 'No se encontró el paquete especificado.'}), 404

    package.date = request.json.get('date', package.date)
    package.quantity_products = request.json.get('quantity_products', package.quantity_products)
    package.total_pay = request.json.get('total_pay', package.total_pay)
    package.id_user = request.json.get('id_user', package.id_user)
    package.state = request.json.get('state', package.state)

    db.session.commit()

    return package_schema.jsonify(package)


