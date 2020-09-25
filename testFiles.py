import unittest 
from project2 import marriage_after_14
import datetime

class MarriageAfter14Test(unittest.TestCase):

    
    """ Test the marriage_after_14 function from US10 """


    #create some birthdays
    birth_date_one = datetime.datetime.strptime("1990-08-01", "%Y-%m-%d")
    birth_date_two = datetime.datetime.strptime("2000-08-01", "%Y-%m-%d")
    birth_date_three = datetime.datetime.strptime("2001-08-01", "%Y-%m-%d")

    #create some marriages 
    marriage_date_one = datetime.datetime.strptime("2014-08-01", "%Y-%m-%d")
    marriage_date_two = datetime.datetime.strptime("2014-08-02", "%Y-%m-%d")

    def test_marriage_after_14_errors(self):

        """ Test the error catching of marriage_after_14 """

        with self.assertRaises(ValueError):
            marriage_after_14(MarriageAfter14Test.marriage_date_one, MarriageAfter14Test.birth_date_three)

    def test_marriage_after_14_no_errors(self):

        """ Test the inputs of the marriage_after_14 function """

        self.assertTrue(marriage_after_14(MarriageAfter14Test.marriage_date_one, MarriageAfter14Test.birth_date_two))
        self.assertTrue(marriage_after_14(MarriageAfter14Test.marriage_date_one, MarriageAfter14Test.birth_date_one))
        self.assertTrue(marriage_after_14(MarriageAfter14Test.marriage_date_two, MarriageAfter14Test.birth_date_one))
        self.assertTrue(marriage_after_14(MarriageAfter14Test.marriage_date_two, MarriageAfter14Test.birth_date_two))



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)