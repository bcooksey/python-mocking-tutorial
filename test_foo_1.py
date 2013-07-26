# Example of basic mocking
import unittest
from foo_1 import Man
from mock import patch, MagicMock

class Foo(unittest.TestCase):
    @patch('foo_1.Watch')
    def test_1(self, mock_watch):
        # Create a fake datetime object
        mock_dt = MagicMock()
        mock_dt.strftime.return_value = '01:05 pm'

        # Have watch always return that fake object
        mock_watch.return_value.get_time.return_value = mock_dt

        man = Man()
        self.assertEquals(man.tell_time(), 'It is now 01:05 pm')

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
