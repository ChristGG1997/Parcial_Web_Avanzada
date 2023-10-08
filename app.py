from flask import Flask, request, jsonify, redirect, render_template
from config.database import app
from controllers.users.users import ruta_user
# from api.Prestamista.apiprestamista import ruta_prestamista
# from api.Prestamo.apiprestamos import ruta_prestamo
# from api.Detalles_prestamo.apidetalles_prestamo import ruta_detalles_prestamo

app.register_blueprint(ruta_user, url_prefix = "/api" )
# app.register_blueprint(ruta_prestamista, url_prefix = "/api" )
# app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
# app.register_blueprint(ruta_detalles_prestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')