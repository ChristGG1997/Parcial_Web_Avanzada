from config.db import ma, db, app

class Package(db.Model):
    """
    Una clase que representa un paquete de productos.

     Atributos:
     -----------
     Yo dint
         El identificador único del paquete.
     fecha: fechahora
         La fecha en la que se creó el paquete.
     cantidad_productos: decimal.Decimal
         La cantidad de productos en el paquete.
     pago_total: decimal.Decimal
         El importe total pagado por el paquete.
     id_usuario: int
         El identificador único del usuario que creó el paquete.
     estado: booleano
         El estado del paquete (Verdadero si está activo, Falso en caso contrario).
    """

    __tablename__ = 'tblpackage'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    quantity_products = db.Column(db.Numeric)
    total_pay = db.Column(db.Numeric(precision=10, scale=2))
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    state = db.Column(db.Boolean)

    def __init__(self, date, quantity_products, total_pay, id_user, state):
        self.date = date
        self.quantity_products = quantity_products
        self.total_pay = total_pay 
        self.id_user = id_user 
        self.state = state
       

with app.app_context():
    db.create_all()

class PackageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'quantity_products', 'total_pay', 'id_user', 'state')