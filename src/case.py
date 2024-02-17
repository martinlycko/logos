class Case:
    # A class to capture a single case

    id = 0              # IDs are imported from the event log
    attributes = {}     # The set of attributes is imported with the event log (e.g. price for a product)

    def __init__(self, id, attributes) -> None:
        self.id = id
        self.attributes = attributes