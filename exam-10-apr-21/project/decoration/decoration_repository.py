class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: object):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def remove(self, decoration: object):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                # print(decoration.__class.__name__)
                return decoration
        return "None"

