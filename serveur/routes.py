from flask import Blueprint, jsonify

example_route = Blueprint('example', __name__)

@example_route.route('/api/example', methods=['GET'])
def example():
    return jsonify({"message": "Ceci est une autre réponse JSON"})
