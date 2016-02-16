import fresh_tomatoes
import movie

# New movie instances require 5 arguments in the following order (all strings):
# Movie Title
# Movie Storyline
# Movie Poster URL
# Movie Trailer URL
# Your rating of the movie, in stars (use asterisks), max. 4 stars

family_stone = movie.Movie("The Family Stone",
                           "Christmas hijinks with Sarah Jessica Parker.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/9/97/The_Family_Stone_Poster.jpg/220px-The_Family_Stone_Poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=_wM0Zn3493o",
                           "***")

wings_of_desire = movie.Movie("Wings of Desire",
                              "Two angels follow humans in Berlin, until one m"
                              "ust decide whether he will become human.",
                              "http://static.rogerebert.com/uploads/movie/movie_poster/wings-of-desire-1988/large_yQI5X0stOQhVhbfZKtsnG8I7sBo.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=dwo122meoAA",
                              "****")

passion_joan = movie.Movie("The Passion of Joan of Arc",
                           "A silent film following the trial and execution of"
                           " Joan of Arc for heresy.",
                           "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/The_Passion_of_Joan_of_Arc_%281928%29_English_Poster.png/220px-The_Passion_of_Joan_of_Arc_%281928%29_English_Poster.png",  # NOQA
                           "https://www.youtube.com/watch?v=CQj_3AY-E1g",
                           "****")

angels_america = movie.Movie("Angels in America",
                             "A gay man with AIDS sees visions in 1980s NYC.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Angels_In_America%2C_2003_TV_mini_series%2C_DVD_cover.jpg/250px-Angels_In_America%2C_2003_TV_mini_series%2C_DVD_cover.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=jTDcbJcCGTE",
                             "****")

five_hundred_days_summer = movie.Movie("500 Days of Summer",
                              "White 20-something hipsters who work at a greet"
                              "ing card company have a tempestuous relationshi"
                              "p.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Five_hundred_days_of_summer.jpg/220px-Five_hundred_days_of_summer.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=PsD0NpFSADM",
                              "***")

a_new_hope = movie.Movie("Star Wars: A New Hope",
                         "Luke Skywalker gets involved in intergalactic confli"
                         "ct and begins his training as a Jedi knight.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                         "***")

# Compiling list of movies into an array

movies = [angels_america, family_stone, five_hundred_days_summer,
          wings_of_desire, passion_joan, a_new_hope]

# Opening fresh tomatoes code that will create the HTML file

fresh_tomatoes.open_movies_page(movies)
