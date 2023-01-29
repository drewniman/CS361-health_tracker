from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/exercise')
@login_required
def exercise():
    return render_template("exercise.html", user=current_user)

@views.route('/nutrition')
@login_required
def nutrition():
    return render_template("nutrition.html", user=current_user)

@views.route('/health_snapshot', methods=['GET', 'POST'])
@login_required
def health_snapshot():
    return render_template("health_snapshot.html", user=current_user)