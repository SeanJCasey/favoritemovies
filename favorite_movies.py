from media import Movie
from fresh_tomatoes import open_movies_page

matrix = Movie(
        "The Matrix",
        ("https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWM"
         "xOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY"
         "1000_CR0,0,723,1000_AL_.jpg"),
        "https://www.youtube.com/watch?v=_Ls19O-9p3s"
    )

big_lebowski = Movie(
        "The Big Lebowski",
        ("https://images-na.ssl-images-amazon.com/images/M/MV5BZTFjMjBiYzItNzU"
         "5YS00MjdiLWJkOTktNDQ3MTE3ZjY2YTY5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY"
         "1000_CR0,0,665,1000_AL_.jpg"),
        "https://www.youtube.com/watch?v=cd-go0oBF4Y"
    )

lock_stock = Movie(
        "Lock, Stock and Two Smoking Barrels",
        ("https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyN2JmZmEtNjA"
         "yMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY"
         "1000_CR0,0,666,1000_AL_.jpg"),
        "https://www.youtube.com/watch?v=h6hZkvrFIj0"
    )

pans_labrynth = Movie(
        "Pan's Labyrinth",
        ("https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3ODg2NjQ5NF5"
         "BMl5BanBnXkFtZTcwMDEwODgzMQ@@._V1_SY1000_CR0,0,679,1000_AL_.jpg"),
        "https://www.youtube.com/watch?v=EqYiSlkvRuw"
    )

favorite_movies = [matrix, big_lebowski, lock_stock, pans_labrynth]
open_movies_page(favorite_movies)
