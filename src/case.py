class Case:
    # A class to capture a single case
    id = 0
    attributes = {}

    def __init__(self, id, attributes) -> None:
        self.id = id
        self.attributes = attributes