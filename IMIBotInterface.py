from flask import jsonify, request, render_template, Flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', test=request.base_url)


@app.route('/config')
def config():
    return render_template('config.html')


@app.route('/_move')
def move():
    angle = request.args.get('angle', 0, type=float)
    strength = request.args.get('strength', 0, type=float)
    # handler.move(angle, strength)
    return jsonify(angle, strength)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

