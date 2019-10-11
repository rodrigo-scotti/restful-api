# -*- coding: utf-8 -*-

from os import getenv


class Config:
	SECRET_KEY = getenv('SECRET_KEY') or b'\x18\xb9\x8b]\x97\x15\x98\n\xafCl\x83-\x13\n0'
	APP_PORT = int(getenv('APP_PORT'))
	DEBUG = eval(getenv('DEBUG').title())


class DevelopmentConfig(Config):
	FLASK_ENV = 'development'
	DEBUG = True


class TestingConfig(Config):
	FLASK_ENV = 'testing'
	TESTING = True


class ProductionConfig(Config):
	FLASK_ENV = 'production'
	TESTING = False
	DEBUG = False


config = {
	'production': ProductionConfig,
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'default': DevelopmentConfig
}
