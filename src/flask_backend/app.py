from flask import Flask, jsonify, request
from flask_backend.controllers.web import web_bp  # 导入控制器蓝图
from flask_migrate import Migrate
from flask_backend.database import db
from flask_backend.models import *
app = Flask(__name__)
# 注册蓝图到主应用
app.register_blueprint(web_bp)

# 数据库model变更，数据库进行变更
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({"message": "Flask Backend Service Running!"})


if __name__ == "__main__":
    # 创建数据库表（首次运行时）
    # conn = get_db_connection()
    # create_table(conn)
    # conn.close()

    # 路由需要在应用的实际运行上下文中进行注册
    # 在实际运行（例如通过 app.run()）前，所有的路由都应该已经注册完毕。
    from flask_backend.controllers.web.data_store  import  register_routes
    register_routes(app)
    app.run(host="0.0.0.0", port=5001, debug=True)
