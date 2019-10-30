import unittest
import random

from verify import verify
from generate import generate

class UnitTest(unittest.TestCase):
    def testGenerate(self):
        for i in range(1, 16) :
            self.assertEqual(verify(generate(str(random.randint((10 ** (i-1)), (10 ** i))))) % 10 == 0, True)

if __name__ == '__main__':
    unittest.main()