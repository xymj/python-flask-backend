from flask_restful import Api
from flask import Blueprint
from .user import UserResource  # 导入资源类

# 创建 Flask Blueprint
web_bp = Blueprint("web", __name__)

# 创建 API 实例并绑定到 Blueprint
api = Api(web_bp)

# 注册资源到路由
api.add_resource(
    UserResource,          # 资源类
    "/api/users",          # 路径 1
    "/api/users/<int:user_id>",  # 路径 2
    methods=["GET", "POST", "PUT", "DELETE"]
)
