# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # look for a movie dict in watchlist with matching title 
    for movie in user_data["watchlist"]:
        if movie["title"] == title:   
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data     


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    total_rating = 0
    for watched_movie in user_data["watched"]:
       total_rating += watched_movie["rating"]
    average_rating = total_rating/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_count = {}
    for watched_movie in user_data["watched"]:
       genre = watched_movie["genre"]
       if genre in genre_count:
           genre_count[genre] += 1
       else:
           genre_count[genre] = 1   

    # find genre with hishest count
    most_watched = None
    highest_count = 0
    for genre, count in genre_count.items():
        if count > highest_count:
            most_watched = genre
            highest_count = count
    return  most_watched      

        


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched = []
    unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_movies.append(movie)   
    return unique_movies         


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

