__all__ = [
    "SourceFile",
    "Part",
    "Unit",
    "Map",
    "Race",
    "Civilization",
    "Tile",
    "Resource",
    "Utility",
    "Occupation",
    "Terrain",
    "Technology",
    "Building",
    "Vehicle",
]

# Base class
class SourceFile:
    def __init__(self, name, data):
        if type(data) != dict:
            raise TypeError(f"the data must be dict, not {data.__class__.__name__}")

        self.data = data
        self.parts = list(self.data.keys())

    def __len__(self):
        return len(self.parts)


class Part:
    def __init__(self, file, data):
        if type(data) != dict and type(data) != list:
            raise TypeError(
                f"the data must be dict or list, not {data.__class__.__name__}"
            )

        if type(data) == dict:
            self.keys = list(self.data.keys())

        self.file = file
        self.data = data

    def __len__(self):
        return len(self.units)


class Unit:
    def __init__(self, file, part, data):
        if type(data) != dict and type(data) != list:
            raise TypeError(
                f"the data must be dict or list, not {data.__class__.__name__}"
            )

        self.file = file
        self.part = part
        self.data = data


# Base on Part
# class

# Base on Unit
class Map(Unit):
    pass


class Race(Unit):
    pass


class Civilization(Unit):
    pass


class Tile(Unit):
    pass


class Resource(Unit):
    pass


class Utility(Unit):
    pass


class Occupation(Unit):
    pass


class Terrain(Unit):
    pass


class Technology(Unit):
    pass


class Building(Unit):
    pass


class Vehicle(Unit):
    pass
