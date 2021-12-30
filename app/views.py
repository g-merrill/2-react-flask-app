from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/items')
def items():

  items = []

  return jsonify({ 'items': items })

@api.route('/api/add_item', methods=['POST'])
def add_item():

  return 'The POST request to this route worked!', 201
