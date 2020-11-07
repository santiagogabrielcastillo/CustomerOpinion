from database import db


class Dealer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    @staticmethod
    def get_by_id(id):
        return Dealer.query.get(id)

    @staticmethod
    def get_all():
        return Dealer.query.all()

    @staticmethod
    def get_by_store(store_id):
        return Dealer.query.filter_by(store_id=store_id)