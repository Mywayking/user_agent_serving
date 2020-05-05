import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
    # 设置这一项是每次请求结束后都会自动提交数据库中的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.1.70:3306/api_inner?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://galen:123!@192.168.1.14:3306/api_inner?charset=utf8'


config = {
    'testing': TestingConfig,
    'Production': ProductionConfig,
}
