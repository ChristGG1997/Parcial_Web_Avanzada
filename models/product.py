from config.db import ma, db, app

class Product(db.Model):
    __tablename__ = 'tblproduct'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    number = db.Column(db.Numeric)

    def __init__(self, name):
       self.name = name

with app.app_context():
    db.create_all()

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'number')