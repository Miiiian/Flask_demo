# -*- coding: utf-8 -*-
#公用配置
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SECRET_KEY = "123456imooc"
SQLALCHEMY_DATABASE_URI = "mysql://root:010328@127.0.0.1/movie_cat"

DOMAIN = {
    "www":"http://192.168.13.1:5000"
}



#RELEASE_PATH = "H:\PythonMian\PycharmDemo\release_version"