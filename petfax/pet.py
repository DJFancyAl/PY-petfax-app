from flask import (Blueprint, render_template)
import json

pet_data = json.load(open('pets.json'))

bp = Blueprint("pet", __name__, url_prefix="/pets")

# pets index route
@bp.route('/')
def index():
    return render_template('index.html', pets=pet_data)

@bp.route('/test')
def pets(): 
    return 'wazzzuppp!'