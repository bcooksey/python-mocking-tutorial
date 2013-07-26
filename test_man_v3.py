# Example of a bug due argument-parameter mismatch being hidden by mocking
import unittest
from man import Man
from mock import patch, MagicMock

class Foo(unittest.TestCase):

    def test_1(self):
        with patch('man.Watch', spec=True) as mock_watch:
            mock_dt = MagicMock()
            mock_dt.strftime.return_value = '01:05 pm'
            mock_watch.return_value.time.return_value = mock_dt

            man = Man()
            self.assertEqual(man.tell_time(), 'It is now 01:05 pm')
            mock_dt.strftime.assert_called_once_with('%I:%M %p')

        # Uncomment and run test to see that actual code would die
        # unmocked_man = Man()
        # print unmocked_man.tell_time()

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
