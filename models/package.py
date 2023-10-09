from config.db import ma, db, app

class Package(db.Model):
    __tablename__ = 'tblpackage'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    quantity_products = db.Column(db.Numeric)
    total_pay = db.Column(db.Numeric(precision=10, scale=2))
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    state = db.Column(db.Boolean)

    def __init__(self, id):
       self.id = str(id)

with app.app_context():
    db.create_all()

class PackageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'quantity_products', 'total_pay', 'id_user', 'state')