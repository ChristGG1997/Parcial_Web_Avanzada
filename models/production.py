from config.database import ma, db, app

class Production(db.Model):
    __tablename__ = 'tblproduction'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Decimal(precision=10, scale=2))
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackage.id'))

    def __init__(self, id):
       self.id = str(id)

with app.app_context():
    db.create_all()

class ProductionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'price', 'id_package')