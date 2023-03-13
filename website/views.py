from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Snapshot
from flask_login import login_required, current_user
from . import db
import time

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    weights = []
    bp = []
    heights = []
    waists = []
    bf_percents = []
    for snapshot in current_user.snapshots:
        if snapshot.weight: weights.append(snapshot.weight)
        if snapshot.blood_pressure: bp.append(snapshot.blood_pressure)
        if snapshot.height: heights.append(snapshot.height)
        if snapshot.waist: waists.append(snapshot.waist)
        if snapshot.bf_percent: bf_percents.append(snapshot.bf_percent)
    weights_x = [i for i in range(len(weights))]
    bp_x = [i for i in range(len(bp))]
    heights_x = [i for i in range(len(heights))]
    waists_x = [i for i in range(len(waists))]
    bf_percents_x = [i for i in range(len(bf_percents))]

    quote = ''
    open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'w').close()
    quoteService = open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'r+')
    quoteService.write('run')
    quoteService.close()
    time.sleep(5)
    openDocument = open('/Users/drewniman/osu-classes/CS-361/exercise_tracker/AimeesMicroservice/quoteService.txt', 'r+')
    quote = openDocument.readline()
    openDocument.close()
    return render_template("home.html", user=current_user, quote=quote, weights=weights, bp=bp, heights=heights, waists=waists, bf_percents=bf_percents, weights_x=weights_x, bp_x=bp_x, heights_x=heights_x, waists_x=waists_x, bf_percents_x=bf_percents_x)
    
@views.route('/exercise')
@login_required
def exercise():
    return render_template("exercise.html", user=current_user)

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
            flash('Health metrics updated!', category='success')
    return render_template("health_snapshot.html", user=current_user)
