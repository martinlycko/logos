class Optional:

    def __init__(self, Value=None):
        self.isSet = False
        self.Value = 0

        if Value is not None:
            self.isSet = True
            self.Value = Value

    def setValue(self, Value):
        self.isSet = True
        self.Value = Value

    def getValue(self):
        if self.isSet is True:
            return self.Value
        else:
            raise ValueError('Column not set')
