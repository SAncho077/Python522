


def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def input_interface(self):
        print("Действия с фильмами")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        answer = input("Выберите вариант действия: ")
        return answer

    @add_title("Добавление фильма")
    def add_user_film(self):
        dict_fims = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None,
        }
        for key in dict_fims:
            dict_fims[key] = input(f"Введите {key} фильма")

        return dict_fims

    @add_title("Каталог фильмов")
    def show_all_films(self, films):
        for ind, films in enumerate(films, 1):
            print(f"{ind}. {films}")

    @add_title("Ввод название фильма")
    def get_user_films(self):
        user_film = input("Введите название фильма:")
        return user_film

    @add_title("Просмотр фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} - была удалена")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer(self, answer):
        print(f"Варианта {answer} не существует")