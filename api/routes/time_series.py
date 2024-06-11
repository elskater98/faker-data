import datetime

import pandas as pd
from flask import Blueprint, jsonify, request

from api.utils import simulate_day_temperature, simulate_energy_consumption, add_noise
from api.utils.faker_singleton import SingletonFaker

time_series_router = Blueprint('time_series', __name__)
s = SingletonFaker()


@time_series_router.route('/temperature', methods=['GET'])
def generate_temperature():
    start_date = request.args.get('start_date') if request.args.get(
        'start_date') else datetime.datetime.today()

    days = request.args.get('days') if request.args.get(
        'days') else 1

    df = simulate_day_temperature(start_date=start_date, days=days, interval=15)
    df = add_noise(df, 'temperature')

    # Return the JSON response
    return jsonify(data=df.to_dict(orient='records'))


@time_series_router.route('/energy-consumption', methods=['GET'])
def generate_energy_consumption():
    start_date = request.args.get('start_date') if request.args.get(
        'start_date') else datetime.datetime.today()

    days = request.args.get('days') if request.args.get(
        'days') else 1

    df = simulate_energy_consumption(start_date=start_date, days=days)
    df = add_noise(df, 'energy_consumption')

    df['collected_dt'] = df['collected_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')

    return jsonify(data=df.to_dict(orient='records'))


@time_series_router.route('/network-traffic', methods=['GET'])
def generate_connections():
    start_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)
    end_date = datetime.datetime.utcnow()
    obj_list = []

    for _ in range(1000):
        collect_dt = s.faker.date_time_between(start_date=start_date, end_date=end_date)
        ip_address = s.faker.ipv4()
        lat = s.faker.latitude()
        long = s.faker.longitude()
        obj_list.append({'collect_dt': collect_dt, 'ip_address': ip_address, 'lat': lat, 'long': long})

    df = pd.DataFrame(obj_list)
    df['collect_dt'] = df['collect_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')

    return jsonify(data=df.to_dict(orient='records'))


@time_series_router.route('/calls', methods=['GET'])
def generate_calls():
    start_date = datetime.datetime.utcnow() - datetime.timedelta(days=3)
    end_date = datetime.datetime.utcnow()
    obj_list = []

    for _ in range(1000):
        collect_dt = s.faker.date_time_between(start_date=start_date, end_date=end_date)
        origin = s.faker.phone_number()
        dest = s.faker.phone_number()
        obj_list.append({'collect_dt': collect_dt, 'origin': origin, 'dest': dest})

    df = pd.DataFrame(obj_list)
    df['collect_dt'] = df['collect_dt'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(data=df.to_dict(orient='records'))
