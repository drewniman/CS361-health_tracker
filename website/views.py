from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Snapshot
from flask_login import login_required, current_user
from . import db
import time

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    quote = ''
    open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'w').close()
    quoteService = open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'r+')
    quoteService.write('run')
    quoteService.close()
    time.sleep(5)
    openDocument = open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'r+')
    quote = openDocument.readline()
    openDocument.close()
    return render_template("home.html", user=current_user, quote=quote)
    
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
    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        blood_pressure = request.form.get('blood_pressure')
        waist = request.form.get('waist')
        bf_percent = request.form.get('bf_percent')

        if height and not (36 < int(height) < 100):
                flash('Height out of range', category='error')
        elif weight and not (80 < int(weight) < 800):
                flash('Weight out of range', category='error')
        elif blood_pressure and not (80 < int(blood_pressure) < 220):
                flash('Blood pressure out of range', category='error')
        elif waist and not (10 < int(waist) < 100):
                flash('Waist circumference out of range', category='error')
        elif bf_percent and not (3 < int(bf_percent) < 90):
                flash('Body fat percentage out of range', category='error')
        else:
            new_snapshot = Snapshot(height=height, weight=weight, blood_pressure=blood_pressure, waist=waist, bf_percent=bf_percent, user_id=current_user.id)
            db.session.add(new_snapshot)
            db.session.commit()
            flash('Health metrics updated! If you made a mistake, you can delete your last entry.', category='success')
    return render_template("health_snapshot.html", user=current_user)
