from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from database import Store, Dealer
from decorators import admin_required

admin_bp = Blueprint('admin', __name__)



@admin_bp.route('/index')
@admin_required
def index():
    return render_template('admin_menu.html')


@admin_bp.route('/stores', methods=['GET', 'POST'])
@admin_required
def list_stores():
    stores = Store.get_all()
    return render_template('admin_stores.html', stores=stores)


@admin_bp.route('/store/new', methods=['GET', 'POST'])
@admin_required
def create_store():
    if request.method == 'POST':
        name = request.form['name']
        store = Store.get_by_name(name)
        if store is None:
            store = Store(name=name)
            store.save()
            return redirect(url_for('admin.list_stores'))
        else:
            flash('Store already exists', 'danger')
            return redirect(url_for('admin.create_store'))
    return render_template('admin_new_store.html')


@admin_bp.route('/store/edit/<int:store_id>', methods=['GET', 'POST'])
@admin_required
def edit_store(store_id):
    store = Store.get_by_id(store_id)
    if request.method == 'POST':
        store.name = request.form['name']
        store.save()
        return redirect(url_for('admin.list_stores'))
    return render_template('admin_edit_store.html', store=store)


@admin_bp.route('/store/delete/<int:store_id>')
@admin_required
def delete_store(store_id):
    store = Store.get_by_id(store_id)
    store.delete()
    return redirect(url_for('admin.list_stores'))


@admin_bp.route('/dealers', methods=['GET', 'POST'])
@admin_required
def list_dealers():
    stores = Store.get_all()
    dealers = Dealer.get_all()
    for dealer in dealers:
        store = dealer.store
    return render_template('admin_dealers.html', store=store, dealers=dealers)


@admin_bp.route('/dealer/new', methods=['GET', 'POST'])
@admin_required
def create_dealer():
    if request.method == 'POST':
        name = request.form['name']
        store_name = request.form['store_name']
        store = Store.get_by_name(store_name)
        if store is None:
            flash('Store does not exist', 'danger')
            return redirect(url_for('admin.create_dealer'))
        else:
            dealer = Dealer(name=name)
            store.dealers.append(dealer)
            dealer.save()
            return redirect(url_for('admin.list_dealers'))
    return render_template('admin_new_dealer.html')


@admin_bp.route('/dealer/edit/<int:dealer_id>', methods=['GET', 'POST'])
@admin_required
def edit_dealer(dealer_id):
    dealer = Dealer.get_by_id(dealer_id)
    if request.method == 'POST':
        dealer.name = request.form['name']
        dealer.save()
        return redirect(url_for('admin.list_dealers'))
    return render_template('admin_edit_dealer.html', dealer=dealer)


@admin_bp.route('/dealer/delete/<int:dealer_id>')
@admin_required
def delete_dealer(dealer_id):
    dealer = Dealer.get_by_id(dealer_id)
    dealer.delete()
    return redirect(url_for('admin.list_dealers'))