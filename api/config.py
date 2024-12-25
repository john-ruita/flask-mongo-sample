import os

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    MONGO_URI = os.getenv("MONGO_TEST_URI")
