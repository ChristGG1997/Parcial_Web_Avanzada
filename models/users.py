from config.db import ma, db, app

class User(db.Model):
    __tablename__ = 'tblusers'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    rol = db.Column(db.Integer, db.ForeignKey('tblroles.id'))
    salario = db.Column(db.Numeric)
    tarifa = db.Column(db.Numeric)
    
    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'rol', 'salario', 'tarifa')