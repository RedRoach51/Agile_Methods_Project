import unittest
from individualClass import individualClass as indiClass
from collections import OrderedDict
from project2 import main, story1

class test1(unittest.TestCase):
    def test1(self):
        indiDict = OrderedDict()
        tup1 = main('FamilyTree.ged')
        tup2 = main('FalseBday.ged')
        tup3 = main('FalseDeath.ged')
        tup4 = main('FalseDivorce.ged')
        tup5 = main('FalseMarriage.ged')
        self.assertEqual(story1(tup1[0], tup1[1]),True)
        self.assertEqual(story1(tup2[0], tup2[1]),False)
        self.assertEqual(story1(tup3[0], tup3[1]),False)
        self.assertEqual(story1(tup4[0], tup4[1]),False)
        self.assertEqual(story1(tup5[0], tup5[1]),False)

if __name__ == '__main__':
    unittest.main()
