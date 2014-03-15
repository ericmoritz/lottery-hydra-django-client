import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery_hydra.demo_settings")
os.environ.setdefault("CONFIG_IRL", "file://{cwd}/config.ttl".format(cwd=os.getcwd()))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
