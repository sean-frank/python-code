import os 
import configparser


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(ROOT_DIR, ".env")

print(ENV_FILE)

def get_config():
    config = configparser.ConfigParser()
    config.read(ENV_FILE)
    
    config.read('config.ini')
    key = config.get('DEFAULT','YT_KEY')
    return key
