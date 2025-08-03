

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Text_to_SQL_project.settings')

application = get_asgi_application()
