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
from angelring import app
import os


# Spell controllers

# global var for current spell
current_spell = []

@app.route('/spell/<int:id>')
def spell_input(id):
    global current_spell
    current_spell.append(id)
    print "#Current spell is: ", current_spell
    return "ok"

@app.route('/spell/sp/<special>')
def special_spell(special):
    global current_spell
    current_spell.append(special)
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
    current_spell = []
    print "#Reset current spell: ", current_spell
    return "ok"

@app.route('/spell/show')
def show_spell():
    return render_template('show_spell.html')