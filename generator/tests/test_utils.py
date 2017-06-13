from django.test import TestCase

from ..utils import generate_a_short_url


class TestUtils(TestCase):

    def test_accurate_short_url(self):
        size = 6
        short_url = generate_a_short_url(size=size)
        self.assertEqual(len(short_url), size)
