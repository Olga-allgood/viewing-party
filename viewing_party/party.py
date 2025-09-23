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
    '''
    First create two lists where each list will separately hold
    the movies (in dictionary form) that either
    the user or friends have watched. Then compare the movies
    in user_list against the friends_list: if the movie in
    user_list is not present in friends_list, then
    that movie will get added to the unique_movies.

    '''
    user_list = []
    friends_list = []

    unique_movies = []

    for user_movie in user_data["watched"]:
        user_list.append(user_movie)

    for friend_movies in user_data["friends"]:
        for friend_movie in friend_movies["watched"]:
            friends_list.append(friend_movie)

    for movie in user_list:
        if movie not in friends_list:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    user_list = []
    friends_list = []

    unique_movies = []

    for user_movie in user_data["watched"]:
        user_list.append(user_movie)
    
    for friend_movies in user_data["friends"]:
        for friend_movie in friend_movies["watched"]:
            if friend_movie not in friends_list:
                friends_list.append(friend_movie)

    for movie in friends_list:
        if movie not in user_list:
            unique_movies.append(movie)
    
    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    First create an empty list to hold the recommended movies
    that will be added later.

    Then get the unique list of movies in which only the friends
    have watched from the previous function get_friends_unique_watched().

    Then loop through the list of unique friends movies, check
    to see if the platform those movies are hosted in are in the
    user's list of subscription platforms. If yes, then those
    movies will added to the recommendation list.
    '''
    rec_list = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)

    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

