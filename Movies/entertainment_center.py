"""
Written by Elliott Hawks
Nov 30, 2016
Udacity Python Project
Using fresh_tomatoes given by udacity

Program takes movie information, feeds it into an open_movies_page method from fresh_tomatoes
and creates a webpage to display the movie info.
"""

import media
import fresh_tomatoes

lotr_fellowship = media.Movie("The Lord of the Rings: Fellowship of the Ring",
                        "A meek Hobbit from the Shire and eight companions set out on a journey to destroy "
                        "the powerful One Ring and save Middle Earth from the Dark Lord Sauron.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_(2001)_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=V75dMMIW2B4" )

lotr_two_towers = media.Movie("The Lord of the Rings: The Two Towers",
                     "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, "
                     "the divided fellowship makes a stand against Sauron's new ally, Saruman, "
                     "and his hordes of Isengard.",
                     "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                     "https://www.youtube.com/watch?v=LbfMDwc4azU" )

three_hundred = media.Movie("300",
                  "Spartans fight to the death.",
                  "https://images-na.ssl-images-amazon.com/images/I/51MtJBws9ZL.jpg",
                  "https://www.youtube.com/watch?v=WorI5HPWbpg" )

lotr_return_king = media.Movie("Lord of the Rings: The Return of the King",
                             "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze "
                             "from Frodo and Sam as they approach Mount Doom with the One Ring.",
                             "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                             "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

saw = media.Movie("Saw",
                  "Two strangers awaken in a room with no recollection of how they got there or why, and soon discover they are "
                  "pawns in a deadly game perpetrated by a notorious serial killer.",
                  "https://s-media-cache-ak0.pinimg.com/originals/73/af/5c/73af5c89826e3e5da20c37cc348ef250.jpg",
                  "https://www.youtube.com/watch?v=OCZp5v8V-94")

transformers = media.Movie("Transformers",
                           "A boy and his alien car try to save the world from evil robots.",
                           "http://files.sharenator.com/transformers_movie_poster_optimus_prime-s712x1054-128089.jpg",
                           "https://www.youtube.com/watch?v=BrnXrtm334k")
                           

#Movies added to list that will be displayed on the webpage
movies = [lotr_fellowship, lotr_two_towers, lotr_return_king, three_hundred, saw, transformers]

#Function call in fresh_tomatoes.py that uses list of moves to generate the HTML file on a new page in browser.
fresh_tomatoes.open_movies_page(movies)
