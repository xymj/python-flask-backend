在 Flask Web 项目中，使用 flask_restful.Api 可以快速创建 RESTful API，并通过 资源类（Resource） 和 路由映射 来组织代码。以下是具体实现步骤：

1. 安装依赖
确保已安装 flask_restful：
bash


poetry add flask flask-restful

2. 创建基本结构
项目目录结构示例：
my_flask_app/
├── app.py          # 主应用入口
├── resources/      # 存放资源类的目录
│   └── user.py     # 用户资源类示例
└── requirements.txt

3. 定义资源类（Resource）
每个资源类对应一个业务实体（如用户、文章等），并实现 HTTP 方法（get, post, put, delete 等）。
示例：用户资源类 user.py
python


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

4. 初始化 Flask 应用并注册资源
在主应用文件（如 app.py）中配置路由：
python


from flask import Flask
from flask_restful import Api
from resources.user import UserResource  # 导入资源类

app = Flask(__name__)
api = Api(app)

# 注册资源到 API，关联路由和 HTTP 方法
# 语法：api.add_resource(资源类, 路径, **kwargs)
api.add_resource(
    UserResource,          # 资源类
    "/api/users",          # 基础路径
    "/api/users/<int:user_id>",  # 动态路径参数
    methods=["GET", "POST", "PUT", "DELETE"],  # 允许的方法（可选）
    endpoint="user"        # 自定义端点名称（可选）
)

if __name__ == "__main__":
    app.run(debug=True)

5. 路由映射规则
add_resource 的路径和方法会自动关联到资源类的 HTTP 方法：
● 路径 /api/users：
  ○ GET → UserResource.get()（无 user_id）
  ○ POST → UserResource.post()
● 路径 /api/users/123：
  ○ GET → UserResource.get(user_id=123)
  ○ PUT → UserResource.put(user_id=123)
  ○ DELETE → UserResource.delete(user_id=123)

6. 自定义方法映射
如果需要更细粒度的控制，可以通过 methods 和 defaults 参数指定：
python


api.add_resource(
    UserResource,
    "/api/users",
    "/api/users/<int:user_id>",
    methods={"GET", "POST"},  # 限制允许的方法
    defaults={"user_id": 0}   # 默认参数值
)

7. 请求参数处理
路径参数
在资源类方法中直接接收动态参数：
python


def get(self, user_id):
    return {"user_id": user_id}
查询参数
通过 request.args 获取：
python


from flask import request

def get(self):
    page = request.args.get("page", 1)
    return {"page": page}
请求体（POST/PUT）
通过 request.json 获取 JSON 数据：
python


def post(self):
    data = request.json
    return {"received": data}, 201

8. 完整示例
app.py
python


from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# 定义资源类
class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            return {"user": f"User {user_id}"}
        return {"users": ["Alice", "Bob"]}

    def post(self):
        data = request.json
        return {"message": f"User {data['name']} created"}, 201

# 注册资源
api.add_resource(
    UserResource,
    "/api/users",
    "/api/users/<int:user_id>",
    methods=["GET", "POST", "PUT", "DELETE"]
)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

9. 测试接口
GET 请求
● 获取所有用户：
bash


curl http://localhost:5000/api/users
# 输出：{"users": ["Alice", "Bob"]}
● 获取单个用户：
bash


curl http://localhost:5000/api/users/123
# 输出：{"user": "User 123"}
POST 请求
bash


curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Charlie"}' \
  http://localhost:5000/api/users
# 输出：{"message": "User Charlie created"}

关键点总结
1. 资源类继承 Resource：每个资源对应一个业务实体。
2. api.add_resource：将资源类与路由路径关联。
3. HTTP 方法映射：通过类方法名（get, post）自动匹配 HTTP 方法。
4. 动态路径参数：通过 <参数名> 在路径中定义，参数会自动传递给方法。
通过这种方式，你可以快速构建结构清晰、符合 RESTful 规范的 API。


