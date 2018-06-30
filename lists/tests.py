from django.test import TestCase


class SmokeTest(TestCase):

    def test_conta_errada(self):
        self.assertEqual(1 + 1, 3)
