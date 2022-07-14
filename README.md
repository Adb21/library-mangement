# Library Management Django APIs
- framework : django and django rest framework
- database : MySQL
- Authentication : JWT

## Requirnemts 
* create a virtual env and activate it
* install python packages from requirements.txt ( pip install -r requirements.txt )
* create new schema in MySQL DB named library either using MYSQL CLI or workbench
* update settings.py file with user and password of MySQL DB in DATABASE section.
  ![image](https://user-images.githubusercontent.com/22220558/178965694-1e96eb06-d5de-4366-9f36-bba307e3afcf.png)
* make migrations using bellow command
  * python manage.py makemigrations
  * python manage.py migrate
  
## run Server
* go to clonned folder then run bellow command and it will run server at http://127.0.0.1:8000/
  * python manage.py runserver 

## API endpoints and functionality 
User types : Admin and Student
### Account related APIs
* Register Admin : 
  * URL : http://127.0.0.1:8000/api/profiles/admin
  * Request Type : POST
  * Input data : username | email | password | first_name | last_name
  
* Register Student : 
  * URL : http://127.0.0.1:8000/api/profiles/student
  * Request Type : POST
  * Input data : username | email | password 
  
* Login : 
  * URL : http://127.0.0.1:8000/api/profiles/login
  * Request Type : POST
  * Input data : email | password 
  * Reponse : Tokens ( refresh and access ) 
  * Toek Validity : Access token = 30 mins | refresh toekn = 1 day
  
* Logout : 
  * URL : http://127.0.0.1:8000/api/profiles/logout
  * Request Type : POST
  * Input data : refresh token 

### Books related APIs
- Only Admin can Add/Retrieve/Delete Book (CRUD operations)
- Students can Only View all Books (View Only)

* Add Book 
  * URL : http://127.0.0.1:8000/api/books/add
  * Request Type : POST
  * Input data : title | author | category | synopsis | isbn | language | pages 
  * Choices : 
      * category = {Fiction,Non-Ficton,History,Geography,Science,Horror,Biographies}
      * language = {English,Hindi,Marathi,Gujarati,Other}

* Get all Books
  * URL : http://127.0.0.1:8000/api/books/< id >
  * Request Type : GET

* Retrieve single Book
  * URL : http://127.0.0.1:8000/api/books/< id >
  * Request Type : GET
  
* Update single Book
  * URL : http://127.0.0.1:8000/api/books/< id >
  * Request Type : PATCH / PUT [patch for partial update | put for full update]
  
* Delete single Book
  * URL : http://127.0.0.1:8000/api/books/< id >
  * Request Type : DEL

### Extra Features
* Pagination and Filters
  * Default page size is 5. can change it in settings.py usner REST_FRAMEWORK section.
  * Filters on category and language
  * search filter and orderby on Title and Author
  * Swagger UI for API endpoints and scema 
    * Swagger UI URL : http://127.0.0.1:8000/
    * schema URL :  http://127.0.0.1:8000/api/schema/
 * CORS headers also added
    * set on CORS_ALLOW_ALL_ORIGINS = True
