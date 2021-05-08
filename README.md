# Historical chef
Challenge task for ChefHero

## features
1. CD/CD integrated with github actions
2. Development done via docker
3. Unit tests available
4. Flake tests available
5. Database used : postgres

## how to run ?
Run the following command from the root of the project : 

```docker-compose up```

The application will now be hosted on localhost with port 8000

## how to run tests ?

Run the following command from the root of the project :

```docker-compose run app sh -c "python manage.py test"```

## how to run flake tests

Run the following command from the root of the project :

```docker-compose run app sh -c "python flake8"```