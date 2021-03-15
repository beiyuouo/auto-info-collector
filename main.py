# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/11 14:47
# Description:

__author__ = "BeiYu"
import os
import uuid

from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session, jsonify
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError

from forms import UploadForm

from config import config

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Custom config
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']

# Flask config
# set request body's max length
# app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # 3Mb

# Flask-CKEditor config
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload_for_ckeditor'

# Flask-Dropzone config
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 3
app.config['DROPZONE_MAX_FILES'] = 30


@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        group_id = str(form.group.data)
        name = str(form.name.data)
        date = str(form.date.data)
        # print(group_id, name, date)
        make_today_dirs(date, int(group_id))

        f = form.screenshot_1.data
        # filename = random_filename(f.filename)
        ext = os.path.splitext(f.filename)[1]
        filename = os.path.join(group_id, date, name, f'{date}-{name}-{1}'+ext)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        f = form.screenshot_2.data
        # filename = random_filename(f.filename)
        ext = os.path.splitext(f.filename)[1]
        filename = os.path.join(group_id, date, name, f'{date}-{name}-{2}' + ext)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        f = form.screenshot_3.data
        # filename = random_filename(f.filename)
        ext = os.path.splitext(f.filename)[1]
        filename = os.path.join(group_id, date, name, f'{date}-{name}-{3}' + ext)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        flash('Upload success.')
        session['filenames'] = [filename]
        return render_template('upload.html', form=form)
    return render_template('upload.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return "<h2>Success</h2>"


@app.route('/name', methods=['GET', 'POST'])
def query_name():
    group_id = request.args.get("group")
    print(group_id)
    if not group_id:
        group_id = 0
    return jsonify({'data': config.name_list[int(group_id)]})


def make_today_dirs(today: str, group_id: int):
    print(config.name_list[group_id-1])
    for name in config.name_list[group_id-1]:
        print(f'make dirs: {group_id, today, name}')
        os.makedirs(os.path.join(app.config['UPLOAD_PATH'], str(group_id), today, name), exist_ok=True)
    pass


def init_env():
    for i in config.group_list:
        os.makedirs(os.path.join(app.config['UPLOAD_PATH'], str(i)), exist_ok=True)
        # print(f'mkdir: {i}')
    pass


if __name__ == '__main__':
    init_env()
    app.run(host=config.host, port=config.port, debug=config.debug)
