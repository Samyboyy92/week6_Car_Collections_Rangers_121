from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from car_collection.forms import CarForm
from car_collection.models import Car, db 


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('look at this cool project. Would you just look at it')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    carform = CarForm()
    try:
        if request.method == 'POST' and carform.validate_on_submit():
            color = carform.color.data
            year = carform.year.data
            make = carform.make.data
            model = carform.model.data
            max_speed = carform.max_speed.data
            user_token = current_user.token

            car = Car(color, year, make, model, max_speed, user_token)

            db.session.add(car)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Car was not created, please check your form and try again')
    
    user_token = current_user.token
    cars = Car.query.filter_by(user_token=user_token)    
    
    return render_template('profile.html', form=carform, cars=cars)

