from setuptools import setup, find_packages

setup(
    name='connex_rest_demo',
    version='1.0.0',
    description='Boilerplate code for a RESTful API based on Connexion',
    url='https://github.com/realpython/materials/tree/master/flask-connexion-rest-part-3',
    author='Doug Farrell',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rest restful api flask swagger openapi connexion',

    packages=find_packages(),

    install_requires=['certifi==2022.12.7', 'chardet==3.0.4', 'Click==7.0',
    'clickclick==1.2.2', 'connexion==2.2.0', 'Flask==1.0.2', 'flask-marshmallow==0.9.0',
    'Flask-SQLAlchemy==2.3.2', 'idna==2.8', 'inflection==0.3.1', 'itsdangerous==1.1.0',
    'Jinja2==2.10', 'jsonschema==2.6.0', 'MarkupSafe==1.1.0', 'marshmallow==2.18.0',
    'marshmallow-sqlalchemy==0.15.0', 'openapi-spec-validator==0.2.4', 'pathlib==1.0.1',
    'PyYAML==4.2b4', 'requests==2.21.0', 'six==1.12.0', 'SQLAlchemy==1.2.17', 'swagger-ui-bundle==0.0.3',
    'urllib3==1.24.1', 'Werkzeug==0.14.1'],
)
