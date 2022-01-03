import datetime

import sqlalchemy

from .base import metadata

users = sqlalchemy.Table('users',
                         metadata,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
                         sqlalchemy.Column('email', sqlalchemy.String, primary_key=True, unique=True),
                         sqlalchemy.Column('username', sqlalchemy.String, unique=True),
                         sqlalchemy.Column('status', sqlalchemy.String, nullable=True),
                         sqlalchemy.Column('avatar', sqlalchemy.String, nullable=True),
                         sqlalchemy.Column('hashed_password', sqlalchemy.String),
                         sqlalchemy.Column('is_staff', sqlalchemy.Boolean, default=False),
                         sqlalchemy.Column('is_active', sqlalchemy.Boolean, default=True),
                         sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                         sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                         )
