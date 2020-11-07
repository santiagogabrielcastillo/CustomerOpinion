from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    @staticmethod
    def get_by_email(email):
        return Admin.query.filter_by(email=email).first()

    @staticmethod
    def is_login_valid(email, password):
        admin = Admin.get_by_email(email)
        print(admin)
        if admin.password == password:
            return True
        else:
            return False


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


    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(25), nullable=False)
    dealer = db.Column(db.String(25), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)

    def __init__(self, customer_name, customer_email, dealer, rating, comments):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dealers = db.relationship('Dealer', backref='store', lazy=True)

    def __init__(self, name):
        self.name = name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Store.query.all()

    @staticmethod
    def get_by_id(id):
        return Store.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Store.query.filter_by(name=name).first()