import unittest
import pytest
from josephus import josephus


class TestJosephus(unittest.TestCase):
    """ Testing the josephus function
        - Test Invalid parameters
        - What happens if n = k?
        - What happens if n = 3 and k = 2?
        - What happens if n is very large, but k =2?
        - Choose a couple of other cases to test
    """

    def test_n_equals_k(self):
        result = josephus(2, 2)
        expected = 0
        self.assertEqual(expected, result)

    def test_case_1(self):
        result = josephus(3, 2)
        expected = 2
        self.assertEqual(expected, result)

    def test_n_large_k_small(self):
        result = josephus(1000, 2)
        expected = 976
        self.assertEqual(expected, result)

    def test_k_large(self):
        result = josephus(30, 20)
        expected = 25
        self.assertEqual(expected, result)

    def test_n_k_equals_0(self):
        result = josephus(0, 0)
        expected = 0
        self.assertEqual(expected, result)

    def test_invalid_params(self):
        with pytest.raises(TypeError) as e:
            josephus('a', 'k')
            assert e.message == "unsupported operand type(s) " \
                                "for -: 'str' and 'int'"
