# api/wsgi.py
from vercel_wsgi import make_wsgi_app
from signing_service.wsgi import application

app = make_wsgi_app(application)
