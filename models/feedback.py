from database import db


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
        self.comments = comments

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
