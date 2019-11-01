import unittest
import random

from verify import verify
from generate import generate

"""Unit tests class.
We generate random numbers from 1 digit long to 15 digit long, feed them to the generate function and then verify the numbers.
This way we can check both functions at the same time to be sure that they give good results.
"""
class UnitTest(unittest.TestCase):
    def testGenerate(self):
        for i in range(1, 16) :
            self.assertEqual(verify(generate(str(random.randint((10 ** (i-1)), (10 ** i))))) % 10 == 0, True)

if __name__ == '__main__':
    unittest.main()