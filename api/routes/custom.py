from flask import Blueprint, request, jsonify

from api.utils import generate_custom_value
from api.utils.faker_singleton import SingletonFaker

custom_router = Blueprint('custom', __name__)

s = SingletonFaker()


@custom_router.route('/', methods=['POST'])
def generate_custom_results():
    if request.args.get('locale'):
        locale = request.args.get('locale')
        s.set_locale(locale)

    # fields = {"collected_at": {"method": "date", "extra_params": {}},
    #           "ip": {"method": "ipv4", "extra_params": {"address_class": "b"}}}

    # TODO: Validate methods before creating records
    data = [generate_custom_value(request.json) for _ in range(1000)]

    return jsonify(data=data)
