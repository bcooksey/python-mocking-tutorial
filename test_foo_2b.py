# Example of using spec to prevent bad mocking
import unittest
from foo_2 import Man
from mock import patch, MagicMock

class Foo(unittest.TestCase):

    def test_1(self):
        with patch('foo_2.Watch', spec=True) as mock_watch:
            mock_dt = MagicMock()
            mock_dt.strftime.return_value = '01:05 pm'
            mock_watch.return_value.get_time.return_value = mock_dt

            man = Man()
            self.assertEqual(man.tell_time(), 'It is now 01:05 pm')

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
