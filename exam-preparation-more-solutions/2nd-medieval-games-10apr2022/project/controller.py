class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != "Drink" and sustenance_type != "Food":
            return
        if not any(s for s in self.supplies if s.__class__.__name__ == "Drink" ):
            raise Exception("There are no drink supplies left!")
        if not any(s for s in self.supplies if s.__class__.__name__ == "Food" ):
            raise Exception("There are no food supplies left!")
        if player.need_sustenance is False:
            return f"{player_name} have enough stamina."
        for i in range(len(self.supplies)-1, -1, -1):
            supply = self.supplies[i]
            if supply.__class__.__name__ == sustenance_type:
                player.stamina = min(100, player.stamina + supply.energy)
                self.supplies.pop(i)
                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        no_stamina_message = ''
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)
        if first_player.stamina == 0:
            no_stamina_message += f"Player {first_player_name} does not have enough stamina.\n"
        if second_player.stamina == 0:
            no_stamina_message += f"Player {second_player_name} does not have enough stamina."
        if no_stamina_message:
            return no_stamina_message.strip()

        attacker = first_player if first_player.stamina < second_player.stamina else second_player
        defendant = first_player if first_player.stamina > second_player.stamina else second_player

        damage_to_def_from_attacker = attacker.stamina / 2
        defendant.stamina = max(0, defendant.stamina - damage_to_def_from_attacker)
        if defendant.stamina <= 0:
            # defendant.stamina = 0
            return f"Winner: {attacker.name}"
        attacker, defendant = defendant, attacker
        damage_to_def_from_attacker = attacker.stamina / 2
        # defendant.stamina -= damage_to_def_from_attacker
        defendant.stamina = max(0, defendant.stamina - damage_to_def_from_attacker)

        if defendant.stamina <= 0:
            # defendant.stamina = 0
            return f"Winner: {attacker.name}"
        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()
