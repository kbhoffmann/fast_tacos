First Create your docker container and taco database:
docker run --name fast-tacos -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine
docker exec -it fast-tacos bash
create database taco_database;
grant all privileges on database taco_database to postgres;

Run the application:
pipenv shell
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs#/default/root__get to interact with the API