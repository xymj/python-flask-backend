import json

from flask import request, jsonify
from flask_restful import Resource
from flask_backend.models.user import User


class UserResource(Resource):
    def get(self, user_id=None):
        """处理 GET 请求"""
        if user_id:
            user = User(id=user_id).get_user
            # 获取单个用户（如 user_id=123）
            # return {"user": f"User {json.dump(user)}"}
            return {"user": user}
        else:
            users = User.get_users()
            # 获取所有用户列表
            return {"users": users}

    def post(self):
        """处理 POST 请求（创建新用户）"""
        # 假设从请求体中获取用户数据
        request_json = request.get_json(force=True)
        # user_data = {"name": "New User"}
        user_data = User.insert_user(username=request_json['username'], email=request_json['email'],
                                     address=request_json['address'])
        return {"message": "User created", "data": user_data.to_dict()}, 201

    def put(self, user_id):
        """处理 PUT 请求（更新用户）"""
        # 更新用户信息（如修改 user_id 对应的数据）
        request_json = request.get_json(force=True)
        user_data = User.update_user(user_id=user_id, **request_json)
        return {"message": "User updated", "data": user_data.to_dict()}, 200

    def delete(self, user_id):
        """处理 DELETE 请求（删除用户）"""
        res = User.delete_user(user_id)
        return {"message": f"User {user_id} deleted is {res}"}
