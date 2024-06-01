# faker-data

## GUNICORN

    gunicorn -w 4 -b 0.0.0.0 'app:create_app()'