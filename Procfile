web: python manage.py syncdb
web: newrelic-admin run-program gunicorn --graceful-timeout 120 --timeout 120 --pythonpath receipt_tracker.wsgi
