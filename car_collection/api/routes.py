from flask import Blueprint, request, jsonify
from car_collection.helpers import token_required
from car_collection.models import db, Car, car_schema, cars_schema


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(our_user):

    color = request.json['color']
    year = request.json['year']
    make = request.json['make']
    model = request.json['model']
    max_speed = request.json['max_speed']
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    car = Car(color, year, make, model, max_speed, user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)


@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(our_user, id):
    if id:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401

@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(our_user):
    token = our_user.token
    cars = Car.query.filter_by(user_token = token).all()
    response = cars_schema.dump(cars)

    return jsonify(response)



@api.route('/cars/<id>', methods = ['PUT'])
@token_required
def update_car(our_user,id):
    car = Car.query.get(id)

    car.color = request.json['color']
    car.year = request.json['year']
    car.make = request.json['make']
    car.model = request.json['model']
    car.max_speed = request.json['max_speed']
    car.user_token = our_user.token

    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)


@api.route('/cars/<id>', methods = ['Delete'])
@token_required
def delete_car(our_user, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    

    return jsonify(response)