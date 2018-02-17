from IMIBotInterface import app
from flask import Flask, jsonify, request, render_template
from IMIBotInterface.ControlsHandler import ControlsHandler

handler = ControlsHandler()

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
    handler.move(angle, strength)
    return jsonify(angle, strength)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

