from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/callback')
def callback():
    return 'callback'

if __name__ == '__main__':
    app.debug = True
    app.run()

