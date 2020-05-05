from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
import pymysql

pymysql.install_as_MySQLdb()


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://galen:123!@192.168.1.14:3306/api_inner?charset=utf8'
# # app.config[
# #     'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.1.70:3306/api_inner?charset=utf8'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
# # 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
config_name = "Production"
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config[config_name])
config[config_name].init_app(app)
db.init_app(app)

from app import routes, models, identify, utils