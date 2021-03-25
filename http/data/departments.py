import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Department(SqlAlchemyBase):
    __tablename__ = 'Department'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    dep_chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)

    chief = orm.relation('User')

    def __repr__(self):
        return f'<Job> {self.job}'
