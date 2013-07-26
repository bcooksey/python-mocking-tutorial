# Example of Basic Test Setup
import unittest
from man import Man

class Foo(unittest.TestCase):

    def test_1(self):
        self.man = Man()
        print self.man.tell_time()

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
