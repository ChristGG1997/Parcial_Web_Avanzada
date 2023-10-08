from config.database import ma, db, app

class Label(db.Model):
    __tablename__ = 'tbllabel'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    id_package = db.Column(db.Integer, db.ForeignKey('tblpackage.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id'))

    def __init__(self, name):
       self.name = name

with app.app_context():
    db.create_all()

class LabelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'id_package', 'id_user')