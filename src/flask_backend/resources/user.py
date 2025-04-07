from flask_restful import Resource

class UserResource(Resource):
    def get(self, user_id=None):
        """ 获取用户信息（支持单个用户和所有用户）"""
        if user_id:
            return {"user": f"User {user_id}"}
        else:
            return {"users": ["user1", "user2"]}

    def post(self):
        """ 创建新用户 """
        return {"message": "User created"}, 201

    def put(self, user_id):
        """ 更新用户信息 """
        return {"message": f"User {user_id} updated"}

    def delete(self, user_id):
        """ 删除用户 """
        return {"message": f"User {user_id} deleted"}
