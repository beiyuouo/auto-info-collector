# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/12 13:20
# Description:

__author__ = "BeiYu"

from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField, SelectField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, Email

from config import config


class UploadForm(FlaskForm):
    group = SelectField(u'组别', choices=config.group_list, id="group")
    date = DateField(u'日期', format="%Y-%m-%d", default=datetime.today(),
                     validators=[DataRequired(message=u'日期不能为空')])
    name = SelectField(u'姓名', choices=config.name_list[0], id="name")
    screenshot_1 = FileField('Upload Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    screenshot_2 = FileField('Upload Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    screenshot_3 = FileField('Upload Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()
    name_list = config.name_list

