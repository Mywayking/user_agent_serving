from datetime import datetime
from app import db


class DeviceUa(db.Model):
    __tablename__ = 'device_ua'  # 表名
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)  # autoincrement 表示自增
    user_agent = db.Column(db.Text(), index=True, unique=False)
    brand = db.Column(db.String(320), index=True, unique=False)
    # pub_date = db.Column(db.DateTime(320), nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.brand)

#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
