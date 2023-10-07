from config.database import ma, db, app

class Cliente(db.Model):
    __tablename__ = 'tblusers'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    rol = db.Column(db.Integer, db.ForeignKey('tblroles.id'))
    salario = db.Column(db.Numeric)
    tarifa = db.Column(db.Numeric)
    

    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():s
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'telefono', 'direccion')