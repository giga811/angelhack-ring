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


# user imports
from angelring import app, models, db
from models import Combination
import os


# Spell controllers

# global var for current spell
current_spell = []
www = False

# function for opening url
def www_open_url(current_spell):
    spell = ""
    for s in current_spell:
        spell += str(s)

    combi = Combination.query.filter_by(code1 = int (spell[0])).\
                    filter_by(code2 = int (spell[1])).\
                    filter_by(code3 = int (spell[2])).first()
    if (combi):
        print combi.url
        open_url(combi.url)
    # if spell == "333":
    #     open_url("http://reraku.jp/")
    # if spell == "334":
    #     open_url("http://angelhack.com/hackathon/tokyo-spring-2015/")
    # if spell == "335":
    #     open_url("http://www.tokyoartmuseum.com/")
    # if spell == "344":
    #     open_url("https://www.facebook.com/reraku")

def open_url(url):
    cmd="""
    osascript -e 'tell application "Safari"
    activate
    open location "{url}"
    end tell'
    """.format(url=url)
    os.system(cmd)


# api for normal spell
# also triggers www
@app.route('/spell/<int:id>')
def spell_input(id):
    global current_spell
    global www
    current_spell.append(id)
    print "#Current spell is: ", current_spell

    # if www true
    if www and len(current_spell) == 3:
        www_open_url(current_spell)
        reset_spell()
        www = False

    return "ok"

@app.route('/spell/sp/<special>')
def special_spell(special):
    global current_spell
    current_spell.append(special)
    print "#Current spell is: ", current_spell
    return "ok"

@app.route('/spell/uniq/<special>')
def uniq_spell(special):
    global current_spell
    global www
    current_spell = []

    if special == "A":
        open_url("http://localhost:5000/museum")
    if special == "B":
        open_url("http://localhost:5000/massage")

    # for harry potter
    if special == "H":
        open_url("http://localhost:5000/img/hp.png")
    if special == "P":
        open_url("http://localhost:5000/img/hp2.jpg")


    if special == "W":
        reset_spell()
        www = True

    print "#Uniq spell: ", special
    print "#Current spell is: ", current_spell
    return "ok"

@app.route('/spell/get_spell')
def get_spell():
    global current_spell
    print "#Return current spell: ", current_spell
    spell = ""
    for s in current_spell:
        spell += str(s)
    return spell

@app.route('/spell/reset_spell')
def reset_spell():
    global current_spell
    global www
    www = False
    current_spell = []
    print "#Reset current spell: ", current_spell
    return "ok"

@app.route('/spell/show')
def show_spell():
    return render_template('show_spell.html')