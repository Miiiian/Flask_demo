# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:010328@127.0.0.1/movie_cat"

SECRET_KEY = "imooc123456"


DOMAIN = {
    "www":"http://192.168.13.1:5000"
}


#RELEASE_PATH = "H:\PythonMian\PycharmDemo\release_version"