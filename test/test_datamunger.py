try:
    from code.datamunger import check_row
except ImportError:
    from datamunger import check_row
import unittest

class TestDatamunger(unittest.TestCase):

    def test_only_tall(self):
        test_data = "446,,,,,,,,,"
        str_vals  = test_data.strip().split(",")
        prev = [0,0,0,0,0,0,0,0,0,0]
        row = 2
        self.assertTrue(check_row(row, prev, str_vals), 'Invalid Data at Row: ' + str(row))

    def test_no_last_value(self):
        test_data = "764,74,145,50,44,242,97,51,61,"
        str_vals  = test_data.strip().split(",")
        prev = [748,73,143,49,43,237,97,50,56,0]
        row = 15
        self.assertTrue(check_row(15, prev, str_vals), 'Invalid Data at Row: ' + str(row))

    def test_all_values(self):
        test_data = "919,125,152,62,59,260,108,61,92,0"
        str_vals  = test_data.strip().split(",")
        prev = [865,94,147,60,54,257,106,60,87,0]
        row = 23
        self.assertTrue(check_row(23, prev, str_vals), 'Invalid Data at Row: ' + str(row))

    def test_only_last_value(self):
        test_data = ",,,,,,,,,0"
        str_vals  = test_data.strip().split(",")
        prev = [1195,173,180,93,109,296,145,78,121,0]
        row = 38
        self.assertTrue(check_row(38, prev, str_vals), 'Invalid Data at Row: ' + str(row))

    def test_one_missing(self):
        test_data = "1467,,225,119,174,321,205,94,135,182"
        str_vals  = test_data.strip().split(",")
        prev = [1453,192,221,119,167,320,204,94,136,180]
        row = 47
        self.assertTrue(check_row(47, prev, str_vals), 'Invalid Data at Row: ' + str(row))

if __name__ == '__main__':
    unittest.main()
