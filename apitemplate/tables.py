import sqlalchemy as sqla
import sqlalchemy.dialects as dialects
import sqlalchemy.dialects.mysql as mysqlDialect

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool, QueuePool

from sqlalchemy import func
import sqlalchemy.sql.operators as operators

Base = declarative_base()

class Name(Base):
    __tablename__ = "tablename"
    col1 = sqla.Column(sqla.Integer, primary_key=True)
    col2 = sqla.Column(sqla.String(length=1))
    col3 = sqla.Column(sqla.Integer)
    col4 = sqla.Column(mysqlDialect.DECIMAL(5,2))
    col5 = sqla.Column(sqla.types.SMALLINT)
    col6 = sqla.Column(sqla.Text)
    col7 = sqla.Column(sqla.DateTime)
    col8 = sqla.Column(sqla.types.TIMESTAMP)
