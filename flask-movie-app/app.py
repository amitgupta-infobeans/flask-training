from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual TMDb API key
TMDB_API_KEY = 'a97bb2ccbeb3bb911313e22104a4f819'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

# Example endpoint to get a list of popular movies
top_rated_movie = '/movie/top_rated'  #top_rated
now_playing_movie = '/movie/now_playing'#now_playing
upcoming_movie = '/movie/upcoming'  # upcoming
popular_movie = '/movie/popular' 

params = {
    'api_key': TMDB_API_KEY
}

def apiCalling(url):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movie_data = response.json()
        movies = movie_data['results']
    else:
        movies= []
    return movies


#popular movies list
@app.route('/')
def index():
   url = TMDB_BASE_URL + popular_movie
   movies = apiCalling(url)
   return render_template('index.html', movies=movies, title="Popular")


#now_playing
@app.route('/now_playing')
def now_playing():
   url = TMDB_BASE_URL + now_playing_movie
   movies = apiCalling(url)
   return render_template('index.html', movies=movies, title="Now Playing")


#upcomming_movies
@app.route('/upcomming_movies')
def upcomming_movies():
   url = TMDB_BASE_URL + upcoming_movie
   movies = apiCalling(url)
   return render_template('index.html', movies=movies, title="Upcoming")


#top_rated
@app.route('/top_rated')
def top_rated():
   url = TMDB_BASE_URL + top_rated_movie
   movies = apiCalling(url)
   return render_template('index.html', movies=movies, title="Top Rated")



#get one movie info...
@app.route('/movies/<movie_id>')
def get_movie(movie_id):

    url = f'{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    movie_data = response.json()
    return render_template('movie.html', movie=movie_data, title="One Movie Details")


if __name__ == '__main__':
    app.run(debug=True)