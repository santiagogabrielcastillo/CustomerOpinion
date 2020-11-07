import functools
import os

from flask import session, current_app, redirect, flash, url_for


def admin_required(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get('email') != os.environ.get('ADMIN'):
            flash('You need to be an admin to access this page', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_func
