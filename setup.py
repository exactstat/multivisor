from setuptools import setup, find_packages

setup(
    name='multivisor',
    version='3.0.3',
    author='Tiago Coutinho',
    author_email='coutinhotiago@gmail.com',
    description='A centralized supervisor web UI',
    packages=find_packages(),
    package_data=dict(multivisor=['dist/*',
                                  'dist/static/css/*',
                                  'dist/static/js/*']),
    entry_points=dict(console_scripts=[
        'multivisor=multivisor.server:main',
        'multivisor-dispatcher=multivisor.dispatcher:main']),
    install_requires=['flask', 'louie', 'gevent', 'supervisor'])