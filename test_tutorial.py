import unittest
import passwordGenerator

import itertools
import collections

class TestPasswordGenerator(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_length(self):
        password = passwordGenerator.generatePassword()
        self.assertTrue( len(password) > 12)
        
    def test_upper_and_lower(self):
        password = passwordGenerator.generatePassword()
        
        self.assertTrue(any(x.isupper() for x in password))
        self.assertTrue(any(x.islower() for x in password))

    def test_number(self):
        password = passwordGenerator.generatePassword()
        self.assertTrue( any(x.isdigit() for x in password))
    
    def test_unique_string(self):
        array_of_pwd = []
        
        for _ in itertools.repeat(None, 10):
            array_of_pwd.append(passwordGenerator.generatePassword())
            # print array_of_pwd[-1] #f you want to print our passwords
        
        self.assertFalse([item for item, count in collections.Counter(array_of_pwd).items() if count > 1])
      
            
if __name__ == '__main__':
    unittest.main()
    
    