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

## Reference

* [Building-beautiful-restful-apis...](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)
* [virtualenv](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)
* [pyvenv or venv](https://docs.python.org/3/library/venv.html)
