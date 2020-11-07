from database import db


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dealers = db.relationship('Dealer', backref='dealer', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_all():
        return Store.query.all()

    @staticmethod
    def get_by_id(id):
        return Store.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Store.query.filter_by(name=name).first()