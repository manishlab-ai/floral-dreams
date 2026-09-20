import os
import sys
from django.core.wsgi import get_wsgi_application

# रूट डायरेक्टरी को पाथ में जोड़ना
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
application = get_wsgi_application()
