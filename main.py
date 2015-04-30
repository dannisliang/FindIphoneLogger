from pyicloud import PyiCloudService
from settings import *



api = PyiCloudService(LOGIN, PASS)
print(api.iphone.location())