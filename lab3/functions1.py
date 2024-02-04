movies = [
    {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
    },
    {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
    },
    {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
    },
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    },
    {
    "name": "The Choice",
    "imdb": 6.2,
    "category": "Romance"
    },
    {
    "name": "Colonia",
    "imdb": 7.4,
    "category": "Romance"
    },
    {
    "name": "Love",
    "imdb": 6.0,
    "category": "Romance"
    },
    {
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
    },
    {
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
    },
    {
    "name": "Ringing Crime",
    "imdb": 4.0,
    "category": "Crime"
    },
    {
    "name": "Joking muck",
    "imdb": 7.2,
    "category": "Comedy"
    },
    {
    "name": "What is the name",
    "imdb": 9.2,
    "category": "Suspense"
    },
    {
    "name": "Detective",
    "imdb": 7.0,
    "category": "Suspense"
    },
    {
    "name": "Exam",
    "imdb": 4.2,
    "category": "Thriller"
    },
    {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
}
]
#!!!!!!EX1!!!!!
def is_high_score_by_name(movie_name):
    for movie in movies:
        if movie["name"] == movie_name:
            return movie["imdb"] > 5.5
    return False


user_input = input("Enter the movie name: ")
result = is_high_score_by_name(user_input)

if result:
    print(f"The IMDB score for {user_input} is above 5.5.")
else:
    print(f"The IMDB score for {user_input} is  below, or the movie was not found.")


 #!!!!!EX2!!!!!!!!
def get_high_score_movies(movie_list):
    high_score_movies = [movie for movie in movie_list if movie["imdb"] > 5.5]
    return high_score_movies


high_score_movies_list = get_high_score_movies(movies)


for movie in high_score_movies_list:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")


#!!!!!!EX3!!!!!
def cat(movies, cat_name):
    return [movie for movie in movies if movie.get('category') == cat_name]


user_category_input = input("Enter the category name: ")

result = cat(movies, user_category_input)

if result:
    print(f"Movies in the category '{user_category_input}':")
    for movie in result:
        print(f"{movie['name']} - IMDB Score: {movie['imdb']}")
else:
    print(f"No movies found in the category '{user_category_input}'.")
print()    

#!!!!!EX4!!!!!!
def average_imdb_score(movie_list):
    total_score = sum(movie["imdb"] for movie in movie_list)
    average_score = total_score / len(movie_list)
    return average_score


avg_score = average_imdb_score(movies)
print(f"The average IMDB score of all movies is: {avg_score:.2f}")

#!!!!!!EX5!!!!!!
def average_imdb_score_by_category(movie_list, category):
    category_movies = [movie["imdb"] for movie in movie_list if movie.get('category') == category]

    average_score = sum(category_movies) / len(category_movies)
    return average_score

user_category_input = input("Enter the category name: ")
avg_score_by_category = average_imdb_score_by_category(movies, user_category_input)

if avg_score_by_category:
    print(f"The average IMDB score for movies in the category '{user_category_input}' is: {avg_score_by_category:.2f}")
else:
    print(f"No movies found in the category '{user_category_input}'.")


