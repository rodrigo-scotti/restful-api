# -*- coding: utf-8 -*-

from flask import Flask
from config import config

from apps.controllers.api import configure_api


def create_app(config_name):
  app = Flask('config-template')

  app.config.from_object(config[config_name])

  configure_api(app)

  return app

