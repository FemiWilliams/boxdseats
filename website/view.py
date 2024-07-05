from flask import Blueprint, render_template, request, flash
from Boxer import Boxer


view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        flash('Find a movie to watch by comparing your letterboxd watch lists!', category = 'info')

    if request.method == 'POST':

        firstUserName = request.form.get('firstAccount')
        secondUserName = request.form.get('secondAccount')

        boxer = Boxer()

        firstUser = boxer.get_watchlist(firstUserName)
        secondUser = boxer.get_watchlist(secondUserName)

        if firstUser is None:
            flash(f'{firstUserName} is not a valid account', category = 'error')
        elif secondUser is None:
            flash(f'{secondUserName} is not a valid account', category = 'error')
        else:
            intersection = boxer.find_intersection(firstUser, secondUser)
            return render_template("home.html", intersection = intersection)

    return render_template("home.html")