from django.test import TestCase


class MyFirstTest(TestCase):

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 3)
