from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.package import Package, PackageSchema

ruta_package = Blueprint("routes_package", __name__)

package_schema   = PackageSchema()
package_schemas = PackageSchema(many=True)

@ruta_package.route('/package', methods=['GET'])
def package():
    resultall = Package.query.all()
    resultPackage= package_schemas.dump(resultall)
    return jsonify(resultPackage)