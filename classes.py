from json import JSONEncoder


class Order(object):
    id = -1
    name = ""
    dependencies = []

    def __init__(self, id, name, dependencies=None):
        self.id = id
        self.name = name
        self.dependencies = []


class OrderEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Order):
            return object.__dict__
        JSONEncoder.default(self, object)

class FormatException(Exception):
    def __init__(self, line_number, file_name, line):
        self.message = f'\nImproper format on line {line_number} in \"{file_name}\": \"{line[:-1]}\"\nAborting to avoid further errors!\n'
        super().__init__(self.message)
