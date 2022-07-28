from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)
        self.age_restriction = age_restriction

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        result = f"Thriller - Title:{self.title}, Year:{self.year}, " \
                 f"Age restriction:{self.age_restriction}, " \
                 f"Likes:{self.likes}, Owned by:{self.owner.username}"
        return result
