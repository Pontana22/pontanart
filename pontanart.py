import os
import redis

from lib.userinput import process_options
from lib.convert import convert
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # ONLY FOR USE WITH LOCALHOST, REMOVE OTHERWISE

app = Flask(__name__)
app.secret_key = ''
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379)
app.config['SESSION_PERMANENT'] = False
Session(app)

SCOPES = ['https://www.googleapis.com/auth/drive.file']
REDIRECT_URI = 'http://localhost:5000/oauth2callback'
CREDENTIALS = './resources/credentials.json'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/options', methods=['POST'])
def options():
    image = request.files['image']
    image_path = os.path.join('./img', image.filename)
    image.save(image_path)
    
    options = dict(request.form)
    process_options(options)
    options['img'] = image_path
    session['options'] = options
    
    if 'credentials' in session:
        return redirect('/create')
    else:
        return redirect('/login')

@app.route('/login')
def login():
    flow = Flow.from_client_secrets_file(CREDENTIALS, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    auth_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true', prompt='consent')
    
    session['state'] = state
    
    return redirect(auth_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']

    flow = Flow.from_client_secrets_file(CREDENTIALS, scopes=SCOPES, redirect_uri=REDIRECT_URI, state=state)
    flow.fetch_token(authorization_response=request.url)

    session['credentials'] = {
        'token': flow.credentials.token,
        'refresh_token': flow.credentials.refresh_token,
        'token_uri': flow.credentials.token_uri,
        'client_id': flow.credentials.client_id,
        'client_secret': flow.credentials.client_secret,
        'scopes': flow.credentials.scopes
    }
    
    return redirect('/create')

@app.route('/create')
def create():
    options = session['options']
    creds = Credentials(**session['credentials'])

    if creds.expired:
        creds.refresh(Request())
    
    convert(options, creds)
    
    os.remove(options['img'])
    
    return render_template('success.html')
