from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        for el in library.user_records:
            if el.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        library.rented_books[user.username] = {}

    def remove_user(self, user: User, library: Library):
        for el in library.user_records:
            if el.user_id == user.user_id:
                library.user_records.remove(user)
                library.rented_books.pop(user.username)
                return
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        for el in library.user_records:
            if el.user_id != user_id:
                continue
            if el.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"

            rented_books = library.rented_books[el.username]
            library.rented_books.pop(el.username)
            library.rented_books[new_username] = rented_books
            el.username = new_username
            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"

