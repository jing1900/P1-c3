#-*-encoding=UTF-8-*-
'''放导出信息的'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#先把app建起来
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
#设置config
app.config.from_pyfile('app.conf')

#定义数据库
db = SQLAlchemy(app)

#导出view
from stagram import views
from stagram import models