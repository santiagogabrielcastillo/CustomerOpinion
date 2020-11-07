import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request, session
from flask_migrate import Migrate
from database import db, Admin
from views.admin import admin_bp
from views.store import store_bp

app = Flask(__name__)
load_dotenv()
#Confi DB
USER_DB = os.environ.get('USER_DB')
PASS_DB = os.environ.get('PASS_DB')
URL_DB = os.environ.get('URL_DB')
NAME_DB = os.environ.get('NAME_DB')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

FULL_DB_URL = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5432/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = SECRET_KEY

db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(store_bp, url_prefix='/store')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if Admin.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for('admin.index'))
        else:
            return redirect(url_for('login_admin'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session['email'] = None
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug=True
    app.run()