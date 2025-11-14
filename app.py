import os

from waitress import serve # type: ignore
from dotenv import load_dotenv # type: ignore

from my_project import create_app

load_dotenv()

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 5001
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"

if __name__ == '__main__':
    required_env_vars = ['DATABASE_HOST', 'DATABASE_NAME', 'DATABASE_USER', 'DATABASE_PASSWORD']
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            f"Please check your .env file."
        )
    
    flask_env = os.getenv('FLASK_ENV', DEVELOPMENT).lower()
    
    db_user = os.getenv('DATABASE_USER')
    db_password = os.getenv('DATABASE_PASSWORD')
    db_host = os.getenv('DATABASE_HOST')
    db_name = os.getenv('DATABASE_NAME')
    
    config = {
        'DEBUG': os.getenv('DEBUG', 'False').lower() == 'true',
        'SQLALCHEMY_DATABASE_URI': f'mysql://{db_user}:{db_password}@{db_host}/{db_name}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() == 'true'
    }

    if flask_env == DEVELOPMENT:
        config['DEBUG'] = True
        create_app(config).run(host=HOST, port=DEVELOPMENT_PORT, debug=True)

    elif flask_env == PRODUCTION:
        serve(
            create_app(config), 
            host=HOST, 
            port=PRODUCTION_PORT,
            threads=16,
            channel_timeout=120,
            connection_limit=2000,
            asyncore_use_poll=True,  # poll/select
            url_scheme='http'
        )

    else:
        raise ValueError(f"Invalid FLASK_ENV value: '{flask_env}'. Must be 'development' or 'production'.")
