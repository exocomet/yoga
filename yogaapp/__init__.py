from flask import Flask
from flask import request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return render_template('register.html')



if __name__ == '__main__':
    app.run()