favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

for movie in favorite_movies: 
    print(movie['name'])

first_movie_name = favorite_movies[0]['name']
for letter in first_movie_name:
        print(letter)


def print_movie_name_and_year(movie):
    movie_data = movie['name'] + ' was released in ' + str(movie['release_year'])
    return(movie_data)

new_movie_data = print_movie_name_and_year(favorite_movies[0])
print(new_movie_data)

if favorite_movies[0] == favorite_movies[1]:
    print('The same')
else:
    print('Different')

# we can also use elif
# elif means "else, if"