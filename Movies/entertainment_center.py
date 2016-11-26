import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?=vwyZH85NQC4" )

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io" )

threeHundred = media.Movie("300",
                  "Spartans fight to the death.",
                  "https://images-na.ssl-images-amazon.com/images/I/51MtJBws9ZL.jpg",
                  "https://www.youtube.com/watch?v=WorI5HPWbpg" )

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn.",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://ww.youtube.com/watch?v=3PsUJFEBC74")

movies = [toy_story, avatar, threeHundred, school_of_rock]
fresh_tomatoes.open_movies_page(movies)

