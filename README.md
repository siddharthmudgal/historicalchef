# Historical chef
Challenge task for ChefHero

## Features packaged
1. CD/CD integrated with github actions
2. Development done via docker
3. TDD ( Test Driven Development )
4. Integration Tests
5. Flake tests
6. Database - postgres
8. Auto generated ID format :
   1. The auto generated ID is auto increment
   2. Is of type BigAutoField
   3. The range is from **1** to **9223372036854775807**
9. Fields validations
   1. Email
   2. data payload ( JSON validation )



## REST API's exposed

1. ```http://localhost:8000/admin```

   1. This REST API provides access to admin portal for this application
   2. Here you can view Event model via UI
   3. Event model can be edited via UI itself
   4. However, this requires credentials of a super user to be generated

2. ```http://localhost:8000/events/event/```

   1. Verbs supported : GET / POST

   2. **GET** -> Lists all the current records present in the event object model

   3. **POST** -> Allow to post a new event object model to the database

      1. Request body

         ```json
         {
             "created_at": 1620502933,
             "email": "sidmud@outlook.com",
             "environment": "development",
             "component": "order",
             "message": "this is a sample message",
             "data_payload": {"key":"value"}
         }
         ```

         

3. ```http://localhost:8000/events/event/find/```

   1. Verbs supported : POST

   2. This API allows searching for relevant records within the events records.

   3. The following fields can be used to search events (as mentioned in the challenge ): 

      1. created_at
      2. email
      3. environment
      4. component
      5. message

   4. Request body for the request

      ```json
      {
          "created_at": "08-05-2021", // optional
          "email": "sidmud@outlook.com", // optional
          "environment": "production", // optional
          "component": "order", //optional
          "message": "message" //optional
      }
      ```



## How to run the app ?
Run the following command from the root of the project : 

```docker-compose up```

The application will now be hosted on localhost with port 8000

## How to run tests ?

Run the following command from the root of the project :

```docker-compose run app sh -c "python manage.py test"```

## How to run flake tests

Run the following command from the root of the project :

```docker-compose run app sh -c "python flake8"```



## Module descriptions

1. app
   1. is the main django app
2. core
   1. Consists of all models & migrations
3. event
   1. implementation and declaration of API's related to event ( views.py )
   2. serialziers related to event ( serializer.py )
   3. business logics related to event ( service.py )



## Business logics implementation

All business logics must go in the service module ( currently only present in event module). Similarly moving forward, when new apps are created they must contain a services python folder ( or a services.py ) to implement the business logics.



## Strategies to improve DB access performance

1. Atomic transactions
2. Indexing
3. QuerySet lazy loading
4. QuerySet caching