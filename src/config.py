
from urllib.parse import quote
import os
from dotenv import load_dotenv, find_dotenv



class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "xxx"

class DevelopmentConfig(Config):
    # carrega .env.local caso exista
    base_path = os.path.dirname(os.path.abspath(__file__))
    INPUT_PATH = os.path.join(base_path, 'input')
    OUTPUT_PATH = os.path.join(base_path, 'output')
    
    
    # local_env_path = os.path.join(base_path, '.env.localhost')
    # if os.path.isfile(local_env_path):
    #     load_dotenv(find_dotenv(local_env_path))
    # else:
    #     load_dotenv(find_dotenv())

    #username = os.getenv("API_CONTRATOS_DB_USERNAME")
    # password = os.getenv("API_CONTRATOS_DB_PASSWORD")
    # db_name = "api_lig_contratos"
    # password_encoded = quote(password)
    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("API_CONTRATOS_DB_USERNAME")}:%s@{os.getenv("API_CONTRATOS_DB_HOST")}:3306/{os.getenv("API_CONTRATOS_DB_DATABASE")}' % quote(f'{os.getenv("API_CONTRATOS_DB_PASSWORD")}')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
    # ALLOWED_EXTENSIONS = {"zip"}
    # UPLOAD_FOLDER = f"{base_path}/lote/itau"
    # SEND_FILE_MAX_AGE_DEFAULT = 0
    # BASE_PATH = f"{base_path}"