import unittest
import functions

class TestFunctions(unittest.TestCase):

    def test_product(self): 
        self.assertEqual(functions.add_by(5,5),25)
        self.assertEqual(functions.add_by(5,5),25)
        self.assertEqual(functions.add_by(5,5),25)
        self.assertEqual(functions.add_by(1,1),1)
    
    def test_sum_by(self):
        self.assertEqual(functions.sum_by(5,5),10)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            self.assertFalse(functions.compare_value('a',2))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=0).run(suite)