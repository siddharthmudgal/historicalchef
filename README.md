# Historical chef
Challenge task for ChefHero

## Skills showcased
1. CD/CD pipeline integration
   1. GitHub actions
2. Docker integration
   1. Development and testing carried out via docker environments
3. TDD ( Test Driven Development )
4. Integration Tests
5. Flake tests
6. Database - postgres

## Noteworthy mentions

1. ( Q1 ) this id should be autogenerated by the activity service, you can pick the format and explain why you pick this kind of id and the policy to generate it

   1. The ID generated is auto increment and of type BigAutoField.
   2. This type is selected because it can include a large number of events and not run out of unique primary keys
   3. The range is from **1** to **9223372036854775807**
      

2. CreatedAt is stored as timestamp in the database as requested in the question.

   1. However, the search records utilizes a date format in the created at field ( 09-05-2021 )
   2. Please note that there is a subtle different from the question. In the search criteria the date passed must contain double digits for date and month, as opposed to an example in the question.
      

3. Responsibilities have been split into different layers

   1. **app**

   - Is the main django app

   2. **core**

   - Consists of all models & migrations

   3. **event**

   - This module encloses functionalities related to 'event'

   - **api**
     - This sub-module covers code related to exposing REST API

   - **Services**
     - This sub-module consists of all business logics

4. Readme is populated
   

5. Business logics must be populated inside the **services** sub-module in various modules ( example event -> services )
   

6. DB access performance is improved by using the following strategies : 

   1. Atomic transactions
   2. Indexing
   3. QuerySet lazy loading
   4. QuerySet caching

7. Fields validated

   - Email

   - data payload ( JSON validation )
     

## REST API's exposed

1. ```http://localhost:8000/admin```

   1. This REST API provides access to admin portal for this application
   2. Here you can view Event model via UI
   3. Event model can be edited via UI itself
   4. However, this requires credentials of a super user to be generated
   
   
2. ```http://localhost:8000/api/```

   1. This is the API root for the exposed REST API's
   2. You can browse the supported REST API's from this page
      

3. ```http://localhost:8000/api/events/```

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

         

4. ```http://localhost:8000/api/search/events/```

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

      

   5. ```http://localhost:8000/api/events/<int:pk>/```
      1. Verbs Supported : GET, DELETE, PUT, PATCH
      2. This API allows retrieval  of event records based on their primary key
      3. example : ```http://localhost:8000/api/events/1/```



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


