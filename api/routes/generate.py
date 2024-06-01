import datetime

import numpy as np
from flask import Blueprint, jsonify, request

generate_router = Blueprint('generate', __name__)
import pandas as pd

from faker import Faker
from faker.providers import internet, geo, profile, phone_number

fake = Faker()
fake.name()
fake.add_provider(internet)
fake.add_provider(geo)
fake.add_provider(profile)
fake.add_provider(phone_number)


@generate_router.route('/time-series/temperature', methods=['GET'])
def generate_ts_temperature():
    start_date = request.args.get('start_date') if request.args.get(
        'start_date') else datetime.datetime.utcnow() - datetime.timedelta(minutes=5)

    end_date = request.args.get('end_date') if request.args.get(
        'end_date') else datetime.datetime.utcnow()

    freq = request.args.get('frequency') if request.args.get(
        'frequency') else '5s'

    date_range = pd.date_range(start=start_date, end=end_date, freq=freq)
    values = np.random.uniform(low=0.0, high=45.0, size=len(date_range))

    df = pd.DataFrame({'collect_dt': date_range, 'value': values})

    df['collect_dt'] = df['collect_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Return the JSON response
    return jsonify(data=df.to_dict(orient='records'))


@generate_router.route('/time-series/network-traffic', methods=['GET'])
def generate_connections():
    start_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)
    end_date = datetime.datetime.utcnow()
    obj_list = []

    for _ in range(1000):
        collect_dt = fake.date_time_between(start_date=start_date, end_date=end_date)
        ip_address = fake.ipv4()
        lat = fake.latitude()
        long = fake.longitude()
        obj_list.append({'collect_dt': collect_dt, 'ip_address': ip_address, 'lat': lat, 'long': long})

    df = pd.DataFrame(obj_list)
    df['collect_dt'] = df['collect_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(data=df.to_dict(orient='records'))


@generate_router.route('/time-series/calls', methods=['GET'])
def generate_calls():
    start_date = datetime.datetime.utcnow() - datetime.timedelta(days=3)
    end_date = datetime.datetime.utcnow()
    obj_list = []

    for _ in range(1000):
        collect_dt = fake.date_time_between(start_date=start_date, end_date=end_date)
        origin = fake.phone_number()
        dest = fake.phone_number()
        obj_list.append({'collect_dt': collect_dt, 'origin': origin, 'dest': dest})

    df = pd.DataFrame(obj_list)
    df['collect_dt'] = df['collect_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(data=df.to_dict(orient='records'))


@generate_router.route('/person', methods=['GET'])
def generate_person():
    obj_list = []

    for _ in range(1000):
        obj_list.append(fake.profile())

    df = pd.DataFrame(obj_list)
    return jsonify(data=df.to_dict(orient='records'))
