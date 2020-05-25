import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Stores credential information
GIT_USER_ID='test'
GIT_USER_PASSWORD='test'


# Google Drive API, credentials
GOOGLE_SERVICE_KEY=basedir+'/instance/pubapi.json'
GOOGLE_SPREADSHEET_NAME = 'publicdata'
GOOGLE_WORKSHEET = 'Sheet'

# PUBLIC_DATA_SERVICE_KEY
PUBLIC_DATA_SERVICE_KEY = "Your-Public-Data-Service-Key"
PUBLIC_DATA_REQUEST_URL = "Your-data-request-url"

# Air Pollution
STATION = "Station-name"

# SIMULATION_MODE
SIMULATION_MODE = 'REAL_TIME'

# SIMULATION_MODEL
REQUEST_FREQ = 30



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
     TESTING = True

class ProductionConfig(Config): pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
