from config.db import ma, db, app

class User(db.Model):
    """
    Representa un usuario en el sistema.

    Atributos:
    - id (int): El identificador único del usuario.
    - nombre (str): El nombre del usuario.
    - correo electrónico (str): la dirección de correo electrónico del usuario.
    - contraseña (str): la contraseña de la cuenta del usuario.
    - rol (int): El rol del usuario en el sistema.
    - salario (decimal.Decimal): El salario del usuario.
    - tarifa (decimal.Decimal): Tarifa horaria del usuario.
    """

    __tablename__ = 'tblusers'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.Text)
    rol = db.Column(db.Integer, db.ForeignKey('tblroles.id'))
    salario = db.Column(db.Numeric)
    tarifa = db.Column(db.Numeric)
    
    def __init__(self, nombre, email, password, rol, salario, tarifa):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
        self.salario = salario
        self.tarifa = tarifa

with app.app_context():
    db.create_all()
    

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'password', 'rol', 'salario', 'tarifa')