# -*- coding: utf-8 -*-

from flask import Flask, session, g
from .models import User


def create_app():
    # 创建flask app
    app = Flask(__name__)

    # 加载配置
    from .config import Config
    from .extensions import db, markdown
    from .helper import siteconfig, categories, menus

    app.config.from_object(Config)
    db.init_app(app)
    app.jinja_env.globals.update(site=siteconfig, site_categories=categories, menus=menus, enumerate=enumerate)
    app.jinja_env.filters['markdown'] = markdown.convert

    # 注册蓝图/视图
    from .views import home
    app.register_blueprint(home)

    return app

