# app/train.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from model import add_training_example

train_blueprint = Blueprint('train', __name__)

TRAIN_USERNAME = 'train_user'
TRAIN_PASSWORD = 'train_pass'

@train_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == TRAIN_USERNAME and password == TRAIN_PASSWORD:
            session['logged_in_train'] = True
            return redirect(url_for('train.train_model'))
    return render_template('train_login.html')

@train_blueprint.route('/logout')
def logout():
    session.pop('logged_in_train', None)
    return redirect(url_for('train.login'))

@train_blueprint.route('/', methods=['GET', 'POST'])
def train_model():
    if not session.get('logged_in_train'):
        return redirect(url_for('train.login'))
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        context = request.form.get('context', '')
        add_training_example(question, answer, context)
        return render_template('train.html', success=True)
    return render_template('train.html', success=False)

