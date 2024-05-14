# Local set-up

## Requirements

- Python (v3.10+)
- PostgreSQL
- ChatGPT API key (or three) - [https://platform.openai.com/](https://platform.openai.com/)


## Project

1. Clone the project repo

1. Create `.env` file based on the `.env.example` file and fill in the required information

1. Set up a python environment, e.g. using virtualenv and pyenv:

    ```
    virtualenv env --python=$HOME/.pyenv/versions/3.10.9/bin/python
    source env/bin/activate
    ```

1. Install python dependencies:

    ```
    pip install -r requirements.txt
    ```


1. Set up a local postgres database, e.g. on macOS using Postgres.app:

    ```
    /Applications/Postgres.app/Contents/Versions/15/bin/psql -p5432
    CREATE DATABASE app_db;
    \c app_db;
    CREATE USER app_user WITH PASSWORD 'app_pw';
    GRANT ALL PRIVILEGES ON DATABASE app_db TO app_user;
    GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to app_user;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to app_user;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to app_user;
    ALTER DATABASE app_db OWNER TO app_user;
    ```

1. Run migrations

    ```
    cd technative
    python manage.py migrate
    ```

1. Create a super user:

    ```
    python manage.py createsuperuser
    ```

1. Run the server:

    ```
    python manage.py runserver
    ```

1. Log into the admin with the superuser: http://localhost:8000

    1. Add a context sentence for all three groups
    1. Add products for all three groups
    1. Create users for each group and set their permissions to only access their relevant content

1. The API can be tested using the `api-tester` HTML page from the repo root.