class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added.append(player)
        return f"Successfully added: {', '.join(p.name for p in added)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def __find_player_by_name(self, name: str):
        for p in self.players:
            if p.name == name:
                return p

        # def sustain(self, player_name: str, sustenance_type: str):
        #     if any(p.name == player_name for p in self.players):
        #         player = None
        #         for p in self.players:
        #             if p.name == player_name:
        #                 player = p
        #                 break
        #         # if player.stamina == 100:
        #         #     return f"{player_name} have enough stamina."
        #         if sustenance_type == "Drink":
        #             if player.stamina == 100:
        #                 return f"{player_name} have enough stamina."
        #             if not any(x.__class__.__name__ == "Drink" for x in self.supplies):
        #                 return f"There are no drink supplies left!"
        #             for i in range(len(self.supplies)-1, 0, -1):
        #                 if self.supplies[i].__class__.__name__ == "Drink":
        #                     if player.stamina + self.supplies[i].energy <= 100:
        #                         player.stamina += self.supplies[i].energy
        #                     else:
        #                         player.stamina = 100
        #                     name = self.supplies[i].name
        #                     self.supplies.pop(i)
        #                     return f"{player_name} sustained successfully with {name}."
        #
        #         elif sustenance_type == "Food":
        #             if player.stamina == 100:
        #                 return f"{player_name} have enough stamina."
        #             if not any(x.__class__.__name__ == "Food" for x in self.supplies):
        #                 return f"There are no food supplies left!"
        #             for i in range(len(self.supplies) - 1, 0, -1):
        #                 if self.supplies[i].__class__.__name__ == "Food":
        #                     if player.stamina + self.supplies[i].energy <= 100:
        #                         player.stamina += self.supplies[i].energy
        #                     else:
        #                         player.stamina = 100
        #                     name = self.supplies[i].name
        #                     self.supplies.pop(i)
        #                     return f"{player_name} sustained successfully with {name}."

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if self.supplies[i].__class__.__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            # player._sustain_player(supply)
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f"{player_name} sustained successfully with {supply.name}."

    # def duel(self, first_player_name: str, second_player_name: str):
    #     first_player = None
    #     second_player = None
    #     for p in self.players:
    #         if p.name == first_player_name:
    #             first_player = p
    #         if p.name == second_player_name:
    #             second_player = p
    #     if first_player.stamina == 0 and second_player.stamina == 0:
    #         return f"Player {first_player_name} does not have enough stamina."\
    #                + '\n' + f"Player {second_player_name} " \
    #                         f"does not have enough stamina."
    #     if first_player.stamina == 0:
    #         return f"Player {first_player_name} does not have enough stamina."
    #
    #     if second_player.stamina == 0:
    #         return f"Player {second_player_name} does not have enough stamina."
    #
    #     # player_with_less = None
    #     # player_with_more = None
    #     if first_player.stamina > second_player.stamina:
    #         player_with_more = first_player
    #         player_with_less = second_player
    #     else:
    #         player_with_more = second_player
    #         player_with_less = first_player
    #     winner = None
    #     current = player_with_less
    #     next = player_with_more
    #     count = 0
    #     while count < 2:
    #         if next.stamina - current.stamina / 2 <= 0:
    #             next.stamina = 0
    #             winner = current
    #             return f"Winner: {winner.name}"
    #         else:
    #             next.stamina -= current.stamina / 2
    #         count += 1
    #         current, next = next, current
    #
    #     if winner is None:
    #         if next.stamina > current.stamina:
    #             winner = next
    #         else:
    #             winner = current
    #     return f"Winner: {winner.name}"

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)


    # def next_day(self):
    #     for player in self.players:
    #         if player.stamina - (player.age * 2) < 0:
    #             player.stamina = 0
    #         else:
    #             player.stamina -= player.age * 2
    #         self.sustain(player.name, "Food")
    #         self.sustain(player.name, "Drink")
    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result


