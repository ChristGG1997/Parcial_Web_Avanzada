from config.db import app
from controllers.users.users_controller import ruta_user
from controllers.label.label_controller import ruta_label
from controllers.packege.package__controller import ruta_package
from controllers.production.production_controller import ruta_production

app.register_blueprint(ruta_user, url_prefix = "/api_v1.0" )
app.register_blueprint(ruta_label, url_prefix = "/api_v1.0" )
app.register_blueprint(ruta_package, url_prefix = "/api" )
app.register_blueprint(ruta_production, url_prefix = "/api" )
