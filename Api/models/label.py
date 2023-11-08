from config.db import ma, db, app

class Label(db.Model):
    """
    Una clase que representa una etiqueta en la base de datos.

    Atributos:
    -----------
    Yo dint
        El identificador único de la etiqueta.
    nombre: cadena
        El nombre de la etiqueta.
    paquete_id: int
        El ID del paquete al que pertenece esta etiqueta.
    id_usuario: int
        El ID del usuario que creó esta etiqueta.
    """

    __tablename__ = 'tbllabel'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackage.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))

    def __init__(self, name, id_package, id_user):
        self.name = name
        self.id_package = id_package
        self.id_user = id_user
       

with app.app_context():
    db.create_all()

class LabelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'id_package', 'id_user')