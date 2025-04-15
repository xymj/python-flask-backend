from flask import Flask, jsonify, request
# from flask_backend.db import get_db_connection, create_table, insert_data, query_data
from flask_backend.models import data_store
# from flask_backend.app import app

# @app.route('/api/table/create', methods=['GET'])
# def create_db_table():
#     conn = get_db_connection()
#     create_table(conn)
#     conn.close()
#     return jsonify({"success": True}), 201

def register_routes(app):
    @app.route('/api/data', methods=['POST'])
    def add_data():
        data = request.json.get('data')
        if not data:
            return jsonify({"error": "Missing 'data' field"}), 400
        data_store.insert_data(data)
        return jsonify({"success": True}), 201

    @app.route('/api/data', methods=['GET'])
    def get_data():
        results = data_store.query_data()
        return jsonify(results), 200

