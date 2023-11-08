from config.db import ma, db, app

class Role(db.Model):
    """
    Una clase que representa un rol de usuario.

    Atributos:
    -----------
    Yo dint
        El identificador único del rol.
    nombre: cadena
        El nombre del rol.
    """

    __tablename__ = 'tblroles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

# Agregar los roles a la base de dato    
with app.app_context():
    db.create_all()
    ensamblador = Role(name='ensamblador')
    cortador = Role(name='cortador')
    guarnecedor = Role(name='guarnecedor')
    admin = Role(name='admin')

    db.session.add(ensamblador)
    db.session.add(cortador)
    db.session.add(guarnecedor)
    db.session.add(admin)

    db.session.commit()    

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')