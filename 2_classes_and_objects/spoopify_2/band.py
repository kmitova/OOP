from spoopify_2.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for item in self.albums:
            if item.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for item in self.albums:
            if item.name == album_name and not item.published:
                self.albums.remove(item)
                return f"Album {album_name} has been removed."
            elif item.name == album_name and item.published:
                return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}\n'
        for item in self.albums:
            result += f"{item.details()}\n"
        return result

