web: gunicorn cornershop.wsgi --log-file -
worker: celery worker --app=tasks.app
