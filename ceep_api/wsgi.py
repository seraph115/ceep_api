from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from app import initialize_app

app = Flask(__name__)
app = ProxyFix(app)
initialize_app(app)
 
@app.route('/')
def hello():
    return "Hello world!"
 
if __name__ == '__main__':
    log.info('>>>>> Starting development server')
    app.run(debug=true)
