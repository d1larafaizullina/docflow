from datetime import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Docs(SqlAlchemyBase, SerializerMixin):

    __tablename__ = 'docs'
    doc_id = sqlalchemy.Column(sqlalchemy.Integer,
                               primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    dt = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String(250), nullable=False)
    number = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    path = sqlalchemy.Column(sqlalchemy.String(200))
    signed = sqlalchemy.Column(sqlalchemy.String(100))
    control = sqlalchemy.Column(sqlalchemy.String(100))
    contra = sqlalchemy.Column(sqlalchemy.String(10))
    istoch = sqlalchemy.Column(sqlalchemy.String(200))
    visa = sqlalchemy.Column(sqlalchemy.String(300))
    p_number = sqlalchemy.Column(sqlalchemy.String(50))
    dt_reg = sqlalchemy.Column(sqlalchemy.DateTime)
    sender = sqlalchemy.Column(sqlalchemy.String(250))
    primech = sqlalchemy.Column(sqlalchemy.String(250))
