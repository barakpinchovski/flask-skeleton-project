from flask import Blueprint, render_template, session, redirect, url_for


logout = Blueprint('logout', __name__, static_folder='static', static_url_path='/logout', template_folder='templates')


@logout.route('/logout')
def index():
    if 'username' in session:
        session.pop('username')
        return render_template('logout.html')
    else:
        return redirect(url_for('home.index'))