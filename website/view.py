from flask import Blueprint, render_template, request
from Boxer import Boxer


view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        firstUser = request.form.get('firstAccount')
        secondUser = request.form.get('secondAccount')

        boxer = Boxer()

        firstUser = boxer.get_watchlist(firstUser)
        secondUser = boxer.get_watchlist(secondUser)

        if firstUser is None:
            pass
        elif secondUser is None:
            pass
        else:
            intersection = boxer.find_intersection(firstUser, secondUser)
            return render_template("home.html", intersection = intersection)

    return render_template("home.html")