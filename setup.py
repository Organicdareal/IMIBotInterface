from setuptools import setup
from IMIBotInterface import app

setup(
    name='IMIBotInterface',
    packages=['IMIBotInterface'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

app.run(host='0.0.0.0', port=5000, debug=True)
