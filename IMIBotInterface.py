from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', test="YO RAP !")


@app.route('/config')
def config():
    return render_template('config.html')


if __name__ == '__main__':
    app.run(debug=True)
