# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import DateField, HiddenField, RadioField, SubmitField, TextField, TextAreaField, BooleanField
from wtforms.validators import Email, EqualTo, Length, Required, AnyOf


class GenerateForm(Form):
    url = TextField(u"Insert Link",  [Required()])

    submit = SubmitField(u"Generate")