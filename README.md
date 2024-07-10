| **DEVELOPMENT SETUP [ LOCAL ]**

* Step 01: Create .env file in root directory
 ENV Simple Code. 
```bash

    ENVIRONMENT_MODE=local
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=postgres
    DB_PORT=5432
    DB_NAME=test_db
    JWT_SECRET_KEY = "09d25e094faa6ca2556c81"
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30

    AWS_S3_CLIENT_ACCESS_KEY="KEY"
    AWS_S3_CLIENT_SECRET_ACCESS_KEY="KEY"
    AWS_REGION_NAME="KEY"
    AWS_S3_BUCKET_NAME="KEY"

``` 

* Step 2:  Clone the repo and move to the project directory . 
```bash
    docker-compose up --build
    docker-compose up --build -d [Optional]
``` 

