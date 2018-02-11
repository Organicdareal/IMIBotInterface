from setuptools import setup

setup(
    name='IMIBotInterface',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)