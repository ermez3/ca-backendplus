import unittest
import optimizing_pathfinding_algorithm


class Test_Kata_Optimizing_Pathfinding_Algorithm(unittest.TestCase):
        def test_cata(self):
                get_number_of_reachable_fields = optimizing_pathfinding_algorithm.get_number_of_reachable_fields
                test = self
                grid = [[1,1,1],
                        [0,0,1],
                        [0,1,0]]
                test.assertEquals(get_number_of_reachable_fields(grid, 3, 3, 0, 0), 0)
                grid = [[1],
                        [1]]
                test.assertEquals(get_number_of_reachable_fields(grid, 2, 1, 0, 0), 1)
                grid = [[0,0,1],
                        [1,0,1],
                        [1,1,0]]
                test.assertEquals(get_number_of_reachable_fields(grid, 3, 3, 1, 0), 2)

if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kata_Optimizing_Pathfinding_Algorithm)
        unittest.TextTestRunner(verbosity=0).run(suite)