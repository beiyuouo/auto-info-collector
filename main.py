# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/11 14:47
# Description:

__author__ = "BeiYu"

import logging
import os

from flask import Flask, send_from_directory, request, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

from config import config

app = Flask(__name__)
bootstrap = Bootstrap(app)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


@app.route('/uploader', methods=['POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.files['image']
        img_name = secure_filename(img.filename)
        create_new_folder(app.config['UPLOAD_FOLDER'])
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'], img_name, as_attachment=True)
    else:
        return "Where is the image?"


@app.route('/', methods=['POST', 'GET'])
def index_page():
    return render_template('upload.html')


def make_today_dirs(today: str, group_id: int):
    for name in config.name_list[group_id]:
        os.makedirs(os.path.join('database', str(group_id), today, name), exist_ok=True)
    pass


def init_env():
    for i in config.group_list:
        os.makedirs(os.path.join('database', i), exist_ok=True)
    pass


if __name__ == '__main__':
    init_env()
    app.run(host=config.host, port=config.port, debug=config.debug)
