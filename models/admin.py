from database import db


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
