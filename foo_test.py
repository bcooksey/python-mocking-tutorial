import unittest
from foo_2 import Man
from mock import patch, MagicMock

class Foo(unittest.TestCase):
    # Things to show:
    #   A case of mocking where the code changes but test still passes
    #   A case of mocking where spec saves us
    #   A case where spec and we go down a level we still pass
    #   A case with autospec

    @patch('foo_2.Watch')
    def test_1(self, mock_watch):
        mock_dt = MagicMock()
        mock_dt.strftime.return_value = '01:05 pm'
        mock_watch.return_value.get_time.return_value = mock_dt

        man = Man()
        self.assertEqual(man.tell_time(), 'It is now 01:05 pm')

# Safely ignore, needed to get test suite to run
if __name__ == '__main__':
    unittest.main()
