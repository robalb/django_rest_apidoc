# Demoapp

A demo application based on Django Rest Framework, with automatic openapi docs generation.

## local development setup

> This documentation assumes that you already have git installed on your device,
> configured with your github credentials

1) ### Install the required software

   Install the following software, if you don't have it already

   - docker [Download docker desktop](https://docs.docker.com/get-docker/)

2) ### clone the repository

   Execute the command `git clone https://github.com/robalb/django_rest_apidoc.git`.

   Execute the command `cd django_rest_apidoc` to navigate into the new repository
   

3) ### Initialize the environment variables

   Execute the command `cp .env.example .env` to copy the content of the `.env.example` file into a new `.env` file

4) ### apply the migrations

   Execute the command `docker-compose run python manage.py migrate`

## local development

Make sure that your terminal is always in the `/django_rest_apidoc` folder, where the
docker-compose.yml file is located.
If you are using windows, make also sure the docker desktop app is running

- ### start docker-compose

  With your terminal, execute the command `docker-compose up -d` to start the app.
  The first time this command may require a couple of minutes.

  When completed, the django application will be available at http://localhost:8000/, and
  the interactive documentation will be available at http://localhost:8000/swagger-ui.

  while the docker-compose app is running, you can apply any change you want to
  the code in `/demoapp`. Django will reload in real time with your changes

- ### stop docker compose

  `docker-compose down`

- ### view django logs

   `docker-compose logs -f django`

- ### run manage.py commands

   `docker-compose run django python manage.py <your command>`

- ### install dependencies

  `docker-compose run django pip install <depname>`

