import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

severity = Table(
    'severity',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('severitylevel', String(255))
)

period = Table(
    'period',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('severity', Integer),
    Column('perioddatetime', String(255))
)

category = Table(
    'category',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('name', String(255))
)

subcategory = Table(
    'subcategory',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('category', Integer),
    Column('name', String(255))
)

template = Table(
    'template',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('category', Integer),
    Column('subcategory', Integer),
    Column('stringtemplate', String(255))
)

campaign = Table(
    'campaign',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('template', Integer),
    Column('period', Integer),
    Column('name', String(255))
)

campaignanalytics = Table(
    'campaignanalytics',
    metadata,
    Column('uniqueid', Integer, primary_key=True),
    Column('campaign', Integer),
    Column('total', String(150)),
    Column('sent', String(150)),
    Column('opened', String(150)),
    Column('clicked', String(150)),
    Column('submiteddata', String(150)),
    Column('error', String(150))

)

database = Database(DATABASE_URI)