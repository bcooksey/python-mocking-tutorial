# Example of using autospec to eliminate argument-param mismatch mocking bugs
import unittest
from foo_3 import Man
from mock import patch, MagicMock

class Foo(unittest.TestCase):

    def test_1(self):
        with patch('foo_3.Watch', autospec=True) as mock_watch:
            mock_dt = MagicMock()
            mock_dt.strftime.return_value = '01:05 pm'
            mock_watch.return_value.get_time.return_value = mock_dt

            # mock_dt = create_autospec(datetime)
            # mock_dt.strftime.return_value = '01:05 pm'
            # mock_watch.return_value.get_time.return_value = mock_dt
            # mock_watch.return_value.get_time.return_value.strftime.return_value = '01:05 pm'

            man = Man()
            self.assertEqual(man.tell_time(), 'It is now 01:05 pm')


        # Uncomment and run test to see that actual code would die
        # unmocked_man = Man()
        # print unmocked_man.tell_time()

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
