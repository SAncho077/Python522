from view import UserInterface
from model import FilmModel

class Controller:
    def __init__(self):
        self.view_project = UserInterface()
        self.model_project = FilmModel()

    def run(self):
        answer = None

        while answer != "q":
            answer = self.view_project.input_interface()

            self.check_user_interface(answer)

    def check_user_interface(self, answer):
        if answer == "1":
            films = self.view_project.add_user_film()
            self.model_project.add_film(films)

        elif answer == "2":
            films = self.model_project.get_all_films()

            self.view_project.show_all_films(films)

        elif answer == "3":
            films_title = self.view_project.get_user_films()
            try:
                film = self.model_project.get_single_film(films_title)
            except KeyError:
                self.view_project.show_incorrect_title_error(films_title)
            else:
                self.view_project.show_single_film(film)

        elif answer == "4":
            film_title = self.view_project.get_user_films()
            try:
                title = self.model_project.remove_film(film_title)
            except KeyError:
                self.view_project.show_incorrect_title_error(film_title)
            else:
                self.view_project.remove_single_film(title)

        elif answer == "q":
            self.model_project.save_data()
        else:
            self.view_project.show_incorrect_answer(answer)

