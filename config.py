from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
