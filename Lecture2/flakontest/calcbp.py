from flakon import JsonBlueprint
from flask import request, jsonify
from lecture1.fooCalculator import Calculator

calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def _sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    res = Calculator.sum(m, n)

    return jsonify(res)
