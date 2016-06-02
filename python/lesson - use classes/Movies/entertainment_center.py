import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "http://www.electric949.com/wp-content/uploads/2015/11/toy-story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.overthinkingit.com/wp-content/uploads/2010/01/Avatar-Sucks.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

joe_dirt = media.Movie("Joe Dirt",
                       "Country rocker trying to find his parents",
                       "https://moviemingler.files.wordpress.com/2015/07/joe_dirt-mullet.jpg",
                       "https://www.youtube.com/watch?v=XoAs204xSJs")

tropic_thunder = media.Movie("Tropic Thunder",
                             "Action comedy about a group of self-absorbed actors who set out to make the most expensive war film",
                             "http://www.gstatic.com/tv/thumb/movieposters/177515/p177515_p_v8_an.jpg",
                             "https://www.youtube.com/watch?v=T-6YhRZowgc")

ex_machina = media.Movie("Ex Machina",
                         "24 year old coder at the world's largest internet company, wins a competition to spend a week at a retreat",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                         "https://www.youtube.com/watch?v=gyKqHOgMi4g")

home_alone = media.Movie("Home Alone",
                         "Home Alone is a 1990 American Christmas comedy film",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcTdEoLOi9ncuhBzSRWrI00a_KWHGI_9KJN-d35rk_3Sws5ygZq2",
                         "https://www.youtube.com/watch?v=IsOlj-xpK9Q")

movies = [toy_story, avatar, joe_dirt, tropic_thunder, ex_machina, home_alone]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)