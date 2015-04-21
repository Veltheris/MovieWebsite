import media
import great_films
"""
This program creates a selection of movie objects using media.py, and then creates a website to view their information using great_films.py

Add the movies in the format
{Name} = media.Movie({title}, {description}, {rating}, {duration}, {release}, {stars}, {director}, {poster_image}, {trailer_youtube})
{poster_image} and {trailer_youtube} require full urls
"""

#Start defining movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "G","81min","November 1995","Tom Hanks, Tim Allen", "John Lasseter",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "PG-13","162min","December 2009","Sam Worthington, Sigourney Weaver", "James Cameron",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pirates = media.Movie("Pirates of the Carribean",
                      "A pirate tries to get his ship back",
                      "PG-13","143min","July 2003","Johnny Depp, Orlando Bloom", "Gore Verbinski",
                      "https://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
                      "https://www.youtube.com/watch?v=naQr0uTrH_s")

iron_man = media.Movie("Iron Man",
                       "A playboy genius billionare becomes a superhero",
                       "PG-13","126min","May 2008","Robert Downey Jr., Gwyneth Paltrow", "Jon Favreau",
                       "http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

avengers = media.Movie("The Avengers",
                       "A group of superheroes unite",
                       "PG-13","143min","May 2012","Robert Downey Jr., Chris Evans", "Joss Whedon",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

matrix = media.Movie("The Matrix",
                     "A hacker discovers the world is not what it seems",
                     "R","136min","March 1999","Keanu Reeves, Laurence Fishburne", "The Wachowski Brothers",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

thor = media.Movie("Thor",
                   "A god must redeem himself",
                   "PG-13","115","May 2011","Chris Hemsworth, Anthony Hopkins","Kenneth Branagh",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

bighero6 = media.Movie("Big Hero 6",
                       "A prodigy and his inflatable robot save people",
                       "PG","102min","November 2014","Ryan Potter, Scott Adsit", "Don Hall, Chris Williams",
                       "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                       "https://www.youtube.com/watch?v=rD5OA6sQ97M")

hobbit = media.Movie("The Hobbit",
                     "A Young hobbit is called to adventure",
                     "PG-13","169min","December 2012","Martin Freeman, Ian McKellen", "Peter Jackson",
                     "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                     "https://www.youtube.com/watch?v=SDnYMbYB-nU")


movies = [bighero6,hobbit,avengers,pirates,avatar,iron_man,matrix,thor,toy_story]
great_films.open_movies_page(movies)
