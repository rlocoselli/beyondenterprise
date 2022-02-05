import unittest

class TestStringMethods(unittest.TestCase):

    def test_string_reverse(self):
        
        string = "rodrigo"
        stringReverse = ""

        for i in range(len(string) -1 ,-1,-1):
            stringReverse += string[i]
        
        self.assertEqual(stringReverse, 'ogirdor')

if __name__ == '__main__':
    unittest.main()