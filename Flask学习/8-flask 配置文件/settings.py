class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    '''生产环境'''
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    '''开发环境'''
    DEBUG = True


class TestingConfig(Config):
    '''测试环境'''
    TESTING = True
