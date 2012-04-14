import os
BASE_PATH = os.path.abspath(__file__)
for i in range(2):
    BASE_PATH = os.path.dirname(BASE_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
