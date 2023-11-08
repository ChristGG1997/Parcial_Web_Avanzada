from config.db import ma, db, app

class Production(db.Model):
    """
    Una clase que representa un registro de producción en la base de datos.

    Atributos:
    -----------
    Yo dint
        El identificador único del registro de producción.
    fecha: fechahora
        La fecha y hora en que ocurrió la producción.
    precio : decimal.Decimal
        El precio de la producción.
    paquete_id: int
        El identificador único del paquete asociado con la producción.
    """

    __tablename__ = 'tblproduction'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Numeric(precision=10, scale=2))
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackage.id'))

    def __init__(self, date, price, id_package):
        self.date = date
        self.price = price
        self.id_package = id_package
       

with app.app_context():
    db.create_all()

class ProductionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'price', 'id_package')