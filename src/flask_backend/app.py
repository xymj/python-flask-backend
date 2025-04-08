from flask import Flask, jsonify, request
from flask_backend.db import get_db_connection, create_table, insert_data, query_data
from flask_backend.controllers.web import web_bp  # 导入控制器蓝图

app = Flask(__name__)
# 注册蓝图到主应用
app.register_blueprint(web_bp)

@app.route('/')
def index():
    return jsonify({"message": "Flask Backend Service Running!"})

@app.route('/api/table/create', methods=['GET'])
def create_db_table():
    conn = get_db_connection()
    create_table(conn)
    conn.close()
    return jsonify({"success": True}), 201

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "Missing 'data' field"}), 400
    conn = get_db_connection()
    insert_data(conn, data)
    conn.close()
    return jsonify({"success": True}), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    results = query_data(conn)
    conn.close()
    return jsonify(results), 200




if __name__ == "__main__":
    # 创建数据库表（首次运行时）
    # conn = get_db_connection()
    # create_table(conn)
    # conn.close()
    app.run(host="0.0.0.0", port=5001, debug=True)
