import flask
from flask import g as flaskGlobals
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with

import contextlib
import datetime
import json

import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker
import redis

import apitemplate.tables as tables
import apitemplate.settings as settings

#import flask.ext.stormpath as strmpath
#from flask.ext.cors import CORS

@contextlib.contextmanager
def redisContext():
    if not hasattr(flaskGlobals, 'redisCon'):
        r = redis.StrictRedis(**settings.REDIS_CONFIG)
        flaskGlobals.redisCon = r

    yield flaskGlobals.redisCon

@contextlib.contextmanager
def sqlContext():
    if not hasattr(flaskGlobals, 'sqlSessionGen'):
        engine = sqla.create_engine(settings.SQL_CONFIG)
        #con = engine.connect()
        tables.Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        flaskGlobals.sqlEngine = engine
        flaskGlobals.sqlSessionGen = Session

    session = flaskGlobals.sqlSessionGen()
    yield session
    session.close()

@contextlib.contextmanager
def mongoContext():
    if not hasattr(flaskGlobals, 'mongoClient'):
        flaskGlobals.mongoClient = pymongo.MongoClient(settings.MONGO_HOST,
                                                  settings.MONGO_PORT)
    yield flaskGlobals.mongoClient

def closeEngine(error):
    pass

namefields = {'col1': fields.Integer,
              'col2': fields.String,
              'col3': fields.Integer,
              'col4': fields.Float,
              'col5': fields.Integer,
              'col6': fields.String,
              'col7': fields.DateTime,
              'col8': fields.DateTime}

#TODO - move me
def recordToDict(record):
    d = {}
    for col in record.__table__.columns:
        val = record.__getattribute__(col.name)
        t = type(val)
        if t == datetime.datetime:
            d[col.name] = str(val)
        #if (t == str) or (t == int) or (t == float) or (t == bool):
        else:
            d[col.name] = val
        #else:
            
    return d

def root():
    return flask.render_template('bare.html')

QSparser = reqparse.RequestParser()
QSparser.add_argument('qsarg', type=str)

class restEndpoint(restful.Resource):
    @marshal_with(namefields)
    def get(self, intarg):
        with sqlContext() as sql:
            #tables.Name.__table__.insert({'col2': 'name'})
            sql.add(tables.Name(col2='adfa', col3=123, col4=12.34, col5=10,
            col6="text", col7=datetime.date.today(), col8=datetime.date.today()))
            sql.commit()
            q = sql.query(tables.Name).filter(tables.Name.col1 == 1)
            e = q.first()
            return e

    def put(self, intarg):
        d = json.loads(request.data)
        d['goodput'] = 'bro'
        return d

    def post(self, intarg):
        d = json.loads(request.data)
        d['goodpost'] = 'bro'
        return d

def uiEndpoint(uiarg):
    args = QSparser.parse_args()
    try:
        qsarg=args.qsarg
    except:
        qsarg="No Args"

    return flask.render_template('bare.html', qsarg=qsarg, uiarg=uiarg)
