# Server
setup your python environment (poetry )

Run `uvicorn server:app --port 44777 --reload`

# Database
## With Docker
Run `docker-compose up` in the root directory
## Without Docker
Setup a postgres database and set the environment variables in the .env file