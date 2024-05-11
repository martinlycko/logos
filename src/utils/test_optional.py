from Optional import Optional

import unittest


class test_None(unittest.TestCase):

    def setUp(self):
        self.Option = Optional()

    def test_RaiseError(self):
        with self.assertRaises(ValueError):
            self.Option.getValue()

    def test_ReturnsFalse(self):
        assert self.Option.isSet is False


class test_Used(unittest.TestCase):

    def setUp(self):
        self.Option = Optional(5)

    def test_ReturnsTrue(self):
        assert self.Option.isSet is True

    def test_ValueSet(self):
        assert self.Option.getValue() == 5


if __name__ == "__main__":
    unittest.main()
