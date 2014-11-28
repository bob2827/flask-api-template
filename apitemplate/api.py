import flask
from flask import g as flaskGlobals
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

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

class sessionCtx(object):
    def __init__(self, sql, redis):
        self.sql = sql
        self.redis = redis

@contextlib.contextmanager
def sessionContext():
    if not hasattr(flaskGlobals, 'redisCon'):
        r = redis.StrictRedis(**settings.REDIS_CONFIG)
        flaskGlobals.redisCon = r

    if not hasattr(flaskGlobals, 'dbSessionGen'):
        engine = sqla.create_engine(settings.SQL_CONFIG)
        #con = engine.connect()
        tables.Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        flaskGlobals.dbEngine = engine
        flaskGlobals.dbSessionGen = Session

    dbCtx = sessionCtx(flaskGlobals.dbSessionGen(), flaskGlobals.redisCon)
    yield dbCtx
    dbCtx.sql.close()

def closeEngine(error):
    pass

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
    def get(self, intarg):
        with sessionContext() as ctx:
            #tables.Name.__table__.insert({'col2': 'name'})
            ctx.sql.add(tables.Name(col2='adfa'))
            ctx.sql.commit()
            q = ctx.sql.query(tables.Name).filter(tables.Name.col1 == 1)
            e = q.first()
            return recordToDict(e)

    def put(self, intarg):
        with sessionContext() as ctx:
            d = json.loads(request.data)
            d['goodput'] = 'bro'
            return d

    def post(self, intarg):
        with sessionContext() as ctx:
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
