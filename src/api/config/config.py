class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/AuthorsProd'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER= 'gabworks51@gmail.com'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'gabworks51@gmail.com'
    MAIL_PASSWORD= 'redeemed@123'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/AuthorsDev'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER= 'gabworks51@gmail.com'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'gabworks51@gmail.com'
    MAIL_PASSWORD= 'redeemed@123'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/AuthorsTest'
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = '234562fgssv999099w@@##%$^%^%^$#AASDFJKKKxgdtf'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'SECRET-KEY-PASSWORD'
    MAIL_DEFAULT_SENDER= 'gabworks51@gmail.com'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'gabworks51@gmail.com'
    MAIL_PASSWORD= 'redeemed@123'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True