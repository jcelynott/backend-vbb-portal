release: python manage.py migrate
release: python manage.py collectstatic --noinput;

web: python manage.py runserver "0.0.0.0:$PORT" 