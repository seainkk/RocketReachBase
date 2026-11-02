import unittest

from main import greeting


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greeting(), "Hello, World!")

    def test_named_greeting(self):
        self.assertEqual(greeting("RocketReachBase"), "Hello, RocketReachBase!")


if __name__ == "__main__":
    unittest.main()
