web: python manage_prod.py syncdb
web: python manage_prod.py collectstatic --noinput
web: gunicorn receipt_tracker.wsgi_prod
