import fresh_tomatoes
import media

"""This file created movie objects to store title, storyline, poster image, and trailer URL. Then passes those objects to fresh_tomatoes"""

tropic_thunder = media.Movie("Tropic Thunder",
                             "Action comedy about a group of self-absorbed actors who set out to make the most expensive war film",
                             "http://www.gstatic.com/tv/thumb/movieposters/177515/p177515_p_v8_an.jpg",
                             "https://www.youtube.com/watch?v=T-6YhRZowgc")

ex_machina = media.Movie("Ex Machina",
                         "24 year old coder at the world's largest internet company, wins a competition to spend a week at a retreat working in AI",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                         "https://www.youtube.com/watch?v=gyKqHOgMi4g")

home_alone = media.Movie("Home Alone",
                         "Home Alone is a 1990 American Christmas comedy film",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcTdEoLOi9ncuhBzSRWrI00a_KWHGI_9KJN-d35rk_3Sws5ygZq2",
                         "https://www.youtube.com/watch?v=IsOlj-xpK9Q")

#Creating array/list of objects to pass to fresh_tomatoes
movies = [tropic_thunder, ex_machina, home_alone]
fresh_tomatoes.open_movies_page(movies)
