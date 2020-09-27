import unittest
from individualClass import individualClass

class testFiles(unittest.TestCase):

    def testBirthDeathValid1(self):
        test = individualClass();
        test.Set_birthday("1990-10-29")
        test.Set_death("1990-10-30")
        self.assertEqual(test.Check_valid_birth_death(),True,"Death is set after Birth");

    def testBirthDeathValid2(self):
        test = individualClass();
        test.Set_birthday("190-1-14")
        test.Set_death("2000-8-23")
        self.assertEqual(test.Check_valid_birth_death(),True,"Death is set after Birth");

    def testBirthDeathValid3(self):
        test = individualClass();
        test.Set_birthday("1990-11-1")
        test.Set_death("1990-4-24")
        self.assertEqual(test.Check_valid_birth_death(),False,"Death is set before Birth");

    def testBirthDeathValid4(self):
        test = individualClass();
        test.Set_birthday("1990-10-29")
        self.assertEqual(test.Check_valid_birth_death(),True,"Death has not happened");

    def testBirthDeathValid5(self):
        test = individualClass();
        test.Set_birthday("1503-4-22")
        test.Set_death("1503-7-11")
        self.assertEqual(test.Check_valid_birth_death(),True,"Death is set after Birth");

test = individualClass();
test.Set_birthday("10-1-14")
test.Set_death("2000-8-23")
test.Check_valid_birth_death();
