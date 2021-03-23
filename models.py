from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, BigInteger,Boolean
from sqlalchemy import sql

metadata = MetaData()
chanels_table = Table ('chanels',
                       metadata,
                       Column('id', Integer, primary_key=True),
                       Column('title', String(256)),
                       Column('icon', String(256)),
                       Column('disabled', Boolean, server_default=sql.expression.false())
                       )
shows_table = Table ('shows',
                     metadata,
                     Column('id', BigInteger, primary_key=True),
                     Column('title', String(256)),
                     Column('description',Text),
                     Column('start_t', DateTime),
                     Column('end_t', DateTime),
                     Column('chanel_id',Integer)
                     )
