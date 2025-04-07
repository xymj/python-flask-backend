from flask_restful import Resource

class UserResource(Resource):
    def get(self, user_id=None):
        """处理 GET 请求"""
        if user_id:
            # 获取单个用户（如 user_id=123）
            return {"user": f"User {user_id}"}
        else:
            # 获取所有用户列表
            return {"users": ["Alice", "Bob", "Charlie"]}

    def post(self):
        """处理 POST 请求（创建新用户）"""
        # 假设从请求体中获取用户数据
        user_data = {"name": "New User"}
        return {"message": "User created", "data": user_data}, 201

    def put(self, user_id):
        """处理 PUT 请求（更新用户）"""
        # 更新用户信息（如修改 user_id 对应的数据）
        return {"message": f"User {user_id} updated"}

    def delete(self, user_id):
        """处理 DELETE 请求（删除用户）"""
        return {"message": f"User {user_id} deleted"}
