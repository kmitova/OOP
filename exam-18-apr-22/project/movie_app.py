from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if any(user.username == username for user in self.users_collection):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        if not any(user.username == username for user in self.users_collection):
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user = None
        for u in self.users_collection:
            if u.username == username:
                user = u
        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = None
        for u in self.users_collection:
            if u.username == username:
                user = u
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        # result = ''
        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            if key == "year":
                movie.year = value
            if key == "age_restriction":
                movie.age_restriction = value
            # result += f"{username} successfully edited {movie.key} movie.\n"
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = None
        for u in self.users_collection:
            if u.username == username:
                user = u
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = None
        for u in self.users_collection:
            if u.username == username:
                user = u
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = None
        for u in self.users_collection:
            if u.username == username:
                user = u
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = ''
        for movie in sorted_movies:
            result += movie.details() + '\n'
        return result.strip()

    def __str__(self):
        result = ''
        if len(self.users_collection) == 0:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join(u.username for u in self.users_collection)}\n"
        if len(self.movies_collection) == 0:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(m.title for m in self.movies_collection)}\n"
        return result.strip()












