from guild_system_2.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for member in self.players:
            if member.name == player_name:
                member.guild = Player.DEFAULT_GUILD
                self.players.remove(member)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = ''
        result += f"Guild: {self.name}"
        for member in self.players:
            result += '\n' + member.player_info()
        return result
