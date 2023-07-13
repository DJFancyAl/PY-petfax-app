from flask import (Blueprint, render_template)

bp = Blueprint("fact", __name__, url_prefix="/facts")

# facts index route
@bp.route('/')
def index():
    return "List of Facts here!"

@bp.route('/new')
def pet_view(): 
    return render_template('new-fact.html')