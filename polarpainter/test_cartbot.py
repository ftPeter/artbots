from unittest import TestCase
import math
from cart_to_bot import cartbot


class TestCartbot(TestCase):
    def test_cartbot(self):
        self.assertTupleEqual(cartbot(0,0), (0,2))
        self.assertTupleEqual(cartbot(2, 0), (2, 0))
        self.assertTupleEqual(cartbot(1, 0), (1, 1))
        self.assertTupleEqual(cartbot(0, 2), (2, math.sqrt(2)*2))
        self.assertTupleEqual(cartbot(1, 1), (math.sqrt(2)*1, math.sqrt(2)*1))
