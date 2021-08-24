## Api Documentation


## Project Setup
	1. git clone https://github.com/MahmudulHassan5809/movie-api-task.git
    2. create virtual env using this command-> python -m venv ./venv
    3. activate virtual env 
    	1.venv\Scripts\activate (windows)
    	2.source venv/bin/activate (Linux)
    4. Istall all the requirements using this commans -> pip install -r requirements.txt
    5. Create a .env file copy all the ENV variable from .env.example and replace by your values.
       For testing purpose i am not putting .env file in gitignore.
    5. Run python manage.py runserver
    6. project will run in http://127.0.0.1:8000/
    7. To test run python manage.py test
    
## Movies Api
	POST REQUEST
    ENDPOINT  : http://127.0.0.1:8000/api/movies/
    PAYLOAD   : {
                  "title": "Forrest Gump"
                }
  	Response  : If movie is found in omdbapi then it will save in our database the return the current saved object.
    		    {
                    "id": 7,
                    "title": "Fight Club",
                    "start_year": 1999,
                    "end_year": null,
                    "rated": "R",
                    "released": "1999-10-15",
                    "runtime": "139 min",
                    "genere": null,
                    "director": "David Fincher",
                    "writer": "Chuck Palahniuk, Jim Uhls",
                    "actors": "Brad Pitt, Edward Norton, Meat Loaf",
                    "plot": "An insomniac office worker and a devil-may-care soap maker form an underground....",
                    "language": "English",
                    "country": "Germany, United States",
                    "awards": "Nominated for 1 Oscar. 11 wins & 38 nominations total",
                    "poster": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYj.jpg",
                    "metascore": 66.0,
                    "imdb_rating": 8.8,
                    "imdb_votes": "1,920,113",
                    "imdb_id": null,
                    "type": "movie",
                    "dvd": "2015-11-25",
                    "box_office": "$37,030,102",
                    "production": "Art Linson Productions, Fox 2000 Pictures, Taurus Film, New Regency Pictures",
                    "website": null
                }
               
    		   If movie not found it then it will return 404 (movie not found)
               if title is send as empty it will return 400 bad request (This field may not be blank)
   
   ---
   	
    GET REQUEST
    ENDPOINT   : http://127.0.0.1:8000/api/movies/
    Response   : Return all the movies available in the database.
    FILTERING  : http://127.0.0.1:8000/api/movies/?title__icontains=club&start_year=1999
                 here you can filter all the model field you just need to send query param
                 in formated way.
    Searching  : http://127.0.0.1:8000/api/movies/?search=David
    			 here you can search by title,plot,actors,director
    Ordering   : http://127.0.0.1:8000/api/movies/?ordering=imdb_rating
    			 here you can order by imdb_rating. if add - before imdb_rating then it will
                 be descending order.

## Comments API
	
    POST REQUEST
    ENDPOINT : http://127.0.0.1:8000/api/movies/comments/
    PAYLOAD  : {
                   "comment": "",
                   "movie": null
               }
               
               It will validate all the required field and validation.In the response potsed comment will be return.
    Response  : {
                    "id": 2,
                    "comment": "Test",
                    "movie": 8
                }
   
   ---
   	GET REQUEST
    ENDPOINT : http://127.0.0.1:8000/api/movies/comments/
    Response : return list of all comments present in the application database.
    Filter By Movie ID : http://127.0.0.1:8000/api/movies/comments/?movie_id=1
    
    
    		     
   