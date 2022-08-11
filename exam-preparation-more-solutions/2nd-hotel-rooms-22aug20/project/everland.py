from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_sum = 0
        for room in self.rooms:
            total_sum += room.expenses + room.room_cost
        return f"Monthly consumption: {total_sum:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                new_budget = room.budget - (room.expenses + room.room_cost)
                room.budget = new_budget
                result += f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {new_budget:.2f}$ left.\n"
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return result.strip()

    def status(self):
        result = ''
        all_guests = sum(r.members_count for r in self.rooms)
        result += f"Total population: {all_guests}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if hasattr(room, 'children'):
                count = 1
                for child in room.children:
                    result += f"--- Child {count} monthly cost: {child.cost * 30:.2f}$\n"
                    count += 1
            if hasattr(room, 'appliances'):
                result += f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in room.appliances):.2f}$\n"
        return result.strip()


everland = Everland()


young_couple = YoungCouple("Johnsons", 150, 205)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

everland.add_room(young_couple)
everland.add_room(young_couple_with_children)

print(everland.get_monthly_consumptions())
# print()
print(everland.pay())
print(everland.status())

