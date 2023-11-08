from config.db import ma, db, app

class Product(db.Model):
    """
    Una clase que representa un producto en la base de datos.

    Atributos:
    -----------
    Yo dint
        El identificador único del producto.
    nombre: cadena
        El nombre del producto.
    número: flotador
        El número asociado al producto.
    """

    __tablename__ = 'tblproduct'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    number = db.Column(db.Numeric)

    def __init__(self, name, number):
       self.name = name
       self.number = number

with app.app_context():
    db.create_all()
    suelas = Product(name='suelas', number=2002)
    db.session.add(suelas)

    db.session.commit()    


class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'number')