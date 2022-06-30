from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def __init__(self):
        Person.__init__(self)
        Employee.__init__(self)

    def teach(self):
        return 'teaching...'



