# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/11 14:47
# Description:

__author__ = "BeiYu"

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length, regexp
from flask_bootstrap import Bootstrap
import os
from config import *
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['SECRET_KEY'] = 'key'
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    group = SelectField(u'组别', choices=config.group_list)
    date = DateField(u'日期', format="%Y-%m-%d", default=datetime.today(),
                     validators=[DataRequired(message=u'日期不能为空')])
    name = SelectField(u'姓名', choices=config.name_list[0])
    screenshot_1 = FileField(u'截图1')
    screenshot_2 = FileField(u'截图2')
    screenshot_3 = FileField(u'截图3')
    # screenshot_1 = FileField(u'截图1', validators=[
    #     FileRequired(message='第1张截图不能为空'),
    #     FileAllowed(['jpg', 'jpeg', 'png'], message='只能上传jpg, jpeg, png')
    # ])
    # screenshot_2 = FileField(u'截图2', validators=[
    #     FileRequired(message='第2张截图不能为空'),
    #     FileAllowed(['jpg', 'jpeg', 'png'], message='只能上传jpg, jpeg, png')
    # ])
    # screenshot_3 = FileField(u'截图3', validators=[
    #     FileRequired(message='第3张截图不能为空'),
    #     FileAllowed(['jpg', 'jpeg', 'png'], message='只能上传jpg, jpeg, png')
    # ])
    submit = SubmitField(u'提交')


@app.route('/upload', methods=['GET', 'POST'])
def uploader():
    form = LoginForm()
    if form.validate_on_submit():
        # print('miaomiaomiao')
        group_id = int(form.group.data)
        today = form.date.data
        name = form.name.data
        print(group_id, today, name)
        make_today_dirs(today, group_id)

        # TODO
        filename = secure_filename(form.screenshot_1.data.filename)
        form.screenshot_1.data.save(filename)
        print(form.screenshot_1.name)
        print(request.files)
        image_data = request.files[form.screenshot_1.name].read()
        print('get data')
        open(os.path.join(form.screenshot_1.data), 'w').write(image_data)
        form.screenshot_1.data.save('1.jpg')
        f = form.screenshot_1.data
        filename = f'{today}-{name}-{1}'
        f.save(os.path.join('database', str(group_id), today, name, filename))

        f = form.screenshot_2.data
        filename = f'{today}-{name}-{2}'
        f.save(os.path.join('database', str(group_id), today, name, filename))

        f = form.screenshot_3.data
        filename = f'{today}-{name}-{3}'
        f.save(os.path.join('database', str(group_id), today, name, filename))
        return redirect(url_for('success'))

    return render_template('upload.html', form=form)


@app.route('/success')
def success():
    return '<h1>Success</h1>'


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
