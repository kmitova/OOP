from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for item in customer.rented_dvds:
                    if item.id == dvd_id:
                        return f"{customer.name} has already rented {item.name}"
        for customer in self.customers:
            if customer.id == customer_id:
                for item in self.dvds:
                    if item.id == dvd_id:
                        if customer.age < item.age_restriction:
                            return f"{customer.name} should be at least {item.age_restriction} to rent this movie"
        for item in self.dvds:
            if item.id == dvd_id:
                if item.is_rented:
                    return "DVD is already rented"
        for customer in self.customers:
            for item in self.dvds:
                if customer.id == customer_id and item.id == dvd_id:
                    customer.rented_dvds.append(item)
                    item.is_rented = True
                    return f"{customer.name} has successfully rented {item.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for item in customer.rented_dvds:
                if item.id == dvd_id:
                    item.is_rented = False
                    customer.rented_dvds.remove(item)
                    return f"{customer.name} has successfully returned {item.name}"
        for customer in self.customers:
            if customer_id == customer.id:
                name = customer.name
                return f"{name} does not have that DVD"

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])






