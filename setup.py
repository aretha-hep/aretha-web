from setuptools import setup

setup(
    name = 'arethaweb',
    author = 'Luaks Heinrich', 
    author_email = 'lukas.heinrich@cern.ch',
    version = '0.0.1',
    install_requires = [
        'Flask',
        'python-socketio',
        'eventlet',
        'Celery',
        'redis',
        'honcho'
    ]
)
