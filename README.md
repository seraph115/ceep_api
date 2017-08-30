# CEEP API SYSTEM
**ceep_api** system

## Usage

```bash
$ cd /path/to/your/workspace
$ git clone https://github.com/seraph115/ceep_api.git
$ cd ceep_api
```

```bash
$ pyvenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

```bash
$ export PYTHONPATH=.:$PYTHONPATH
$ python ceep_api/app.py
```

## Technology Stack

### Components

* RESTful framework - [flask-restplus](http://flask-restplus.readthedocs.org)
* ORM framework - [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
* DateBase Driver  - [pymysql](https://pymysql.readthedocs.io)

