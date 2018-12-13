import unittest
from Python编程从入门到实践.chapter11.chapter112 import get_format_name


class FullNameTest(unittest.TestCase):

    def test_get_format_name(self):
        result = get_format_name('wang', 'bo', 'bo')
        self.assertEqual(result, 'wangbobo')


if __name__ == '__main__':
    unittest.main()
