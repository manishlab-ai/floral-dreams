import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "floral_dreams_project.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
