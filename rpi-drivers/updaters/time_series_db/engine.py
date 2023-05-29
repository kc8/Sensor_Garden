#SQL Alchemy engine for connecting to the DB.
from sqlalchemy.orm import sessionmaker, backref, relationship
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import os, json

# Connect to DB with engine:

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONNECTION_FILE = BASE_DIR+"/updaters/times_series_db/db_info.json"
Base = declarative_base()


def get_secret(setting, file):
    """
    Gets are returns a setting value (connection string) from the file
    :param setting: Setting in the JSON file to read
    :param file: File to read the connection string from
    :return: A specific setting from the JSON file
    """
    with open(file) as f:
        secrets = json.load(f)
        try:
            return secrets[setting]
        except KeyError:
            print("Failure to read DB settings")
            _CONNECTION_STRING = ""


_CONNECTION_STRING = str(get_secret("connection_string", _CONNECTION_FILE))
engine = db.create_engine(_CONNECTION_STRING)
Base.metadata.bind = engine
#Create a session sop that we can update the DB
DBSession = sessionmaker(bind=engine)
session = DBSession()
