--------------read me-------------------------

********************************************************************************************

MYSQL DATABASE:

Make sure you should follow below commands to use mysql database in your django project

1. Install mysqlclient, command(pip install mysqlclient)
2. Open your MYSQL Command line and create your database to store your data as movies
3. I have created database name (movieslist) in this project.
4. Then we shoud use the same database using command (use database name) eg: use movies
   then it will swich to your database to use forther.

5. check in settings.py file in IndianMovies file as i provided.
   In that file you find my mysql engine in that place of sqllite3.


********************************************************************************************

Modules:

   I have used bellow modules in this project

  1. Django modules
  2. Serializers module
  3. mysqlclient for database connection
  4. rest_framework

********************************************************************************************


EXPLANATION:

-> Created django project name (IndianMovies) and inside this created app name (movies)

-> Implemented urls, views and models.

-> created superuser as admin, below are the credentials.
   Admin User name : admin
   password: 12345
   * have given all permission that admin can delete, edit add movies.
 
-> created user, and below are the credentials for user.
   user name : user
   password: Chinna@30
   * this user can just view movies

-> used serilizers file for implement rest api


********************************************************************************************

POSTMAN Details:
 
    API URL (http://127.0.0.1:8000/movies/put)
    Content-Type : application/json
    METHOD : PUT
    JSON SAMPLE PAYLOAD:
       {
         "movie_name": "bigil",
         "hero_name": "vijay",
         "heroin_name": "nayanatara",
         "music_director_name": "Rehman",
         "director_name": "Atle"
        }


********************************************************************************************




