from base.bases import Base
import os

import requests
from requests import Session
import configparser as cp


config=cp.ConfigParser()
root_dir = os.path.dirname(os.path.abspath('.'))
# print(root_dir)
print(root_dir.split('\\')[-1]=='testys')
path=root_dir+'\conf\config.ini'
print(path)
