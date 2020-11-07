from flask import Blueprint, request, redirect, render_template, url_for, flash
from database import Dealer, Store, Feedback
store_bp = Blueprint('store', __name__)


@store_bp.route('/')
def index():
    stores = Store.get_all()
    return render_template('store.html', stores=stores)


@store_bp.route('/<int:store_id>', methods=['GET', 'POST'])
def store(store_id):
    stores = Store.get_all()
    shop = Store.get_by_id(store_id)
    dealers = Dealer.get_by_store(shop.id)
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if not customer_email or customer_name or dealer:
            flash('Please enter required fields', 'danger')
            return redirect(url_for('store.store', store_id=store_id))
        feedback = Feedback(customer_name=customer_name, customer_email=customer_email, dealer=dealer, rating=rating, comments=comments)
        feedback.save()
        return render_template('success.html', feedback=feedback)
    return render_template('store_opinion.html', shop=shop, dealers=dealers, stores=stores)
