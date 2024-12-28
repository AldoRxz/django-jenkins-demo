from django.test import TestCase

class SimpleTestCase(TestCase):

    def test_always_passes(self):
        self.assertEqual(1, 1)

    def test_another_pass(self):
        self.assertEqual(2, 2)

    def test_string_comparison(self):
        self.assertEqual("hello", "hello")

    def test_true_is_true(self):
        self.assertTrue(True)

    def test_false_is_false(self):
        self.assertFalse(False)

