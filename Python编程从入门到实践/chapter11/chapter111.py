import unittest
from Python编程从入门到实践.chapter10.chapter105 import get_names


class IOFileTest(unittest.TestCase):

    def test_get_name(self):

        result_name = get_names('wang', 'bo')
        print(result_name)
        self.assertEqual(result_name, 'wang bo')


unittest.main()
