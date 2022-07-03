from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed = 0
        for worker in self.workers:
            needed += worker.salary
        if needed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed = 0
        for animal in self.animals:
            needed += animal.money_for_care
        if needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += repr(lion) + '\n'
        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += repr(tiger) + '\n'
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += repr(cheetah) + '\n'
        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += repr(keeper) + '\n'
        caretakers = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += repr(caretaker) + '\n'
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += repr(vet) + '\n'
        return result.strip()