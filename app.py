# from datafoo import get_data
from flask import Flask
from flask import render_template
from datafoo import get_data

recalls_data = get_data()
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', recalls_count=len(recalls_data), recalls=recalls_data)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
