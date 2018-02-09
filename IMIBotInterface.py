from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', test=Flask.static_url_path)


@app.route('/config')
def config():
    return render_template('config.html')


if __name__ == '__main__':
    app.run(debug=True)
