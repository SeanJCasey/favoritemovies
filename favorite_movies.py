from media import Movie
from fresh_tomatoes import open_movies_page

matrix = Movie(
        "The Matrix",
        # "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=_Ls19O-9p3s"
    )

big_lebowski = Movie(
        "The Big Lebowski",
        # "'The Dude' Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BZTFjMjBiYzItNzU5YS00MjdiLWJkOTktNDQ3MTE3ZjY2YTY5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=cd-go0oBF4Y"
    )

lock_stock = Movie(
        "Lock, Stock and Two Smoking Barrels",
        # "A botched card game in London triggers four friends, thugs, weed-growers, hard gangsters, loan sharks and debt collectors to collide with each other in a series of unexpected events, all for the sake of weed, cash and two antique shotguns.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=h6hZkvrFIj0"
    )

pans_labrynth = Movie(
        "Pan's Labyrinth",
        # "In the falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3ODg2NjQ5NF5BMl5BanBnXkFtZTcwMDEwODgzMQ@@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=EqYiSlkvRuw"
    )

favorite_movies = [matrix, big_lebowski, lock_stock, pans_labrynth]
open_movies_page(favorite_movies)
