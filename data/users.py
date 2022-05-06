import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):

    __tablename__ = 'ord_reg'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nick = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    fio = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    podr = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    _pass = sqlalchemy.Column(sqlalchemy.String(10), nullable=True)
    # hashed_pass = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)

    def __repr__(self):
        return "<ord_reg> " + str(self.id) + ' ' + self.nick + ' ' + self.fio

    # def set_password(self, password):
    #     self.hashed_pass = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.hashed_pass, password)
