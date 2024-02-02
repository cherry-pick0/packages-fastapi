# Shipping parcels service

FastAPI app for tracking shipped packages.

## Instructions

1) Setup

     *Instructions for Linux/Ubuntu*
          
     Install:
          
        * pipenv
        * PostgreSQL


2) Setup db:
     
        # Create local db
        sudo -u postgres createdb shipping_packages_db
        
        # Enter postgres
        sudo -u postgres psql
        
        # Create new user and grant privileges
        CREATE USER shipping_packages_user WITH ENCRYPTED PASSWORD 'shipping_packages_db_pass';
        GRANT ALL PRIVILEGES ON DATABASE shipping_packages_db to shipping_packages_user;
        
        # For testing purposes - add permission to create db
        ALTER USER shipping_packages_user CREATEDB;
        
        # Connect to our new local db
        \c shipping_packages_db


3) Start a project
        
        # Create and enter virtual environment
        pipenv shell
        
        # Install dependencies
        pipenv install
        
        # Add PYTHONPATH to your environment variables or run this command:
        export PYTHONPATH=$PWD
        
        # Run migrations
        alembic upgrade head
        
        # Run the app
        uvicorn main:app --reload
        
        # Go to http://127.0.0.1:8000/docs
        
