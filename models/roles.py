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

with app.app_context():
    db.create_all()

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')