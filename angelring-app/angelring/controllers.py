"""
2015/06/27
Angelhack app
angelring
"""

# flask imports
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash,\
    _app_ctx_stack, jsonify, send_from_directory
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.restful import reqparse, abort, Api, Resource
import json
import random


# user imports
from angelring import app, db, models
import os
from .forms import GenerateForm
from models import Combination
from random import randint

# code to run appscript

def keyCode(keycode):
    cmd = """
    osascript -e 'tell application "System Events"
    key code """ + keycode + """
    end tell'
    """
    os.system(cmd)

@app.route('/slideshow')
def slideshow():
    cmd = """
    osascript -e '
    tell application "Microsoft PowerPoint"
    delay 1
    set slideShowSettings to slide show settings of active presentation
    run slide show slideShowSettings
    end tell'
    """
    os.system(cmd)
    print "Go slideshow"
    return "ok"

@app.route('/right')
def goright():
    keyCode("124")
    print "Go right"
    return "ok"

@app.route('/left')
def goleft():
    keyCode("123")
    print "Go left"
    return "ok"



# route for INDEX
@app.route("/")
def hello():
    return render_template('index.html')

# api
@app.route("/api/test")
def get_sensor():
    return "200"

# tests

test_i = 0
@app.route('/test')
def test_page():
    global test_i
    test_i += 123
    print test_i
    return "ok"

# get mail
@app.route('/generate/', methods=['GET', 'POST'])
def generate():
    form = GenerateForm()
    links = Combination.query.all()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('generate.html', form=form)
        else:
            link = Combination.query.filter_by(url = form.url.data).first()
            if link is None:
                found = False
                code = [1, 1, 1]
                while found is False:
                    code = random.sample([1, 2, 3, 4], 3)
                    # combi = db.Combination.query.filter(
                    #     db.Combination.code1 == code[0], 
                    #     db.Combination.code2 == code[1],
                    #     db.Combination.code3 == code[2]).first()
                    combi = Combination.query.filter_by(code1 = code[0]).first()
                    if combi is None:
                        new_link = Combination(
                            code1 = code[0],
                            code2 = code[1],
                            code3 = code[2],
                            url = form.url.data
                            )
                        db.session.add(new_link)
                        db.session.commit()
                        found = True

                return render_template('generate.html', success = True, code = code, links = links)
            codes = [int(link.code1), int(link.code2), int(link.code3)]
            return render_template('generate.html', already = True, code = codes, links = links)

    return render_template('generate.html', form=form, links = links)

@app.route('/seedb/')
def seedb():
    combi = Combination.query.all()
    return render_template('seedb.html', data = combi)

# @app.route('/populate/')
# def populate():
#     for code1 in range(1, 10):
#         for code2 in range(1, 10):
#             for code3 in range(1, 10):

### static file helpers
# route for static js, css files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)
@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory(app.static_folder + '/fonts', path)
@app.route('/font-awesome/<path:path>')
def send_fontawesome(path):
    return send_from_directory(app.static_folder + '/font-awesome', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(app.static_folder + '/img', path)
@app.route('/less/<path:path>')
def send_less(path):
    return send_from_directory(app.static_folder + '/less', path)
