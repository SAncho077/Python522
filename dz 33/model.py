import pickle
import os.path


class Film:
    def __init__(self, name_film, genre, director, year_of_release, duration, studio, actors):
        self.name_film = name_film
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name_film} ({self.director})"

class FilmModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.name_film] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_films = {
            "название": film.name_film,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.year_of_release,
            "длительность": film.duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_films

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.db_name, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
