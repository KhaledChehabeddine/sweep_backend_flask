import main
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = main.app.test_client()
        self.app.testing = True

    def test_status_code(self) -> None:
        self.assertEqual(self.app.get('/').status_code, 200)

    def test_message(self) -> None:
        self.assertEqual(self.app.get('/'), main.wrap_html("Hello World!"))


if __name__ == '__main__':
    unittest.main()
