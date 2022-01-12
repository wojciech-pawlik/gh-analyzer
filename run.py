import flask
from flask import Flask, url_for, redirect
from flask_github import request
from flask_dance.contrib.github import make_github_blueprint, github
import os

from gh_analyzer import analyzer


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////login.db'

app.config['GITHUB_CLIENT_ID'] = '846c0a7bbc9a615b3a5f'
app.config['GITHUB_CLIENT_SECRET'] = '113d13e1a518b61e547e06daba6e7455f9a495e2'

github_blueprint = make_github_blueprint(client_id=app.config['GITHUB_CLIENT_ID'],
                                         client_secret=app.config['GITHUB_CLIENT_SECRET'])
app.register_blueprint(github_blueprint, url_prefix='/github_login')

LOGGED_AS = ''
BUTTON_MODE = ''


@app.route('/')
def index():
    global BUTTON_MODE
    global LOGGED_AS
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            LOGGED_AS = account_info_json['login']
            return flask.render_template('index.html', logged_as=LOGGED_AS, button_mode=BUTTON_MODE)
    return flask.render_template('index.html')


@app.route('/list', methods=['POST'])
def list_repos():
    global BUTTON_MODE
    global LOGGED_AS
    if request.method == 'POST':
        username = request.form.get('username')
        token = github_blueprint.token['access_token']
        if request.form['list_button'] == 'List repos':
            BUTTON_MODE = 'repos'
            message = analyzer.list_repos(username=username, token=token)
            return flask.render_template('index.html', username=username, list_repos=message, logged_as=LOGGED_AS, button_mode=BUTTON_MODE)
        elif request.form['list_button'] == 'List languages':
            BUTTON_MODE = 'languages'
            message = analyzer.repos_language_percentage(username=username, token=token)
            return flask.render_template('index.html', username=username, list_repos=message, logged_as=LOGGED_AS, button_mode=BUTTON_MODE)
    BUTTON_MODE = ''
    return flask.render_template('index.html', list_repos='', logged_as=LOGGED_AS, button_mode=BUTTON_MODE)


if __name__ == '__main__':
    app.run()
