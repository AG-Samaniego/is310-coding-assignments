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

favorite_movies = {
    "movie_1": {
        "name": "Coming to America",
        "YoR": 1989,
        "Sequels": "none"
    },
    "movie_2": {
        "name": "Napoleon Dynamite",
        "YoR": 2004,
        "sequels": "none"
    }
}

favorite_books = {
    "book_1": {
        "name": "The Hunger Games",
        "YoR": 2008,
        "Sequels": ["Catching Fire", "Mockingjay"]
    },
    "book_2": {
        "name": "Animal's People",
        "YoR": 2011,
        "Sequels": "none"
    }
}

print("What is your favorite movie or book?")
media_title = input()
favorite_books["new_book"] = {
        "name": media_title
}
print("Your favorite movie is: ", media_title, " Describe to me what this movie is about!")
media_desc = input().strip()
favorite_books["new_book"]["Description"] = media_desc

print(favorite_books)