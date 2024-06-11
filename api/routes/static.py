import pandas as pd
from flask import Blueprint, jsonify, request

from api.utils.faker_singleton import SingletonFaker

static_router = Blueprint('static', __name__)

s = SingletonFaker()


@static_router.route('/person', methods=['GET'])
def generate_person():
    if request.args.get('locale'):
        locale = request.args.get('locale')
        s.set_locale(locale)

    obj_list = []

    for _ in range(1000):
        obj_list.append(s.faker.profile())

    df = pd.DataFrame(obj_list)
    return jsonify(data=df.to_dict(orient='records'))
