from flask_backend.database import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200))  # 新添加的字段

    def __repr__(self):
        return f'<User {self.username}>'

    @property
    def get_user(self):
        """ 获取当前用户对象 """
        return User.query.filter_by(id=self.id).first()

    @classmethod
    def get_users(cls):
        """ 获取所有用户对象 """
        return cls.query.all()

    @classmethod
    def insert_user(cls, username, email, address):
        """ 插入新用户 """
        new_user = cls(username=username, email=email, address=address)
        db.session.add(new_user)
        db.session.commit()  # 直接提交（flush 在 commit 前自动调用）
        return new_user

    @classmethod
    def update_user(cls, user_id, **kwargs):
        """ 更新用户信息 """
        user = cls.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
            return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        """ 删除用户 """
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False


    def to_dict(self):
        """转换模型实例为字典"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'address': self.address,
        }